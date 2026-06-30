/**
 * FIX JODIT INDENT/OUTDENT CHO BULLET POINT CẤP 1/2/3
 * 
 * Jodit mặc định khi indent chỉ thêm margin-left thay vì tạo nested <ul>.
 * Outdent cũng bị lỗi tương tự.
 * 
 * File này cung cấp hàm setupJoditListFix(editor) để gắn vào afterInit event.
 * Dùng editor.e.on() để đảm bảo có tham chiếu editor đúng 100%.
 */

/**
 * Tìm thẻ <li> gần nhất chứa con trỏ hiện tại
 */
function findCurrentLi(editor: any): HTMLLIElement | null {
  try {
    const sel = editor.selection;
    if (!sel) return null;
    const current = sel.current();
    if (!current) return null;
    
    if (current instanceof HTMLElement) {
      return (current.tagName === 'LI' ? current : current.closest('li')) as HTMLLIElement | null;
    }
    // Text node
    return (current.parentElement?.closest('li') || null) as HTMLLIElement | null;
  } catch {
    return null;
  }
}

/**
 * INDENT: Đẩy <li> vào sâu hơn 1 cấp bằng cách tạo nested <ul> thật
 */
function handleIndent(editor: any): boolean | void {
  const li = findCurrentLi(editor);
  if (!li) return; // Không ở trong list → để Jodit xử lý
  
  const parentList = li.parentElement;
  if (!parentList || (parentList.tagName !== 'UL' && parentList.tagName !== 'OL')) return;
  
  const prevLi = li.previousElementSibling as HTMLElement | null;
  if (!prevLi || prevLi.tagName !== 'LI') {
    return false; // Item đầu tiên, không indent được
  }
  
  // Tìm nested list đã tồn tại cuối prevLi
  let nestedList: Element | null = null;
  for (let i = prevLi.children.length - 1; i >= 0; i--) {
    const child = prevLi.children[i];
    if (child.tagName === 'UL' || child.tagName === 'OL') {
      nestedList = child;
      break;
    }
  }
  
  // Chưa có thì tạo mới cùng loại với parent
  if (!nestedList) {
    nestedList = editor.createInside.element(parentList.tagName.toLowerCase());
    prevLi.appendChild(nestedList);
  }
  
  // Xóa margin-left rác
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');
  
  // Nhét li vào nested list
  nestedList.appendChild(li);
  
  // Đặt lại con trỏ
  editor.selection.setCursorIn(li);
  return false; // Chặn Jodit mặc định
}

/**
 * OUTDENT: Kéo <li> ra ngoài 1 cấp
 */
function handleOutdent(editor: any): boolean | void {
  const li = findCurrentLi(editor);
  if (!li) return;
  
  const parentList = li.parentElement;
  if (!parentList || (parentList.tagName !== 'UL' && parentList.tagName !== 'OL')) return;
  
  // Xóa margin-left rác
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');
  
  const grandParentLi = parentList.parentElement;
  // Kiểm tra xem parentList có nằm trong một LI cha không
  if (grandParentLi && grandParentLi.tagName === 'LI') {
    // ===== ĐANG Ở NESTED LIST → KÉO RA 1 CẤP =====
    const grandParentList = grandParentLi.parentElement;
    if (!grandParentList) return;
    
    // Thu thập siblings phía sau
    const siblingsAfter: Node[] = [];
    let next = li.nextSibling;
    while (next) {
      siblingsAfter.push(next);
      next = next.nextSibling;
    }
    
    // Chèn li ra cấp cha, ngay sau grandParentLi
    grandParentList.insertBefore(li, grandParentLi.nextSibling);
    
    // Siblings phía sau → nhét vào nested list mới gắn vào li
    if (siblingsAfter.length > 0) {
      const newList = editor.createInside.element(parentList.tagName.toLowerCase());
      siblingsAfter.forEach((sib: Node) => newList.appendChild(sib));
      li.appendChild(newList);
    }
    
    // Dọn nested list cũ nếu rỗng
    if (parentList.children.length === 0) {
      parentList.remove();
    }
    
    editor.selection.setCursorIn(li);
    return false;
  } else {
    // ===== ĐÃ Ở CẤP NGOÀI CÙNG → CHUYỂN THÀNH <p> =====
    const p = editor.createInside.element('p');
    
    // Tìm nested list con
    const childLists: Element[] = [];
    const contentNodes: Node[] = [];
    
    Array.from(li.childNodes).forEach((child: any) => {
      if (child.tagName === 'UL' || child.tagName === 'OL') {
        childLists.push(child);
      } else {
        contentNodes.push(child);
      }
    });
    
    // Đưa nội dung vào <p> (move, không clone)
    contentNodes.forEach((node: Node) => p.appendChild(node));
    
    // Thu thập siblings phía sau
    const siblingsAfter: Node[] = [];
    let next = li.nextSibling;
    while (next) {
      siblingsAfter.push(next);
      next = next.nextSibling;
    }
    
    // Chèn <p> sau parentList
    if (parentList.parentNode) {
      parentList.parentNode.insertBefore(p, parentList.nextSibling);
    }
    
    // Siblings phía sau → tạo list mới sau <p>
    if (siblingsAfter.length > 0) {
      const newList = editor.createInside.element(parentList.tagName.toLowerCase());
      siblingsAfter.forEach((sib: Node) => newList.appendChild(sib));
      if (p.parentNode) {
        p.parentNode.insertBefore(newList, p.nextSibling);
      }
    }
    
    // Nested list con → đặt sau <p>
    childLists.forEach((list: Element) => {
      if (p.parentNode) {
        p.parentNode.insertBefore(list, p.nextSibling);
      }
    });
    
    // Xóa li cũ, dọn list rỗng
    li.remove();
    if (parentList.children.length === 0) {
      parentList.remove();
    }
    
    editor.selection.setCursorIn(p);
    return false;
  }
}

/**
 * GẮN VÀO EDITOR INSTANCE:
 * Gọi hàm này trong events.afterInit để đảm bảo editor instance đúng 100%.
 */
export function setupJoditListFix(editor: any) {
  editor.e.on('beforeCommand', (command: string): false | void => {
    if (command === 'indent') {
      return handleIndent(editor);
    }
    if (command === 'outdent') {
      return handleOutdent(editor);
    }
  });
}
