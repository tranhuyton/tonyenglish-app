/**
 * FIX TAB INDENT/OUTDENT TRONG LIST CHO JODIT + REACT
 * 
 * Gắn addEventListener trực tiếp vào contenteditable DOM element,
 * dùng CAPTURE PHASE để chạy TRƯỚC mọi handler khác.
 * Bypass hoàn toàn: Jodit event system, React synthetic events, Jodit plugins.
 */

export function setupListIndent(editor: any) {
  if (!editor) return;

  const attach = () => {
    // editor.editor = thẻ contenteditable div bên trong Jodit
    const el = editor.editor;
    if (!el) return;

    console.log('[joditFix] ✅ Attached Tab handler to contenteditable element');

    // CAPTURE PHASE = chạy trước tất cả handlers khác
    el.addEventListener('keydown', (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;

      // Tìm LI chứa con trỏ
      const sel = window.getSelection();
      if (!sel || !sel.rangeCount) return;
      
      const range = sel.getRangeAt(0);
      let node: Node | null = range.startContainer;
      
      // Tìm LI gần nhất
      let li: HTMLElement | null = null;
      while (node && node !== el) {
        if (node.nodeType === 1 && (node as HTMLElement).tagName === 'LI') {
          li = node as HTMLElement;
          break;
        }
        node = node.parentNode;
      }

      if (!li) return; // Không ở trong list → bỏ qua

      // CHẶN TẤT CẢ handler khác
      e.preventDefault();
      e.stopPropagation();
      e.stopImmediatePropagation();

      if (e.shiftKey) {
        doOutdent(editor, li);
      } else {
        doIndent(editor, li);
      }
    }, true); // true = CAPTURE PHASE

    // Bắt nút indent/outdent trên toolbar
    editor.e.on('beforeCommand.listfix', (command: string) => {
      if (command !== 'indent' && command !== 'outdent') return;

      const sel = window.getSelection();
      if (!sel || !sel.rangeCount) return;
      
      const range = sel.getRangeAt(0);
      let node: Node | null = range.startContainer;
      let li: HTMLElement | null = null;
      while (node && node !== el) {
        if (node.nodeType === 1 && (node as HTMLElement).tagName === 'LI') {
          li = node as HTMLElement;
          break;
        }
        node = node.parentNode;
      }

      if (!li) return;

      if (command === 'indent') {
        doIndent(editor, li);
      } else {
        doOutdent(editor, li);
      }

      return false;
    });
  };

  // Đợi editor ready
  if (editor.isReady) {
    attach();
  } else if (editor.waitForReady) {
    editor.waitForReady().then(attach);
  } else {
    // Fallback: thử sau 500ms
    setTimeout(attach, 500);
  }
}

function doIndent(editor: any, li: HTMLElement) {
  const parentList = li.parentElement;
  if (!parentList || !isListTag(parentList.tagName)) return;

  const prevLi = li.previousElementSibling;
  if (!prevLi || prevLi.tagName !== 'LI') return;

  let nestedList: Element | null = null;
  const lastChild = prevLi.lastElementChild;
  if (lastChild && isListTag(lastChild.tagName)) {
    nestedList = lastChild;
  }

  if (!nestedList) {
    nestedList = document.createElement(parentList.tagName.toLowerCase());
    prevLi.appendChild(nestedList);
  }

  nestedList.appendChild(li);
  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');

  placeCursor(li);
  editor.setEditorValue();
}

function doOutdent(editor: any, li: HTMLElement) {
  const parentList = li.parentElement;
  if (!parentList || !isListTag(parentList.tagName)) return;

  const grandParentLi = parentList.parentElement;
  if (!grandParentLi || grandParentLi.tagName !== 'LI') return;

  const grandParentList = grandParentLi.parentElement;
  if (!grandParentList) return;

  const siblingsAfter: Node[] = [];
  let next = li.nextSibling;
  while (next) {
    siblingsAfter.push(next);
    next = next.nextSibling;
  }

  grandParentList.insertBefore(li, grandParentLi.nextSibling);

  if (siblingsAfter.length > 0) {
    const newList = document.createElement(parentList.tagName.toLowerCase());
    siblingsAfter.forEach(sib => newList.appendChild(sib));
    li.appendChild(newList);
  }

  if (parentList.children.length === 0) {
    parentList.remove();
  }

  li.style.removeProperty('margin-left');
  li.style.removeProperty('padding-left');

  placeCursor(li);
  editor.setEditorValue();
}

function placeCursor(li: HTMLElement) {
  const sel = window.getSelection();
  if (!sel) return;
  const range = document.createRange();
  
  // Đặt cursor vào text node đầu tiên trong li
  const walker = document.createTreeWalker(li, NodeFilter.SHOW_TEXT, null);
  const firstText = walker.nextNode();
  if (firstText) {
    range.setStart(firstText, 0);
    range.collapse(true);
  } else {
    range.selectNodeContents(li);
    range.collapse(true);
  }
  sel.removeAllRanges();
  sel.addRange(range);
}

function isListTag(tagName: string): boolean {
  return tagName === 'UL' || tagName === 'OL';
}
