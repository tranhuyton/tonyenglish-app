/**
 * FIX JODIT INDENT/OUTDENT CHO BULLET POINT CẤP 1/2/3
 * 
 * Jodit mặc định khi indent thì chỉ thêm margin-left vào <li> thay vì
 * tạo nested <ul> bên trong. Điều này khiến CSS phân cấp (disc/circle/square)
 * không hoạt động.
 * 
 * File này override cả 2 lệnh indent và outdent để thao tác DOM trực tiếp:
 * - indent: Nhét <li> hiện tại vào một <ul> con nằm bên trong <li> phía trên
 * - outdent: Kéo <li> ra khỏi <ul> con, đưa lên cấp cha
 */

/**
 * Tìm thẻ <li> gần nhất chứa con trỏ hiện tại
 */
function findCurrentLi(editor: any): HTMLLIElement | null {
  const current = editor.selection.current();
  if (!current) return null;
  
  if (current instanceof HTMLElement) {
    return current.tagName === 'LI' ? current : current.closest('li');
  }
  // Text node
  return current.parentElement?.closest('li') || null;
}

/**
 * XỬ LÝ INDENT: Đẩy <li> vào sâu hơn 1 cấp
 * 
 * Cơ chế: Lấy <li> phía trên (previousElementSibling), tìm hoặc tạo
 * một <ul>/<ol> con bên trong nó, rồi nhét <li> hiện tại vào đó.
 * 
 * Trước:  <ul>
 *           <li>A</li>       ← li trước
 *           <li>B</li>       ← li hiện tại (đang bấm indent)
 *         </ul>
 * 
 * Sau:    <ul>
 *           <li>A
 *             <ul>
 *               <li>B</li>   ← đã nhét vào nested list
 *             </ul>
 *           </li>
 *         </ul>
 */
function handleIndent(editor: any): boolean | void {
  const li = findCurrentLi(editor);
  if (!li) return; // Không đang ở trong list → để Jodit xử lý bình thường
  
  const parentList = li.parentElement;
  if (!parentList || (parentList.tagName !== 'UL' && parentList.tagName !== 'OL')) return;
  
  const prevLi = li.previousElementSibling;
  if (!prevLi || prevLi.tagName !== 'LI') {
    // Item đầu tiên trong list, không thể indent thêm
    return false;
  }
  
  // Tìm <ul>/<ol> con đã tồn tại bên trong prevLi
  let nestedList: Element | null = null;
  for (let i = prevLi.children.length - 1; i >= 0; i--) {
    const child = prevLi.children[i];
    if (child.tagName === 'UL' || child.tagName === 'OL') {
      nestedList = child;
      break;
    }
  }
  
  // Nếu chưa có thì tạo mới
  if (!nestedList) {
    nestedList = document.createElement(parentList.tagName.toLowerCase());
    prevLi.appendChild(nestedList);
  }
  
  // Xóa margin-left rác mà Jodit có thể đã thêm trước đó
  (li as HTMLElement).style.removeProperty('margin-left');
  
  // Nhét li vào nested list
  nestedList.appendChild(li);
  
  // Đặt lại con trỏ
  editor.selection.setCursorIn(li);
  return false; // Chặn Jodit xử lý mặc định
}

/**
 * XỬ LÝ OUTDENT: Kéo <li> ra ngoài 1 cấp
 * 
 * Cơ chế: Lấy <li> ra khỏi <ul> con, đặt vào <ul> cha ngay sau <li> cha.
 * Các <li> em phía sau sẽ được giữ lại trong một <ul> con mới.
 * 
 * Trước:  <ul>
 *           <li>A
 *             <ul>
 *               <li>B</li>       ← li hiện tại (đang bấm outdent)  
 *               <li>C</li>       ← sibling phía sau
 *             </ul>
 *           </li>
 *         </ul>
 * 
 * Sau:    <ul>
 *           <li>A</li>
 *           <li>B               ← đã kéo ra cấp cha
 *             <ul>
 *               <li>C</li>     ← siblings phía sau được giữ trong nested list mới
 *             </ul>
 *           </li>
 *         </ul>
 */
function handleOutdent(editor: any): boolean | void {
  const li = findCurrentLi(editor);
  if (!li) return; // Không đang ở trong list → để Jodit xử lý bình thường
  
  const parentList = li.parentElement;
  if (!parentList || (parentList.tagName !== 'UL' && parentList.tagName !== 'OL')) return;
  
  // Xóa margin-left rác mà Jodit có thể đã thêm
  (li as HTMLElement).style.removeProperty('margin-left');
  
  const grandParentLi = parentList.parentElement?.closest('li');
  
  if (grandParentLi) {
    // ===== CÒN TRONG NESTED LIST → KÉO RA 1 CẤP =====
    const grandParentList = grandParentLi.parentElement;
    if (!grandParentList) return;
    
    // Thu thập tất cả siblings phía sau li hiện tại
    const siblingsAfter: Node[] = [];
    let next = li.nextSibling;
    while (next) {
      siblingsAfter.push(next);
      next = next.nextSibling;
    }
    
    // Chèn li ra cấp cha, ngay sau grandParentLi
    grandParentList.insertBefore(li, grandParentLi.nextSibling);
    
    // Nếu còn siblings phía sau → tạo nested list mới gắn vào li
    if (siblingsAfter.length > 0) {
      const newList = document.createElement(parentList.tagName.toLowerCase());
      siblingsAfter.forEach(sib => newList.appendChild(sib));
      li.appendChild(newList);
    }
    
    // Dọn dẹp: xóa nested list cũ nếu đã rỗng
    if (parentList.children.length === 0) {
      parentList.remove();
    }
    
    editor.selection.setCursorIn(li);
    return false;
  } else {
    // ===== ĐÃ Ở CẤP NGOÀI CÙNG → CHUYỂN THÀNH <p> =====
    const p = document.createElement('p');
    
    // Tìm các nested list con bên trong li
    const childLists: Element[] = [];
    const contentNodes: Node[] = [];
    
    Array.from(li.childNodes).forEach(child => {
      const el = child as Element;
      if (el.tagName === 'UL' || el.tagName === 'OL') {
        childLists.push(el);
      } else {
        contentNodes.push(child.cloneNode(true));
      }
    });
    
    // Đưa nội dung text vào thẻ <p>
    contentNodes.forEach(node => p.appendChild(node));
    
    // Chèn <p> vào sau parentList
    parentList.parentNode!.insertBefore(p, parentList.nextSibling);
    
    // Thu thập siblings phía sau
    const siblingsAfter: Node[] = [];
    let next = li.nextSibling;
    while (next) {
      siblingsAfter.push(next);
      next = next.nextSibling;
    }
    
    // Nếu còn siblings → tạo list mới chứa chúng, đặt sau <p>
    if (siblingsAfter.length > 0) {
      const newList = document.createElement(parentList.tagName.toLowerCase());
      siblingsAfter.forEach(sib => newList.appendChild(sib));
      parentList.parentNode!.insertBefore(newList, p.nextSibling);
    }
    
    // Đưa các nested list con ra sau <p>
    childLists.forEach(list => {
      parentList.parentNode!.insertBefore(list, p.nextSibling);
    });
    
    // Xóa li cũ và dọn dẹp
    li.remove();
    if (parentList.children.length === 0) {
      parentList.remove();
    }
    
    editor.selection.setCursorIn(p);
    return false;
  }
}

/**
 * HOOK CHÍNH: Gắn vào events.beforeCommand của Jodit
 * Chặn lệnh indent/outdent mặc định và thay bằng logic custom
 */
export const fixJoditIndentAndOutdent = function(
  command: string, _1: any, _2: any, _3: any, editor: any
) {
  if (command === 'indent') {
    return handleIndent(editor);
  }
  if (command === 'outdent') {
    return handleOutdent(editor);
  }
};
