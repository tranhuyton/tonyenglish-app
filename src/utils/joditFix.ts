/**
 * FIX JODIT v4 INDENT/OUTDENT CHO BULLET POINT CẤP 1/2/3
 * 
 * Jodit v4 plugin indent.js CHỈ thêm margin-left, KHÔNG tạo nested <ul>.
 * File này override lệnh indent/outdent khi con trỏ đang ở trong <li>
 * để tạo/xóa nested <ul> thật sự → CSS phân cấp disc/circle/square hoạt động.
 * 
 * Cách dùng: Gọi setupJoditListFix(editor) trong events.afterInit
 */

/**
 * Tìm thẻ <li> gần nhất chứa con trỏ
 */
function findCurrentLi(editor: any): HTMLLIElement | null {
  try {
    const current = editor.s.current();
    if (!current) return null;
    
    if (current instanceof HTMLElement) {
      if (current.tagName === 'LI') return current as HTMLLIElement;
      return current.closest('li') as HTMLLIElement | null;
    }
    // Text node
    return current.parentElement?.closest('li') as HTMLLIElement | null;
  } catch {
    return null;
  }
}

/**
 * INDENT: Nhét <li> vào nested <ul> bên trong <li> phía trên
 */
function handleIndent(editor: any): false | void {
  const li = findCurrentLi(editor);
  if (!li) return; // Không ở trong list → để Jodit xử lý bình thường (margin)
  
  const parentList = li.parentElement;
  if (!parentList || (parentList.tagName !== 'UL' && parentList.tagName !== 'OL')) return;
  
  const prevLi = li.previousElementSibling;
  if (!prevLi || prevLi.tagName !== 'LI') {
    return false; // Item đầu tiên, không indent được → chặn Jodit thêm margin
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
    nestedList = editor.ed.createElement(parentList.tagName.toLowerCase());
    prevLi.appendChild(nestedList);
  }
  
  // Xóa margin-left rác mà Jodit có thể đã thêm
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');
  
  // Nhét li vào nested list
  nestedList.appendChild(li);
  
  editor.s.setCursorIn(li);
  return false; // Chặn Jodit mặc định
}

/**
 * OUTDENT: Kéo <li> ra 1 cấp
 */
function handleOutdent(editor: any): false | void {
  const li = findCurrentLi(editor);
  if (!li) return;
  
  const parentList = li.parentElement;
  if (!parentList || (parentList.tagName !== 'UL' && parentList.tagName !== 'OL')) return;
  
  // Xóa margin-left rác
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');
  
  const grandParent = parentList.parentElement;
  
  if (grandParent && grandParent.tagName === 'LI') {
    // ===== ĐANG Ở NESTED LIST → KÉO RA 1 CẤP =====
    const grandParentList = grandParent.parentElement;
    if (!grandParentList) return;
    
    // Thu thập siblings phía sau li hiện tại
    const siblingsAfter: Node[] = [];
    let next = li.nextSibling;
    while (next) {
      siblingsAfter.push(next);
      next = next.nextSibling;
    }
    
    // Chèn li ra cấp cha, ngay sau grandParent LI
    grandParentList.insertBefore(li, grandParent.nextSibling);
    
    // Nếu còn siblings → tạo nested list mới gắn vào li
    if (siblingsAfter.length > 0) {
      const newList = editor.ed.createElement(parentList.tagName.toLowerCase());
      siblingsAfter.forEach((sib: Node) => newList.appendChild(sib));
      li.appendChild(newList);
    }
    
    // Dọn nested list cũ nếu rỗng
    if (parentList.children.length === 0) parentList.remove();
    
    editor.s.setCursorIn(li);
    return false;
    
  } else {
    // ===== ĐÃ Ở CẤP NGOÀI CÙNG → CHUYỂN THÀNH <p> =====
    const p = editor.ed.createElement('p');
    
    // Tách nested list con ra riêng
    const childLists: Element[] = [];
    const contentNodes: Node[] = [];
    Array.from(li.childNodes).forEach((child: any) => {
      if (child.tagName === 'UL' || child.tagName === 'OL') {
        childLists.push(child);
      } else {
        contentNodes.push(child);
      }
    });
    
    // Đưa nội dung text vào <p>
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
      const newList = editor.ed.createElement(parentList.tagName.toLowerCase());
      siblingsAfter.forEach((sib: Node) => newList.appendChild(sib));
      if (p.parentNode) p.parentNode.insertBefore(newList, p.nextSibling);
    }
    
    // Nested list con → đặt sau <p>
    childLists.forEach((list: Element) => {
      if (p.parentNode) p.parentNode.insertBefore(list, p.nextSibling);
    });
    
    li.remove();
    if (parentList.children.length === 0) parentList.remove();
    
    editor.s.setCursorIn(p);
    return false;
  }
}

/**
 * Gắn vào editor qua afterInit event.
 * Override lệnh indent/outdent KHI con trỏ đang ở trong <li>.
 */
export function setupJoditListFix(editor: any) {
  // Override indent command
  editor.registerCommand('indent', {
    exec: () => {
      const result = handleIndent(editor);
      if (result === false) return false;
    },
    hotkeys: ['ctrl+]', 'cmd+]']
  }, { priority: 1 });  // priority 1 = chạy trước plugin indent mặc định
  
  // Override outdent command
  editor.registerCommand('outdent', {
    exec: () => {
      const result = handleOutdent(editor);
      if (result === false) return false;
    },
    hotkeys: ['ctrl+[', 'cmd+[']
  }, { priority: 1 });
}
