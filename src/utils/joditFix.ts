export const fixJoditIndentAndOutdent = function(command: string, _1: any, _2: any, _3: any, editor: any) {
    if (command === 'outdent') {
        try {
            const current = editor.selection.current();
            const li = current instanceof Element ? current.closest('li') : current?.parentElement?.closest('li');
            if (!li) return; // Allow normal outdent if not in list
            
            const parentUl = li.parentElement;
            if (!parentUl || (parentUl.tagName !== 'UL' && parentUl.tagName !== 'OL')) return;
            
            const grandParentLi = parentUl.closest('li');
            
            if (grandParentLi) {
                const grandParentUl = grandParentLi.parentElement;
                if (!grandParentUl) return;

                const siblingsAfter = [];
                let next = li.nextSibling;
                while (next) {
                    siblingsAfter.push(next);
                    next = next.nextSibling;
                }

                grandParentUl.insertBefore(li, grandParentLi.nextSibling);

                if (siblingsAfter.length > 0) {
                    const newUl = document.createElement(parentUl.tagName);
                    siblingsAfter.forEach(sib => newUl.appendChild(sib));
                    li.appendChild(newUl);
                }

                if (parentUl.children.length === 0) parentUl.remove();
                
                editor.selection.setCursorIn(li);
                return false; // Prevent Jodit's default outdent
            } else {
                // Outdent to root paragraph
                const p = document.createElement('p');
                
                // Move child ULs to become siblings
                const childLists = Array.from(li.children).filter(c => c.tagName === 'UL' || c.tagName === 'OL');
                
                // Copy non-list contents to P
                Array.from(li.childNodes).forEach(child => {
                    if (child.tagName !== 'UL' && child.tagName !== 'OL') {
                        p.appendChild(child.cloneNode(true));
                    }
                });
                
                parentUl.parentNode.insertBefore(p, parentUl.nextSibling);
                
                const siblingsAfter = [];
                let next = li.nextSibling;
                while (next) {
                    siblingsAfter.push(next);
                    next = next.nextSibling;
                }
                
                if (siblingsAfter.length > 0) {
                    const newUl = document.createElement(parentUl.tagName);
                    siblingsAfter.forEach(sib => newUl.appendChild(sib));
                    parentUl.parentNode.insertBefore(newUl, p.nextSibling);
                }
                
                childLists.forEach(list => {
                    parentUl.parentNode.insertBefore(list, p.nextSibling);
                });
                
                li.remove();
                if (parentUl.children.length === 0) parentUl.remove();
                
                editor.selection.setCursorIn(p);
                return false;
            }
        } catch(e) {
            console.error("Custom outdent error", e);
        }
    }
};
