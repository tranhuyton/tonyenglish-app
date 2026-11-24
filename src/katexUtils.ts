import katex from 'katex';

export type CalculatorPolicy = 'non-calculator' | 'calculator' | null;
export type IgcseMathCode = '0580' | '0606' | null;

const escapeHtml = (str: string): string =>
  String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

/**
 * Safely renders KaTeX delimiters `\(...\)` (inline) and `\[...\]` (display) inside
 * an HTML string without ever touching `$` currency symbols.
 */
export function renderMathInHtml(html: string): string {
  if (!html || (!html.includes('\\(') && !html.includes('\\['))) return html || '';
  return html
    .replace(/\\\[([\s\S]*?)\\\]/g, (_m, expr) => {
      try {
        return `<span class="katex-display-wrap block my-2 overflow-x-auto">${katex.renderToString(expr.trim(), {
          displayMode: true,
          throwOnError: false,
          strict: false,
        })}</span>`;
      } catch {
        return expr;
      }
    })
    .replace(/\\\(([\s\S]*?)\\\)/g, (_m, expr) => {
      try {
        return katex.renderToString(expr.trim(), {
          displayMode: false,
          throwOnError: false,
          strict: false,
        });
      } catch {
        return expr;
      }
    });
}

/**
 * Renders question labels and marking schemes in IGCSE Paper/Direct exams using real KaTeX
 * when `\(...\)`, `\[...\]`, or standalone LaTeX commands (`\frac`, `\int`, `\sqrt`, etc.)
 * are present, while preserving plain-text prose safely.
 */
export function renderIgcseLatex(text: string): string {
  if (!text) return '';
  const raw = String(text);

  // Case 1: Explicit KaTeX delimiters `\(...\)` or `\[...\]`
  if (raw.includes('\\(') || raw.includes('\\[')) {
    const parts: string[] = [];
    const tokenRe = /\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g;
    let lastIdx = 0;
    let match: RegExpExecArray | null;
    while ((match = tokenRe.exec(raw)) !== null) {
      if (match.index > lastIdx) {
        parts.push(escapeHtml(raw.slice(lastIdx, match.index)));
      }
      const isDisplay = match[1] !== undefined;
      const expr = (isDisplay ? match[1] : match[2]).trim();
      try {
        parts.push(
          katex.renderToString(expr, {
            displayMode: isDisplay,
            throwOnError: false,
            strict: false,
          })
        );
      } catch {
        parts.push(escapeHtml(expr));
      }
      lastIdx = match.index + match[0].length;
    }
    if (lastIdx < raw.length) {
      parts.push(escapeHtml(raw.slice(lastIdx)));
    }
    return parts.join('');
  }

  // Case 2: Pure standalone LaTeX expression (e.g. `\pm\frac{1}{3}(x+2)(2x+1)(x-3)` in 0606 marking schemes)
  const trimmed = raw.trim();
  const looksPureLatex =
    /^\\(pm|mp|frac|sqrt|int|sum|binom|left|sin|cos|tan|ln|log)/.test(trimmed) &&
    !/\b(the|and|for|show|find|solve|given|marks?|award|accept|must|use)\b/i.test(trimmed);

  if (looksPureLatex) {
    try {
      return katex.renderToString(trimmed, {
        displayMode: false,
        throwOnError: false,
        strict: false,
      });
    } catch {
      // fall through
    }
  }

  // Case 3: Mixed prose with inline raw LaTeX fragments (e.g. `(a) Find \int_{0}^{\pi} \sin\theta d\theta.`)
  const hasRawLatex =
    raw.includes('\\') || /[\^_]\{[^}]+\}/.test(raw);
  if (!hasRawLatex) return escapeHtml(raw);

  // Convert common inline LaTeX commands cleanly with KaTeX or safe HTML fallback
  let escaped = escapeHtml(raw);
  // Render `\int_{...}^{...}` / `\frac{...}{...}` / `\sqrt{...}` / `\binom{...}{...}` via KaTeX inline
  escaped = escaped.replace(
    /(\\(?:int(?:_\{[^}]+\}\^\{[^}]+\})?|frac\{[^{}]+\}\{[^{}]+\}|sqrt\{[^{}]+\}|binom\{[^{}]+\}\{[^{}]+\}|pm|mp|pi|theta|alpha|beta|gamma|delta|leq|geq|neq|approx|infty|times|div|cdot))/g,
    (m) => {
      try {
        return katex.renderToString(m, { displayMode: false, throwOnError: false, strict: false });
      } catch {
        return m;
      }
    }
  );
  escaped = escaped
    .replace(/\^\{([^}]+)\}/g, '<sup>$1</sup>')
    .replace(/_\{([^}]+)\}/g, '<sub>$1</sub>')
    .replace(/\^\(([^)]+)\)/g, '<sup>$1</sup>')
    .replace(/\\(sin|cos|tan|sec|csc|cosec|cot|ln|log|lim)\b/g, '$1');
  return escaped;
}

export function detectCalculatorPolicy(title?: string, basicInfo?: any): CalculatorPolicy {
  const explicit = String(basicInfo?.calculatorPolicy || basicInfo?.calculator_policy || '').toLowerCase();
  if (explicit === 'non-calculator' || explicit === 'non_calculator' || explicit === 'no') return 'non-calculator';
  if (explicit === 'calculator' || explicit === 'yes') return 'calculator';

  const t = `${title || ''} ${basicInfo?.title || ''} ${basicInfo?.tags || ''}`.toLowerCase();
  if (/non[\s-]*calc|không\s*máy\s*tính|0580\/2[123]|paper\s*2\s*\(non|0606\/1[12]|paper\s*1\s*\(non/.test(t)) {
    return 'non-calculator';
  }
  if (/\[calculator\]|calculator\s*(allowed|mastery|mock|practice|drill)|0580\/4[123]|0606\/2[12]|paper\s*4\s*\(extended\)|paper\s*2\s*\(calc/.test(t)) {
    return 'calculator';
  }
  return null;
}

export function detectIgcseMathSyllabus(title?: string, courseId?: string): IgcseMathCode {
  if (String(courseId || '') === '7211abb0-ccba-479f-92ad-2d218121f717') return '0580';
  if (String(courseId || '') === '0a8d7434-262a-4462-89c1-2b01c6ea1e4e') return '0606';
  const t = String(title || '').toLowerCase();
  if (t.includes('0606') || t.includes('add maths') || t.includes('additional math')) return '0606';
  if (t.includes('0580') || t.includes('maths 0580')) return '0580';
  return null;
}
