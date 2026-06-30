/**
 * FIX TAB INDENT/OUTDENT TRONG LIST CHO JODIT + REACT
 * 
 * Plugin `tab` của Jodit v4 CÓ logic tạo nested list, nhưng jodit-react
 * khiến nó không hoạt động (có thể do event bị chặn bởi React).
 * 
 * File này gắn trực tiếp keydown handler vào Jodit instance,
 * bypass hoàn toàn plugin system.
 * 
 * Gọi: setupListIndent(joditInstance) trong editorRef callback
 */

import { Jodit } from 'jodit';

export function setupListIndent(editor: any) {
  if (!editor || !editor.e) return;

  // === Tab key handler ===
  editor.e.on('keydown.listfix', (e: KeyboardEvent) => {
    if (e.key !== 'Tab') return;

    const current = editor.s.current();
    if (!current) return;

    // Tìm LI chứa con trỏ
    const li = (current.nodeType === 1) 
      ? (current as HTMLElement).closest('li') 
      : current.parentElement?.closest('li');
    if (!li) return; // Không ở trong list → bỏ qua

    e.preventDefault();
    e.stopImmediatePropagation();

    if (e.shiftKey) {
      doOutdent(editor, li);
    } else {
      doIndent(editor, li);
    }
    
    return false;
  });

  // === Indent/Outdent toolbar button handler ===
  editor.e.on('beforeCommand.listfix', (command: string) => {
    if (command !== 'indent' && command !== 'outdent') return;

    const current = editor.s.current();
    if (!current) return;

    const li = (current.nodeType === 1)
      ? (current as HTMLElement).closest('li')
      : current.parentElement?.closest('li');
    if (!li) return;

    if (command === 'indent') {
      doIndent(editor, li);
    } else {
      doOutdent(editor, li);
    }

    return false; // Chặn Jodit default (margin-left)
  });
}

/**
 * INDENT: Chuyển LI vào nested list bên trong LI phía trước
 */
function doIndent(editor: any, li: HTMLElement) {
  const parentList = li.parentElement;
  if (!parentList || !isListTag(parentList.tagName)) return;

  const prevLi = li.previousElementSibling;
  if (!prevLi || prevLi.tagName !== 'LI') return; // Phải có LI phía trước

  // Tìm nested list đã có cuối prevLi
  let nestedList: Element | null = null;
  const lastChild = prevLi.lastElementChild;
  if (lastChild && isListTag(lastChild.tagName)) {
    nestedList = lastChild;
  }

  // Chưa có → tạo mới cùng loại
  if (!nestedList) {
    nestedList = document.createElement(parentList.tagName.toLowerCase());
    // Copy attributes từ parent list
    Array.from(parentList.attributes).forEach(attr => {
      (nestedList as Element).setAttribute(attr.name, attr.value);
    });
    prevLi.appendChild(nestedList);
  }

  // Di chuyển LI vào nested list
  nestedList.appendChild(li);

  // Xóa margin-left rác
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');

  // Đặt lại cursor
  editor.s.setCursorIn(li, false);
  editor.setEditorValue();
}

/**
 * OUTDENT: Kéo LI ra cấp cha
 */
function doOutdent(editor: any, li: HTMLElement) {
  const parentList = li.parentElement;
  if (!parentList || !isListTag(parentList.tagName)) return;

  const grandParentLi = parentList.parentElement;
  if (!grandParentLi || grandParentLi.tagName !== 'LI') return; // Đã ở cấp ngoài cùng

  const grandParentList = grandParentLi.parentElement;
  if (!grandParentList) return;

  // Thu thập siblings sau li hiện tại
  const siblingsAfter: Node[] = [];
  let next = li.nextSibling;
  while (next) {
    siblingsAfter.push(next);
    next = next.nextSibling;
  }

  // Chèn li vào sau grandParentLi
  grandParentList.insertBefore(li, grandParentLi.nextSibling);

  // Nếu có siblings sau → tạo nested list mới gắn vào li
  if (siblingsAfter.length > 0) {
    const newList = document.createElement(parentList.tagName.toLowerCase());
    siblingsAfter.forEach(sib => newList.appendChild(sib));
    li.appendChild(newList);
  }

  // Dọn list cũ nếu rỗng
  if (parentList.children.length === 0) {
    parentList.remove();
  }

  // Xóa margin-left rác
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');

  // Đặt lại cursor
  editor.s.setCursorIn(li, false);
  editor.setEditorValue();
}

function isListTag(tagName: string): boolean {
  return tagName === 'UL' || tagName === 'OL';
}
