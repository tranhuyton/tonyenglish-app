import React, { useState, useEffect, useCallback, useMemo, useRef } from 'react';
import { supabase } from './supabase';

// =========================================================================================
// THƯ VIỆN ĐỌC PDF - TÍCH HỢP JUMP TO PAGE & VISION AI
// =========================================================================================
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';

pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

const PdfVisionViewer = ({ url, onClose, onCallTutor }: { url: string, onClose: () => void, onCallTutor?: () => void }) => {
  const [numPages, setNumPages] = useState<number | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [pageInput, setPageInput] = useState<string>('1'); 
  const [isLoading, setIsLoading] = useState(true);
  const [isTwoPageMode, setIsTwoPageMode] = useState(false);
  const [zoomLevel, setZoomLevel] = useState<number>(1.2);
  const [isFullscreen, setIsFullscreen] = useState(false);
  
  const viewerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
      setPageInput(currentPage.toString());
  }, [currentPage]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (['INPUT', 'TEXTAREA'].includes((e.target as HTMLElement).tagName)) {
          return;
      }
      
      if (e.key === 'ArrowRight') {
          handleNext();
      } else if (e.key === 'ArrowLeft') {
          handlePrev();
      } else if (e.key === '=' || e.key === '+') {
          handleZoomIn();
      } else if (e.key === '-' || e.key === '_') {
          handleZoomOut();
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [numPages, currentPage, isTwoPageMode]);

  useEffect(() => {
    const onFullscreenChange = () => {
        setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', onFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
      if (!document.fullscreenElement) {
          viewerRef.current?.requestFullscreen().catch(err => console.log(err));
      } else {
          document.exitFullscreen();
      }
  };

  const handlePageRenderSuccess = () => {
    clearTimeout((window as any).pdfCaptureTimeout);
    (window as any).pdfCaptureTimeout = setTimeout(() => {
      setIsLoading(false);
      const canvases = document.querySelectorAll('.react-pdf__Page__canvas');
      
      if (canvases.length > 0) {
        const combinedCanvas = document.createElement('canvas');
        const ctx = combinedCanvas.getContext('2d');
        
        let totalW = 0;
        let maxH = 0;
        
        canvases.forEach(c => {
            totalW += (c as HTMLCanvasElement).width;
            maxH = Math.max(maxH, (c as HTMLCanvasElement).height);
        });

        const MAX_WIDTH = 800;
        const scaleFactor = totalW > MAX_WIDTH ? MAX_WIDTH / totalW : 1;

        combinedCanvas.width = totalW * scaleFactor;
        combinedCanvas.height = maxH * scaleFactor;
        
        let curX = 0;
        canvases.forEach(c => {
            if (ctx) {
                const drawWidth = (c as HTMLCanvasElement).width * scaleFactor;
                const drawHeight = (c as HTMLCanvasElement).height * scaleFactor;
                ctx.drawImage(c as HTMLCanvasElement, curX, 0, drawWidth, drawHeight);
                curX += drawWidth;
            }
        });

        const base64Image = combinedCanvas.toDataURL('image/jpeg', 0.45); 
        (window as any).tonyLatestPdfPageImage = base64Image;
        window.dispatchEvent(new CustomEvent('tony-send-page-image', { detail: base64Image }));
      }
    }, 500);
  };

  const handleNext = () => {
      if (numPages && currentPage < numPages) {
          setIsLoading(true);
          setCurrentPage(p => Math.min(p + (isTwoPageMode ? 2 : 1), numPages || 1));
      }
  };

  const handlePrev = () => {
      if (currentPage > 1) {
          setIsLoading(true);
          setCurrentPage(p => Math.max(p - (isTwoPageMode ? 2 : 1), 1));
      }
  };

  const handlePageInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      setPageInput(e.target.value);
  };

  const handlePageInputSubmit = (e: React.KeyboardEvent<HTMLInputElement>) => {
      if (e.key === 'Enter') {
          let p = parseInt(pageInput);
          if (!isNaN(p)) {
              p = Math.max(1, Math.min(p, numPages || 1));
              setIsLoading(true);
              setCurrentPage(p);
              setPageInput(p.toString());
          } else {
              setPageInput(currentPage.toString());
          }
      }
  };

  const handleZoomIn = () => {
      setZoomLevel(prev => Math.min(prev + 0.2, 3.0));
  };
  
  const handleZoomOut = () => {
      setZoomLevel(prev => Math.max(prev - 0.2, 0.5));
  };

  return (
    <div ref={viewerRef} className="w-full h-full flex flex-col bg-[#0f172a] relative z-20 font-sans">
      <div className="flex flex-wrap items-center justify-between bg-slate-900/90 backdrop-blur-md p-2 md:p-3 shrink-0 border-b border-slate-700/50 shadow-lg gap-2 z-10">
         <div className="flex items-center gap-2 md:gap-4">
             <div className="hidden sm:flex items-center gap-2 text-emerald-400 bg-emerald-950/40 px-3 py-1.5 rounded-full border border-emerald-800/50 shadow-[0_0_10px_rgba(16,185,129,0.1)]">
                <span className="text-sm">🤖</span>
                <span className="text-[11px] md:text-xs font-semibold animate-pulse tracking-wide">AI đang hỗ trợ</span>
             </div>
             <div className="flex items-center bg-slate-800/80 rounded-lg border border-slate-700/50 p-0.5">
                <button onClick={handleZoomOut} className="w-8 h-8 flex items-center justify-center text-slate-400 hover:bg-slate-700 hover:text-white rounded-md transition-all" title="Thu nhỏ (-)">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM13.5 10.5h-6" /></svg>
                </button>
                <span className="text-slate-300 text-xs font-semibold font-mono w-12 text-center select-none">
                    {Math.round(zoomLevel * 100)}%
                </span>
                <button onClick={handleZoomIn} className="w-8 h-8 flex items-center justify-center text-slate-400 hover:bg-slate-700 hover:text-white rounded-md transition-all" title="Phóng to (+)">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607zM10.5 7.5v6m3-3h-6" /></svg>
                </button>
             </div>
         </div>
         <div className="flex items-center gap-3 flex-1 justify-center min-w-[250px]">
             <button 
                 onClick={() => { 
                     setIsTwoPageMode(!isTwoPageMode);
                 }}
                 className={`hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all border ${isTwoPageMode ? 'bg-[#0ea5e9]/20 text-[#0ea5e9] border-[#0ea5e9]/30' : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-slate-200'}`}
             >
                 {isTwoPageMode ? (
                     <><span className="text-sm">📖</span> 2 Trang</>
                 ) : (
                     <><span className="text-sm">📄</span> 1 Trang</>
                 )}
             </button>
             <div className="flex items-center gap-1 bg-slate-800/80 rounded-lg p-1 border border-slate-700/50">
                <button 
                    onClick={handlePrev} 
                    disabled={currentPage === 1} 
                    className="text-white px-3 py-1.5 rounded bg-slate-700/50 hover:bg-[#0ea5e9] font-bold text-xs disabled:opacity-30 transition-all shadow-sm"
                >
                    ←
                </button>
                <div className="flex items-center text-slate-400 text-xs font-medium px-2">
                    <input 
                        type="text" 
                        value={pageInput}
                        onChange={handlePageInputChange}
                        onKeyDown={handlePageInputSubmit}
                        onBlur={() => setPageInput(currentPage.toString())}
                        className="w-10 text-center bg-slate-900 text-white font-semibold mx-1 py-1 rounded border border-slate-600 focus:outline-none focus:border-[#0ea5e9] focus:ring-1 focus:ring-[#0ea5e9] transition-all"
                    />
                    <span className="opacity-70 mx-1">/</span> {numPages || '--'}
                </div>
                <button 
                    onClick={handleNext} 
                    disabled={numPages !== null && currentPage >= numPages} 
                    className="text-white px-3 py-1.5 rounded bg-slate-700/50 hover:bg-[#0ea5e9] font-bold text-xs disabled:opacity-30 transition-all shadow-sm"
                >
                    →
                </button>
             </div>
         </div>
         <div className="flex items-center gap-2">
             {onCallTutor && (
                 <button 
                     onClick={onCallTutor}
                     className="flex items-center gap-1.5 px-3 h-9 rounded-lg text-xs font-bold bg-emerald-500/10 border border-emerald-500/30 hover:bg-emerald-500 text-emerald-400 hover:text-white transition-all shadow-sm active:scale-95 shrink-0"
                     title="Vào lớp Học trực tiếp với Gia Sư AI"
                 >
                     <span className="animate-pulse">👨‍🏫</span>
                     <span>Lên Bảng</span>
                 </button>
             )}
             <button 
                onClick={toggleFullscreen} 
                className="w-9 h-9 rounded-lg bg-slate-800 border border-slate-700 hover:bg-slate-700 flex items-center justify-center text-slate-300 hover:text-white transition-all" 
                title="Toàn màn hình"
             >
                 {isFullscreen ? (
                     <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg>
                 ) : (
                     <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                 )}
             </button>
             <button 
                onClick={onClose} 
                className="w-9 h-9 rounded-lg bg-red-500/10 border border-red-500/30 hover:bg-red-500 flex items-center justify-center text-red-400 hover:text-white transition-all" 
                title="Đóng tài liệu"
             >
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
             </button>
         </div>
      </div>
      {/* 3D Book styles */}
      <style>{`
        .pdf-page-left { box-shadow: inset -20px 0 30px -15px rgba(0,0,0,0.25), -4px 4px 20px rgba(0,0,0,0.4); }
        .pdf-page-right { box-shadow: inset 20px 0 30px -15px rgba(0,0,0,0.25), 4px 4px 20px rgba(0,0,0,0.4); }
        .pdf-page-single { box-shadow: 0 8px 40px rgba(0,0,0,0.5), 0 2px 10px rgba(0,0,0,0.3); }
      `}</style>
      <div className="flex-1 overflow-auto flex justify-center items-start p-4 md:p-8 bg-[#020617] relative custom-scrollbar scroll-smooth">
         {isLoading && (
            <div className="absolute inset-0 flex flex-col items-center justify-center bg-[#020617]/80 backdrop-blur-sm z-10">
               <div className="w-10 h-10 border-4 border-[#0ea5e9]/20 border-t-[#0ea5e9] rounded-full animate-spin"></div>
               <span className="mt-3 text-slate-400 text-sm font-medium animate-pulse">Đang tải trang tài liệu...</span>
            </div>
         )}
         <Document 
            file={url} 
            onLoadSuccess={({ numPages }) => setNumPages(numPages)} 
            loading={null}
         >
            <div className={`flex justify-center items-start ${isTwoPageMode ? 'gap-0 flex-col lg:flex-row' : ''}`}>
               <Page 
                   pageNumber={currentPage} 
                   scale={zoomLevel} 
                   renderTextLayer={false} 
                   renderAnnotationLayer={false} 
                   onRenderSuccess={handlePageRenderSuccess} 
                   className={`overflow-hidden max-w-full bg-white ${isTwoPageMode ? 'pdf-page-left' : 'pdf-page-single'}`}
                   loading={null} 
               />
               {isTwoPageMode && numPages && currentPage + 1 <= numPages && (
                   <Page 
                       pageNumber={currentPage + 1} 
                       scale={zoomLevel} 
                       renderTextLayer={false} 
                       renderAnnotationLayer={false} 
                       onRenderSuccess={handlePageRenderSuccess} 
                       className="overflow-hidden max-w-full bg-white hidden lg:block pdf-page-right"
                       loading={null} 
                   />
               )}
           </div>
         </Document>
      </div>
    </div>
  );
};

// =========================================================================================
// 🚀 COMPONENT RENDER BÀI GIẢNG (EDTECH IFRAME STYLE)
// =========================================================================================
const StaticLectureContent = React.memo(({ html, isIframeOnly, onOpenPopup, onOpenDict, onCloseDict }: any) => {
   const iframeRef = useRef<HTMLIFrameElement>(null);
   const [iframeHeight, setIframeHeight] = useState(100);

   useEffect(() => { 
       setIframeHeight(10); 
   }, [html]);

   useEffect(() => {
     const handleMessage = (e: MessageEvent) => {
       if (e.data?.type === 'LECTURE_LINK_CLICK') {
         let href = e.data.href;
         if (href.startsWith('/')) {
             href = window.location.origin + href;
         }

         if (href.includes('tonyenglish.vn/uploads') || 
             href.includes('youtube.com') || 
             href.includes('youtu.be') || 
             href.toLowerCase().includes('.pdf')) {
             onOpenPopup(href);
         } else { 
             window.open(href, '_blank', 'noopener,noreferrer');
         }
       } else if (e.data?.type === 'LECTURE_RESIZE') {
         const h = e.data.height;
         if (h) {
             setIframeHeight(Math.max(100, h + 40));
         }
       } else if (e.data?.type === 'LECTURE_OPEN_DICT') {
         if (iframeRef.current) {
            const rect = iframeRef.current.getBoundingClientRect();
            onOpenDict(e.data.word, rect.left + e.data.x, rect.top + e.data.y, rect.top + e.data.rectTop);
         }
       } else if (e.data?.type === 'LECTURE_CLOSE_DICT') {
         onCloseDict();
       } else if (e.data?.type === 'OPEN_IELTS_AI') {
         const fakeBtn = document.createElement('button');
         fakeBtn.className = 'btn-ai-trigger hidden'; 
         
         if (e.data.topic) {
             fakeBtn.setAttribute('data-topic', e.data.topic);
         }
         if (e.data.image) {
             fakeBtn.setAttribute('data-image', e.data.image);
         }
         if (e.data.task) {
             fakeBtn.setAttribute('data-task', e.data.task);
         }
         
         document.body.appendChild(fakeBtn);
         fakeBtn.click();
         setTimeout(() => { 
             fakeBtn.remove(); 
         }, 100);
       } 
       else if (e.data?.type === 'OPEN_LIVE_SPEAKING') {
         const fakeLiveBtn = document.createElement('button');
         fakeLiveBtn.className = 'btn-live-trigger hidden';
         
         if (e.data.topic) {
             fakeLiveBtn.setAttribute('data-topic', e.data.topic);
         }
         
         document.body.appendChild(fakeLiveBtn);
         fakeLiveBtn.click();
         setTimeout(() => { 
             fakeLiveBtn.remove(); 
         }, 100);
       }
     };
     
     window.addEventListener('message', handleMessage);
     return () => window.removeEventListener('message', handleMessage);
   }, [onOpenPopup, onOpenDict, onCloseDict]);

   const iframeContent = `
     <!DOCTYPE html>
     <html lang="vi">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
       <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
       <style>
         :root {
            --brand-color: #0ea5e9;
            --text-main: #334155;
            --bg-light: #f8fafc;
         }
         html, body { 
             height: max-content !important;
             min-height: 0 !important;
             margin: 0; padding: 0; 
             font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
             color: var(--text-main);
             background: transparent; overflow: hidden; 
             line-height: 1.75;
             font-size: 17px;
             -webkit-font-smoothing: antialiased;
         }
         * { box-sizing: border-box; }
         
         /* Typography Styling cho Học thuật */
         h1, h2, h3, h4 { 
             color: #0f172a;
             font-weight: 700; 
             margin-top: 1.5em; 
             margin-bottom: 0.5em; 
             line-height: 1.3; 
         }
         h1 { 
             font-size: 1.75rem;
             border-bottom: 2px solid #e2e8f0; 
             padding-bottom: 0.3em; 
         }
         h2 { font-size: 1.5rem; }
         h3 { font-size: 1.25rem; }
         p { margin-top: 0; margin-bottom: 1.25rem; }
         
         /* Media & Elements */
         img, video { 
              max-width: 100%;
              height: auto; 
              display: block; 
              border-radius: 12px; 
              margin: 1.5rem auto; 
              box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
          }
          iframe {
               width: 100% !important;
               aspect-ratio: 16 / 9;
               border: none !important;
               margin: 0 !important;
               border-radius: 8px;
               display: block;
          }
          .iframe-only-mode iframe {
              margin: 0 !important;
              border-radius: 0 !important;
              box-shadow: none !important;
              width: 100% !important;
              min-height: 85vh !important;
          }
         svg { max-width: 100%; height: auto; pointer-events: all !important; }
         
         /* Links */
         a { 
             cursor: pointer;
             color: var(--brand-color); 
             text-decoration: none; 
             font-weight: 600; 
             border-bottom: 1px transparent; 
             transition: all 0.2s;
         }
         a:hover { 
             color: #0284c7;
             text-decoration: underline; 
             text-underline-offset: 4px; 
         }
         ::selection { background: #bae6fd; color: #0369a1; }
         
         /* EdTech Specifics */
         blockquote { 
            border-left: 4px solid var(--brand-color);
            background: var(--bg-light); 
            margin: 1.5rem 0; 
            padding: 1rem 1.5rem; 
            border-radius: 0 8px 8px 0;
            font-style: italic; 
            color: #475569;
         }
         table { 
             border-collapse: collapse;
             width: 100%; 
             margin-bottom: 1.5rem; 
             border-radius: 8px; 
             overflow: hidden; 
             box-shadow: 0 1px 3px rgba(0,0,0,0.05);
         }
         table th, table td { 
             border: 1px solid #e2e8f0;
             padding: 0.875rem 1rem; 
             vertical-align: top; 
         }
         table th { 
             background-color: var(--bg-light);
             font-weight: 600; 
             text-align: left; 
             color: #0f172a; 
         }
         table tr:nth-child(even) { background-color: #fcfcfc; }
         code { 
             font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
             font-size: 0.9em; 
             background: #f1f5f9; 
             padding: 0.2em 0.4em; 
             border-radius: 4px; 
             color: #db2777;
         }
         pre code { background: transparent; padding: 0; color: inherit; }
         pre { 
             background: #1e293b;
             color: #f8fafc; 
             padding: 1.25rem; 
             border-radius: 12px; 
             overflow-x: auto; 
             margin-bottom: 1.5rem; 
             font-size: 0.9rem;
         }
         
         #content-wrapper { display: flow-root; width: 100%; padding-bottom: 2rem; }
       </style>
     </head>
     <body class="${isIframeOnly ? 'iframe-only-mode' : ''}">
       <div id="content-wrapper">${html ? html.replace(/viewbox=/gi, 'viewBox=') : ''}</div>
       <script>
         document.addEventListener('click', function(e) {
           var target = e.target;
           
           var anchor = target.closest('a');
           if (anchor && 
               anchor.hasAttribute('href') && 
               !anchor.outerHTML.includes('openIELTSAssessor') && 
               !anchor.classList.contains('btn-ielts-trigger') && 
               !anchor.classList.contains('btn-ai-trigger') && 
               !anchor.classList.contains('btn-live-trigger')) {
                   
               e.preventDefault(); 
               var rawHref = anchor.getAttribute('href');
               window.parent.postMessage({ type: 'LECTURE_LINK_CLICK', href: rawHref }, '*'); 
               return; 
           }

           var btn = target.closest('.btn-ai-trigger, .btn-ielts-trigger, .btn-live-trigger');
           if (btn) {
               e.preventDefault(); 
               e.stopPropagation();
               e.stopImmediatePropagation();
               
               var isLive = btn.classList.contains('btn-live-trigger');
               
               var originalText = btn.innerHTML;
               btn.innerHTML = isLive ? "📞 Đang kết nối..." : "✨ Đang mở AI...";
               btn.style.opacity = "0.7";
               setTimeout(function() { 
                   btn.innerHTML = originalText; 
                   btn.style.opacity = "1"; 
               }, 1500);
               if(isLive) {
                  window.parent.postMessage({ 
                      type: 'OPEN_LIVE_SPEAKING', 
                      topic: btn.getAttribute('data-topic') || '' 
                  }, '*');
               } else {
                  window.parent.postMessage({ 
                      type: 'OPEN_IELTS_AI', 
                      topic: btn.getAttribute('data-topic') || '', 
                      image: btn.getAttribute('data-image') || '', 
                      task: btn.getAttribute('data-task') || 'task2' 
                  }, '*');
               }
               return false;
           }

         }, true);
         
         var selectionTimer = null;
         document.addEventListener('mouseup', function(e) {
           clearTimeout(selectionTimer);
           
           selectionTimer = setTimeout(function() {
               var sel = window.getSelection();
               var text = sel.toString().trim();
               
               if (text && text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
                 var range = sel.getRangeAt(0);
                 var rect = range.getBoundingClientRect();
                 window.parent.postMessage({ 
                     type: 'LECTURE_OPEN_DICT', 
                     word: text, 
                     x: rect.left + (rect.width/2), 
                     y: rect.bottom, 
                     rectTop: rect.top 
                 }, '*');
               }
           }, 150);
         });
         document.addEventListener('mousedown', function(e) {
           var sel = window.getSelection();
           if (!sel.toString().trim()) { 
               window.parent.postMessage({ type: 'LECTURE_CLOSE_DICT' }, '*'); 
           }
         });
         function reportHeight() {
            var wrapper = document.getElementById('content-wrapper');
            if (wrapper) {
                var h = wrapper.getBoundingClientRect().height;
                if (h > 0) {
                    window.parent.postMessage({ type: 'LECTURE_RESIZE', height: h }, '*');
                }
            }
         }
         
         window.addEventListener('load', reportHeight);
         if (window.ResizeObserver) {
            var ro = new ResizeObserver(reportHeight);
            ro.observe(document.body);
            ro.observe(document.getElementById('content-wrapper'));
         } else { 
            setInterval(reportHeight, 500);
         }
       </script>
     </body>
     </html>
   `;
   return (
     <div className={`w-full animate-in fade-in duration-700 relative ${isIframeOnly ? 'h-[85vh]' : ''}`}>
       <iframe
         ref={iframeRef}
         srcDoc={iframeContent}
         style={{ width: '100%', height: isIframeOnly ? '100%' : `${iframeHeight}px`, border: 'none', overflow: 'hidden' }}
         sandbox="allow-scripts allow-same-origin allow-popups"
         scrolling="no"
       />
     </div>
   );
}, (prevProps, nextProps) => prevProps.html === nextProps.html);


// =========================================================================================
// MAIN COMPONENT: LECTURE VIEWER
// =========================================================================================
export default function LectureViewer({ 
    courseId, 
    onBack, 
    onStartTest, 
    onOpenAI 
}: { 
    courseId: string, 
    onBack: () => void, 
    onStartTest?: (type: string, data: any) => void, 
    onOpenAI?: (passedMode?: string, topic?: string, image?: string, task?: string) => void 
}) {
  const [course, setCourse] = useState<any>(null);
  const [modules, setModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  
  const [pages, setPages] = useState<any[]>([]);
  const [activeLectureId, setActiveLectureId] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [completedTasks, setCompletedTasks] = useState<string[]>([]);
  const [allLectureProgress, setAllLectureProgress] = useState<Record<string, string[]>>({});
  
  const [completedLectures, setCompletedLectures] = useState<Set<string>>(new Set());
  const [viewedPages, setViewedPages] = useState<Set<number>>(new Set());
  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); 
  const [isTaskMenuOpen, setIsTaskMenuOpen] = useState(false);
  const taskMenuRef = useRef<HTMLDivElement>(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [popupUrl, setPopupUrl] = useState<string | null>(null);
  
  // 🚀 MỚI: HỨNG ẢNH ĐƯỢC UP TỪ SIDEBAR ĐỂ HIỂN THỊ NỬA TRÁI MÀN HÌNH
  const [uploadedBoardImage, setUploadedBoardImage] = useState<string | null>(null);

  const [dictPopup, setDictPopup] = useState<{show: boolean, word: string, x: number, y: number, rectTop: number, data: any, isLoading: boolean} | null>(null);
  const [isTeacherBoardOpen, setIsTeacherBoardOpen] = useState(false);
  const [boardWidthVw, setBoardWidthVw] = useState(50);
  const containerRef = useRef<HTMLDivElement>(null);

  const courseProgress = useMemo(() => {
      if (lectures.length === 0) return 0;
      return Math.round((completedLectures.size / lectures.length) * 100);
  }, [lectures, completedLectures]);

  const activeLecture = useMemo(() => {
      return lectures.find(l => l.id === activeLectureId);
  }, [lectures, activeLectureId]);

  const totalPages = pages.length;

  const currentHtmlContent = useMemo(() => { 
      const page = pages.find(p => p.page_number === currentPage); 
      return page ? page.content_html : ''; 
  }, [pages, currentPage]);

  const isIframeOnly = useMemo(() => {
      if (!currentHtmlContent) return false;
      try {
          const doc = new DOMParser().parseFromString(currentHtmlContent, 'text/html');
          const text = doc.body.textContent?.replace(/[\W_]+/g, '').trim();
          const mediaNodes = doc.body.querySelectorAll('iframe, embed, object');
          return (text === '' && mediaNodes.length === 1);
      } catch(e) {
          return false;
      }
  }, [currentHtmlContent]);

  useEffect(() => {
    const handleToggleBoard = (e: any) => {
        setIsTeacherBoardOpen(e.detail === true || e.detail === 'open');
    };
    const handleBoardResize = (e: any) => {
        setBoardWidthVw(e.detail);
    };
    window.addEventListener('tony-teacher-board-state', handleToggleBoard);
    window.addEventListener('tony-board-resize', handleBoardResize);
    return () => {
        window.removeEventListener('tony-teacher-board-state', handleToggleBoard);
        window.removeEventListener('tony-board-resize', handleBoardResize);
    };
  }, []);

  // 🚀 LẮNG NGHE LỆNH MỞ ẢNH ĐỀ BÀI TỪ SIDEBAR BẮN QUA
  useEffect(() => {
      const handleOpenImageBoard = (e: any) => {
          setUploadedBoardImage(e.detail);
          setIsTeacherBoardOpen(true);
      };
      window.addEventListener('tony-open-image-board', handleOpenImageBoard);
      return () => window.removeEventListener('tony-open-image-board', handleOpenImageBoard);
  }, []);

  useEffect(() => {
    if (popupUrl && popupUrl.toLowerCase().includes('.pdf')) {
        sessionStorage.setItem('tony_pdf_mode', 'true');
        window.dispatchEvent(new CustomEvent('tony-pdf-mode-change', { detail: true }));
    } else {
        sessionStorage.removeItem('tony_pdf_mode');
        window.dispatchEvent(new CustomEvent('tony-pdf-mode-change', { detail: false }));
    }
  }, [popupUrl]);

  useEffect(() => {
      if (isTeacherBoardOpen) {
          const interval = setInterval(() => {
              const liveMode = sessionStorage.getItem('tony_live_mode');
              if (!liveMode && !uploadedBoardImage) {
                  setIsTeacherBoardOpen(false); 
              }
          }, 500);
          return () => clearInterval(interval);
      }
  }, [isTeacherBoardOpen, uploadedBoardImage]);

  useEffect(() => {
      if (!currentUser || !activeLectureId || pages.length === 0) return;
      
      const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
      if (safeLectureTasks.length > 0) return; 

      // Chỉ hoàn thành khi ĐÃ XEM HẾT TẤT CẢ CÁC TRANG (cuộn xuống cuối mỗi trang)
      if (viewedPages.size >= pages.length && !completedLectures.has(activeLectureId)) {
          setCompletedLectures(prev => new Set(prev).add(activeLectureId));
          
          supabase.from('lecture_progress')
              .select('id')
              .eq('user_id', currentUser.id)
              .eq('lecture_id', activeLectureId)
              .then(({ data: existingArray }) => {
                  if (existingArray && existingArray.length > 0) {
                      supabase.from('lecture_progress')
                          .update({ completed_tasks: [], is_completed: true })
                          .eq('id', existingArray[0].id)
                          .then();
                  } else {
                      supabase.from('lecture_progress')
                          .insert({ user_id: currentUser.id, lecture_id: activeLectureId, completed_tasks: [], is_completed: true })
                          .then();
                  }
              });
          supabase.from('activity_logs').insert([{
              user_id: currentUser.id,
              action_type: 'finish_lecture',
              details: { lecture_title: activeLecture?.title || "Bài giảng" }
          }]).then();
      }
  }, [viewedPages, pages.length, activeLectureId, currentUser, activeLecture, completedLectures]);

  useEffect(() => {
    if (activeLecture && currentHtmlContent) {
      window.dispatchEvent(new CustomEvent('tony-update-lecture-context', {
        detail: {
          title: activeLecture.title, 
          html: currentHtmlContent 
        }
      }));
    }
  }, [activeLecture, currentHtmlContent]);

  useEffect(() => {
    if (containerRef.current) {
        containerRef.current.scrollTo({ top: 0, behavior: 'smooth' });
        // Nếu trang ngắn không cần cuộn → tự động đánh dấu đã xem
        setTimeout(() => {
            if (containerRef.current && containerRef.current.scrollHeight <= containerRef.current.clientHeight + 100) {
                setViewedPages(prev => {
                    if (prev.has(currentPage)) return prev;
                    const next = new Set(prev);
                    next.add(currentPage);
                    return next;
                });
            }
        }, 500);
    }
  }, [activeLectureId, currentPage]);

  useEffect(() => {
    if (courseId && courseId !== '') {
        fetchCourseData();
    } else { 
        setErrorMessage("Không tìm thấy mã Khóa học."); 
        setIsLoading(false); 
    }
  }, [courseId]);

  useEffect(() => {
    const handleFullscreenChange = () => {
        setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    
    if (window.innerWidth >= 768) {
        setIsSidebarOpen(true);
    }
    
    return () => {
        document.removeEventListener('fullscreenchange', handleFullscreenChange);
    };
  }, []);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
       const dictPop = document.getElementById('dict-popup');
       if (dictPop && !dictPop.contains(e.target as Node)) {
           setDictPopup(null);
       }
       if (taskMenuRef.current && !taskMenuRef.current.contains(e.target as Node)) {
           setIsTaskMenuOpen(false);
       }
    };
    
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const fetchCourseData = async () => {
    setIsLoading(true);
    setErrorMessage(null);
    try {
      const { data: { user } } = await supabase.auth.getUser();
      setCurrentUser(user);

      const [
          { data: courseData, error: courseErr },
          { data: modData },
          { data: lecData }
      ] = await Promise.all([
          supabase.from('courses').select('*').eq('id', courseId).single(),
          supabase.from('lecture_modules').select('*').eq('course_id', courseId).order('order_index'),
          supabase.from('lectures').select('*').eq('course_id', courseId).eq('is_published', true)
      ]);

      if (courseErr || !courseData) {
          throw new Error("Không tìm thấy dữ liệu Khóa học trên hệ thống.");
      }
      
      setCourse(courseData);
      
      const safeModData = modData || [];
      setModules(safeModData);

      let validLectures = (lecData || []).filter(lec => 
          lec.module_id && safeModData.some(mod => mod.id === lec.module_id)
      );

      validLectures.sort((a, b) => {
          const modA = safeModData.find(m => m.id === a.module_id);
          const modB = safeModData.find(m => m.id === b.module_id);
          const modOrderDiff = (modA?.order_index || 0) - (modB?.order_index || 0);
          
          if (modOrderDiff !== 0) {
              return modOrderDiff;
          }
          return (a.order_index || 0) - (b.order_index || 0);
      });

      setLectures(validLectures);

      if (user && validLectures.length > 0) {
         const lectureIds = validLectures.map(l => l.id);
         const { data: allProg } = await supabase.from('lecture_progress')
             .select('lecture_id, completed_tasks, is_completed')
             .eq('user_id', user.id)
             .in('lecture_id', lectureIds);

         const pMap: Record<string, string[]> = {};
         const compSet = new Set<string>();

         if (allProg) { 
             allProg.forEach(p => { 
                 pMap[p.lecture_id] = p.completed_tasks || []; 
                 if (p.is_completed) {
                     compSet.add(p.lecture_id);
                 }
             });
         }
         
         setAllLectureProgress(pMap);
         setCompletedLectures(compSet);
      }

      if (validLectures && validLectures.length > 0) {
         const savedLectureId = localStorage.getItem(`tony_last_lec_${user?.id}_${courseId}`);
         const targetLecture = validLectures.find(l => l.id === savedLectureId) || validLectures[0];
         if (targetLecture.module_id) {
             setExpandedModules([targetLecture.module_id]);
         }
         handleSelectLecture(targetLecture.id, user?.id);
      } else {
         if (safeModData.length > 0) {
             setExpandedModules([safeModData[0].id]);
         }
      }
    } catch (error: any) { 
        setErrorMessage(error.message);
    } finally { 
        setIsLoading(false); 
    }
  };

  const handleSelectLecture = async (lectureId: string, userIdOverride?: string) => {
    try {
        setActiveLectureId(lectureId);
        setCurrentPage(1); 
        setPages([]); 
        setCompletedTasks([]);
        setViewedPages(new Set());
        
        if (window.innerWidth < 768) {
            setIsSidebarOpen(false);
        }
        
        const targetUserId = userIdOverride || currentUser?.id;
        if (targetUserId) {
            localStorage.setItem(`tony_last_lec_${targetUserId}_${courseId}`, lectureId);
        }

        const [
            { data: pageData },
            progressRes
        ] = await Promise.all([
            supabase.from('lecture_pages').select('*').eq('lecture_id', lectureId).order('page_number'),
            targetUserId 
                ? supabase.from('lecture_progress').select('*').eq('lecture_id', lectureId).eq('user_id', targetUserId) 
                : Promise.resolve({ data: null })
        ]);

        const visiblePages = (pageData || [])
            .filter((p: any) => !String(p.content_html || '').startsWith('<!-- hidden -->'))
            .map((p: any, idx: number) => ({
                ...p,
                page_number: idx + 1
            }));
        setPages(visiblePages);
        
        if (targetUserId && progressRes.data && progressRes.data.length > 0) {
           const pData = progressRes.data[0];
           if (pData && Array.isArray(pData.completed_tasks)) {
               setCompletedTasks(pData.completed_tasks);
               setAllLectureProgress(prev => ({
                   ...prev, 
                   [lectureId]: pData.completed_tasks
               }));
           }
           
           if (pData.is_completed) {
               setCompletedLectures(prev => new Set(prev).add(lectureId));
           }
           
        } else if (targetUserId) { 
           setCompletedTasks([]);
           setCompletedLectures(prev => {
               const newSet = new Set(prev);
               newSet.delete(lectureId);
               return newSet;
           });
        }
    } catch (err) {
        console.error(err);
    }
  };

  const toggleModule = (modId: string) => {
      setExpandedModules(prev => 
          prev.includes(modId) ? prev.filter(id => id !== modId) : [...prev, modId]
      );
  };

  const handleToggleTask = useCallback(async (taskId: string) => {
      if (!currentUser || !activeLectureId) {
          return;
      }
      
      const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
      
      setCompletedTasks(prev => {
         const newCompleted = prev.includes(taskId) ? prev.filter(id => id !== taskId) : [...prev, taskId];
         const isCompleted = safeLectureTasks.length > 0 && newCompleted.length === safeLectureTasks.length;
         
         supabase.from('lecture_progress')
             .select('id')
             .eq('user_id', currentUser.id)
             .eq('lecture_id', activeLectureId)
             .then(({ data: existingArray }) => {
                 if (existingArray && existingArray.length > 0) {
                     supabase.from('lecture_progress')
                         .update({ completed_tasks: newCompleted, is_completed: isCompleted })
                         .eq('id', existingArray[0].id)
                         .then();
                 } else {
                     supabase.from('lecture_progress')
                         .insert({ user_id: currentUser.id, lecture_id: activeLectureId, completed_tasks: newCompleted, is_completed: isCompleted })
                         .then();
                 }
             }).catch();

         setAllLectureProgress(allPrev => ({ 
             ...allPrev, 
             [activeLectureId]: newCompleted 
         }));

         if (isCompleted) {
             setCompletedLectures(prevSet => new Set(prevSet).add(activeLectureId));
             supabase.from('activity_logs').insert([{
                 user_id: currentUser.id,
                 action_type: 'finish_lecture',
                 details: { lecture_title: activeLecture?.title || "Bài giảng" }
             }]).then();
         } else {
             setCompletedLectures(prevSet => {
                 const newSet = new Set(prevSet);
                 newSet.delete(activeLectureId);
                 return newSet;
             });
         }
         
         return newCompleted;
      });
  }, [currentUser, activeLectureId, lectures, activeLecture]);

  const handleStartTaskExercise = async (task: any) => {
      if (!onStartTest || !task.test_id) {
          return;
      }
      
      try {
         const { data: testData, error } = await supabase.from('tests').select('*').eq('id', task.test_id).single();

         if (error || !testData) { 
             alert("Bài tập này hiện không khả dụng. Vui lòng liên hệ Admin.");
             return; 
         }
         
         if (!completedTasks.includes(task.id)) {
             handleToggleTask(task.id);
         }
         
         const type = String(testData.test_type || '').toLowerCase();

         if (type.includes('standard')) {
             onStartTest('standard', testData);
         } else if (type.includes('case-study') || type.includes('business')) {
             onStartTest('case-study', testData);
         } else if (type === 'ielts-writing') {
             onStartTest('ielts-writing', testData);
         } else if (type === 'ielts-speaking') {
             onStartTest('ielts-speaking', testData);
         } else if (type.includes('ielts')) {
             onStartTest('computer', testData);
         } else {
             onStartTest('standard', testData);
         }
      } catch (err) {
          console.error(err);
      }
  };

  const handleNextPage = () => {
    if (currentPage < pages.length) {
        setCurrentPage(prev => prev + 1);
    } else {
      const currentIndex = lectures.findIndex(l => l.id === activeLectureId);

      if (currentIndex !== -1 && currentIndex < lectures.length - 1) {
         const nextLecture = lectures[currentIndex + 1];

         if (nextLecture.module_id && !expandedModules.includes(nextLecture.module_id)) {
             setExpandedModules(prev => [...prev, nextLecture.module_id]);
         }
         
         handleSelectLecture(nextLecture.id);
      }
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
        setCurrentPage(prev => prev - 1);
    } else {
       const currentIndex = lectures.findIndex(l => l.id === activeLectureId);

       if (currentIndex > 0) {
          const prevLecture = lectures[currentIndex - 1];

          if (prevLecture.module_id && !expandedModules.includes(prevLecture.module_id)) {
              setExpandedModules(prev => [...prev, prevLecture.module_id]);
          }
          
          handleSelectLecture(prevLecture.id);
       }
    }
  };

  const triggerDictionary = useCallback((word: string, x: number, y: number, rectTop: number) => {
    setDictPopup({ show: true, word, x, y, rectTop, data: null, isLoading: true });
    
    Promise.allSettled([
        fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`)
            .then(r => r.ok ? r.json() : Promise.reject()),
        fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(word)}&langpair=en|vi`)
            .then(r => r.json())
    ]).then(([enRes, viRes]) => {
         let phonetics = '';
         let audio = '';
         let translation = 'Không tìm thấy bản dịch.';
        
         if (enRes.status === 'fulfilled' && enRes.value[0]) {
            phonetics = enRes.value[0].phonetics?.find((p:any) => p.text)?.text || '';
            audio = enRes.value[0].phonetics?.find((p:any) => p.audio)?.audio || '';
         }
        
         if (viRes.status === 'fulfilled' && viRes.value?.responseData?.translatedText) {
            translation = viRes.value.responseData.translatedText;
         }
        
         setDictPopup(prev => prev ? { 
            ...prev, 
            data: { phonetics, audio, translation }, 
            isLoading: false 
         } : null);
    });
  }, []);

  const handleTextSelection = useCallback(() => {
     setTimeout(() => {
        const selection = window.getSelection();
        if (!selection || selection.rangeCount === 0) return;
        
        const text = selection.toString().trim();
        if (!text) return;
        
        if (text.length > 0 && text.length < 40 && text.split(' ').length <= 4) {
           const range = selection.getRangeAt(0);
           const rect = range.getBoundingClientRect();
           triggerDictionary(text, rect.left + (rect.width/2), rect.bottom, rect.top);
        }
     }, 100);
  }, [triggerDictionary]);

  const toggleFullScreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(e => console.log(e));
    } else if (document.exitFullscreen) {
        document.exitFullscreen();
    }
  };

  const getEmbedUrl = (url: string) => {
    if (url.includes('youtube.com/playlist?list=')) {
        return url.replace('playlist?list=', 'embed/videoseries?list=');
    }
    if (url.includes('youtube.com/watch?v=')) {
        return url.replace('watch?v=', 'embed/');
    }
    if (url.includes('youtu.be/')) {
        return url.replace('youtu.be/', 'youtube.com/embed/');
    }
    return url;
  };

  const handleCallTutor = () => {
      const safeHtml = currentHtmlContent ? currentHtmlContent.replace(/<[^>]+>/g, '').slice(0, 2000) : 'Không có dữ liệu văn bản';
      const safeTitle = activeLecture?.title || 'Bài giảng English';
      
      const tutorContext = {
          overall: "N/A",
          transcript: `Học sinh đang học bài: "${safeTitle}". \nNội dung bài học: "${safeHtml}".`,
          feedback: "Bạn là gia sư đang dạy bài giảng này. Hãy chủ động chào học sinh, nhắc tên bài học và hỏi xem học sinh không hiểu phần nào trong nội dung trên để bạn giải thích bằng giọng nói ân cần."
      };
      
      sessionStorage.setItem('tony_live_mode', 'TUTOR');
      sessionStorage.setItem('tony_tutor_data', JSON.stringify(tutorContext));
      
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'live-test' }));
  };

  const safeLectureTasks = Array.isArray(activeLecture?.task_list) ? activeLecture.task_list : [];
  const safeCompletedTasks = Array.isArray(completedTasks) ? completedTasks : [];
  const isLastLectureAndPage = (totalPages === 0 || currentPage === totalPages) && lectures.findIndex(l => l.id === activeLectureId) === lectures.length - 1;

  const isAllTasksDone = safeLectureTasks.length > 0 && safeCompletedTasks.length === safeLectureTasks.length;

  if (isLoading) {
      return (
          <div className="min-h-[100dvh] flex flex-col items-center justify-center bg-slate-50">
              <div className="w-12 h-12 border-4 border-[#0ea5e9]/30 border-t-[#0ea5e9] rounded-full animate-spin"></div>
              <p className="mt-4 text-slate-500 font-medium">Đang tải không gian học...</p>
          </div>
      );
  }
  
  if (errorMessage) {
      return (
          <div className="min-h-[100dvh] flex flex-col items-center justify-center bg-slate-50">
              <div className="text-5xl mb-4 text-red-400">⚠️</div>
              <h2 className="text-xl font-bold text-slate-800 mb-2">Lỗi tải bài giảng</h2>
              <p className="text-slate-500 mb-6">{errorMessage}</p>
              <button 
                  onClick={onBack} 
                  className="bg-[#0ea5e9] text-white px-6 py-2.5 rounded-xl font-semibold shadow-md hover:bg-[#0284c7] transition-all"
              >
                  Quay lại trang chủ
              </button>
          </div>
      );
  }

  return (
    <div className="flex flex-col h-[100dvh] w-full bg-[#f8fafc] font-sans text-slate-800 overflow-hidden relative overscroll-none">
      
      <header className="h-[64px] bg-[#0ea5e9]/95 backdrop-blur-md text-white flex items-center px-4 md:px-6 shrink-0 z-30 shadow-md justify-between border-b border-[#0284c7]/50 transition-all">
         <div className="flex items-center gap-2 md:gap-4 min-w-0 flex-1">
            <button 
                onClick={onBack} 
                className="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 transition-all shrink-0" 
                title="Quay lại"
            >
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" /></svg>
            </button>
            <button 
                onClick={() => setIsSidebarOpen(!isSidebarOpen)} 
                className="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 transition-all shrink-0" 
                title="Danh mục"
            >
               <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M4 6h16M4 12h16M4 18h7" /></svg>
            </button>
            
            <div className="flex flex-col min-w-0 ml-1">
               <h1 className="text-[15px] md:text-[17px] font-semibold leading-tight truncate tracking-tight">{course?.title}</h1>
               <div className="hidden sm:flex items-center gap-2 mt-0.5">
                   <div className="w-24 h-1.5 bg-black/20 rounded-full overflow-hidden">
                       <div className="h-full bg-emerald-400 rounded-full" style={{ width: `${courseProgress}%` }}></div>
                   </div>
                   <span className="text-[10px] font-medium opacity-80">{courseProgress}%</span>
               </div>
            </div>
            
            {safeLectureTasks.length > 0 && (
               <div className="relative ml-2 shrink-0" ref={taskMenuRef}>
                 <button 
                   onClick={() => setIsTaskMenuOpen(!isTaskMenuOpen)} 
                   className={`flex items-center gap-2 px-3 py-1.5 md:py-2 rounded-full text-[13px] font-semibold transition-all border shadow-sm ${isAllTasksDone ? 'bg-emerald-500 text-white border-emerald-400' : 'bg-white/15 hover:bg-white/25 text-white border-white/20'}`}
                 >
                   <span className="text-base">{isAllTasksDone ? '🏆' : '🎯'}</span> 
                   <span className="hidden sm:inline">{isAllTasksDone ? 'Hoàn thành' : 'Nhiệm vụ'}</span>
                   <span className="bg-black/20 px-1.5 py-0.5 rounded-md text-[11px]">{safeCompletedTasks.length}/{safeLectureTasks.length}</span>
                 </button>

                 {isTaskMenuOpen && (
                    <div className="fixed top-[70px] left-1/2 -translate-x-1/2 w-[92vw] max-w-[400px] md:absolute md:top-full md:left-auto md:right-0 md:translate-x-0 md:mt-3 bg-white rounded-2xl shadow-[0_20px_60px_rgba(0,0,0,0.15)] border border-slate-100 overflow-hidden z-[100] animate-in slide-in-from-top-2 duration-200">
                       <div className="bg-slate-50 px-5 py-4 border-b border-slate-100 flex flex-col gap-2">
                          <div className="flex justify-between items-center">
                             <h4 className="font-bold text-slate-800 text-[14px]">Nhiệm vụ bài học</h4>
                             <span className={`font-bold text-[13px] px-2.5 py-1 rounded-full ${isAllTasksDone ? 'bg-emerald-100 text-emerald-700' : 'bg-[#0ea5e9]/10 text-[#0ea5e9]'}`}>
                                 {Math.round((safeCompletedTasks.length / safeLectureTasks.length) * 100)}%
                             </span>
                          </div>
                          <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                              <div className={`h-full transition-all duration-500 ${isAllTasksDone ? 'bg-emerald-500' : 'bg-[#0ea5e9]'}`} style={{ width: `${(safeCompletedTasks.length / safeLectureTasks.length) * 100}%` }}></div>
                          </div>
                       </div>
                       
                       <div className="max-h-[60vh] overflow-y-auto p-3 custom-scrollbar flex flex-col gap-2 bg-slate-50/50">
                          {safeLectureTasks.map((task: any) => {
                             const isCompleted = safeCompletedTasks.includes(task.id);
                             return (
                                <div key={task.id} className={`flex items-start gap-3 p-4 rounded-xl transition-all border ${isCompleted ? 'bg-white border-emerald-200 shadow-sm' : 'bg-white border-slate-200 hover:border-[#0ea5e9]/50 hover:shadow-md'}`}>
                                   <button 
                                       onClick={() => handleToggleTask(task.id)} 
                                       className={`relative flex items-center justify-center shrink-0 w-6 h-6 mt-0.5 rounded-full border-2 transition-all ${isCompleted ? 'bg-emerald-500 border-emerald-500 text-white' : 'bg-slate-50 border-slate-300 hover:border-[#0ea5e9]'}`}
                                   >
                                       {isCompleted && (
                                           <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg>
                                       )}
                                   </button>
                                   <div className="flex-1 min-w-0 flex flex-col items-start gap-2.5">
                                      <span className={`text-[14px] font-medium leading-relaxed transition-colors ${isCompleted ? 'text-slate-500 line-through' : 'text-slate-800'}`}>
                                          {task.text}
                                      </span>
                                      {task.type === 'exercise' && (
                                         <button 
                                           onClick={() => handleStartTaskExercise(task)} 
                                           className={`text-[12px] font-semibold px-4 py-2 rounded-lg transition-all ${isCompleted ? 'bg-slate-100 text-slate-500 hover:bg-slate-200' : 'bg-[#0ea5e9] text-white shadow-sm shadow-blue-500/30 hover:bg-[#0284c7] hover:shadow-md active:scale-95'}`}
                                         >
                                           {isCompleted ? 'Làm lại bài' : 'Bắt đầu làm bài ➜'}
                                         </button>
                                      )}
                                   </div>
                                </div>
                             )
                          })}
                       </div>
                    </div>
                 )}
               </div>
            )}
         </div>

         <div className="flex items-center gap-2 sm:gap-3 shrink-0 ml-2">
             <button
                 onClick={() => {
                     sessionStorage.setItem('portal_selected_course_id', courseId);
                     sessionStorage.setItem('portal_active_view', 'course');
                     sessionStorage.setItem('portal_current_folder_id', '');
                     sessionStorage.setItem('lms_portal_tab', 'library');
                     onBack();
                 }}
                 className="flex items-center gap-2 px-3 py-2 md:px-4 md:h-10 rounded-full text-[13px] md:text-[14px] font-semibold transition-all bg-white/15 hover:bg-white/25 text-white border border-white/20 shadow-sm hover:shadow-md hover:-translate-y-0.5"
                 title="Đi đến kho đề của khóa học"
             >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" /></svg>
                <span className="hidden sm:inline">Kho đề</span>
             </button>
             {!(course?.title || '').toLowerCase().includes('ielts') && (
                 <button 
                     onClick={() => { 
                         if(onOpenAI) {
                             onOpenAI('tutor'); 
                         }
                     }} 
                     className="flex items-center gap-2 px-3 py-2 md:px-4 md:h-10 rounded-full text-[13px] md:text-[14px] font-semibold transition-all bg-gradient-to-r from-amber-400 to-orange-400 hover:from-amber-500 hover:to-orange-500 text-amber-950 shadow-md border border-amber-300/50 hover:shadow-lg hover:-translate-y-0.5"
                 >
                    <span className="animate-bounce">✨</span> <span className="hidden sm:inline">Hỏi AI Tutor</span>
                 </button>
             )}
             {(course?.title || '').toLowerCase().includes('ielts') && (
                 <>
                 <button 
                     onClick={() => onOpenAI?.('ielts', activeLecture?.title, undefined, 'speaking')} 
                     className="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center transition-all bg-gradient-to-br from-pink-400 to-rose-500 text-white shadow-md border border-white/20 hover:shadow-lg hover:scale-105 shrink-0"
                     title="Tutor Speaking"
                 >
                     <span className="text-[10px] md:text-[11px] font-bold leading-tight">Spk</span>
                 </button>
                 <button 
                     onClick={() => onOpenAI?.('ielts', activeLecture?.title, undefined, 'task1')} 
                     className="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center transition-all bg-gradient-to-br from-emerald-400 to-teal-500 text-white shadow-md border border-white/20 hover:shadow-lg hover:scale-105 shrink-0"
                     title="Tutor Writing Task 1"
                 >
                     <span className="text-[10px] md:text-[11px] font-bold leading-tight">WT1</span>
                 </button>
                 <button 
                     onClick={() => onOpenAI?.('ielts', activeLecture?.title, undefined, 'task2')} 
                     className="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center transition-all bg-gradient-to-br from-violet-400 to-purple-500 text-white shadow-md border border-white/20 hover:shadow-lg hover:scale-105 shrink-0"
                     title="Tutor Writing Task 2"
                 >
                     <span className="text-[10px] md:text-[11px] font-bold leading-tight">WT2</span>
                 </button>
                 </>
             )}
             <button 
                 onClick={toggleFullScreen} 
                 className="hidden md:flex w-10 h-10 rounded-full items-center justify-center bg-white/10 hover:bg-white/20 text-white transition-all"
             >
                {isFullscreen ? (
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg>
                ) : (
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>
                )}
             </button>
          </div>
      </header>

      <div className="flex flex-1 overflow-hidden relative w-full">
         
         {isSidebarOpen && (
             <div 
                 className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-40 md:hidden transition-opacity" 
                 onClick={() => setIsSidebarOpen(false)} 
             />
         )}

         <aside className={`fixed md:relative inset-y-0 left-0 z-50 md:z-20 h-[100dvh] md:h-full bg-white border-r border-slate-200 flex flex-col shrink-0 transition-transform duration-300 ease-in-out shadow-[4px_0_24px_rgba(0,0,0,0.05)] md:shadow-none
            ${isSidebarOpen && !isTeacherBoardOpen ? 'translate-x-0 w-[300px] md:w-[340px]' : '-translate-x-full w-[300px] md:w-0 md:opacity-0 md:border-r-0 md:translate-x-0'}`}>
           
           <div className="p-5 border-b border-slate-100 shrink-0 bg-slate-50/50">
              <h3 className="font-bold text-slate-800 text-[16px] mb-3">Nội dung khóa học</h3>
              <div className="flex flex-col gap-1.5">
                  <div className="flex justify-between text-[12px] font-medium text-slate-500">
                      <span>Tiến độ</span>
                      <span className="text-[#0ea5e9]">{completedLectures.size} / {lectures.length} bài</span>
                  </div>
                  <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                      <div className="h-full bg-[#0ea5e9] rounded-full transition-all duration-500" style={{ width: `${courseProgress}%` }}></div>
                  </div>
              </div>
           </div>
           
           <div className="flex-1 overflow-y-auto custom-scrollbar bg-white pb-24" style={{ WebkitOverflowScrolling: 'touch' }}>
             {modules.length === 0 ? (
                <div className="p-8 text-center text-slate-400 text-sm">Chưa có nội dung.</div>
             ) : (
                modules.map((mod, index) => {
                  const moduleLectures = lectures.filter(l => l.module_id === mod.id);
                  const isExpanded = expandedModules.includes(mod.id);
                  
                  return (
                    <div key={mod.id} id={`module-container-${mod.id}`} className="border-b border-slate-100 last:border-0">
                      <button 
                          onClick={(e) => { 
                              e.preventDefault(); 
                              toggleModule(mod.id); 
                              if (!expandedModules.includes(mod.id)) {
                                  setTimeout(() => {
                                      const el = document.getElementById(`module-container-${mod.id}`);
                                      if (el) {
                                          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                                      }
                                  }, 310);
                              }
                          }} 
                          className={`w-full text-left px-5 py-4 transition-colors flex justify-between items-center ${isExpanded ? 'bg-slate-50/50' : 'hover:bg-slate-50'}`}
                      >
                        <div className="flex items-start gap-3">
                            <span className="text-slate-300 font-medium text-sm mt-0.5">
                                {(index+1).toString().padStart(2, '0')}
                            </span>
                            <h4 className="text-[14px] font-semibold text-slate-800 leading-snug">
                                {mod.title}
                            </h4>
                        </div>
                        <span className={`text-[10px] text-slate-400 transition-transform duration-200 shrink-0 ml-2 ${isExpanded ? 'rotate-180' : ''}`}>
                            ▼
                        </span>
                      </button>
                      
                      <div className={`overflow-hidden transition-all duration-300 ease-in-out ${isExpanded ? 'max-h-[2000px] opacity-100' : 'max-h-0 opacity-0'}`}>
                        <div className="pb-3 bg-white flex flex-col gap-0.5 px-2">
                          {moduleLectures.map((lec) => {
                             const isActive = activeLectureId === lec.id;
                             const totalTasks = Array.isArray(lec.task_list) ? lec.task_list.length : 0;
                             const completedCount = allLectureProgress[lec.id]?.length || 0;
                             const isLecCompleted = completedLectures.has(lec.id);

                             return (
                               <button 
                                   key={lec.id} 
                                   onClick={() => handleSelectLecture(lec.id)} 
                                   className={`w-full text-left px-3 py-2.5 rounded-lg text-[13px] transition-all flex items-start gap-3 relative group ${isActive ? 'bg-[#0ea5e9]/10 text-[#0ea5e9]' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'}`}
                               >
                                 <div className="mt-0.5 shrink-0">
                                     {isLecCompleted ? (
                                        <div className="w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-3.5 h-3.5"><path fillRule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clipRule="evenodd" /></svg>
                                        </div>
                                     ) : isActive ? (
                                        <div className="w-5 h-5 rounded-full border-2 border-[#0ea5e9] text-[#0ea5e9] flex items-center justify-center">
                                            <div className="w-2 h-2 rounded-full bg-[#0ea5e9]"></div>
                                        </div>
                                     ) : (
                                        <div className="w-5 h-5 rounded-full border-2 border-slate-300 group-hover:border-[#0ea5e9] transition-colors"></div>
                                     )}
                                 </div>
                                 <div className="flex-1 min-w-0 flex flex-col gap-1">
                                    <span className={`leading-snug ${isActive ? 'font-semibold' : 'font-medium'}`}>
                                        {lec.title}
                                    </span>
                                    {totalTasks > 0 && (
                                       <span className={`text-[10px] w-fit px-1.5 py-0.5 rounded font-medium ${isLecCompleted ? 'bg-emerald-50 text-emerald-600' : 'bg-slate-100 text-slate-500'}`}>
                                           {completedCount}/{totalTasks} bài tập
                                       </span>
                                    )}
                                 </div>
                               </button>
                             )
                          })}
                        </div>
                      </div>
                    </div>
                  )
                })
             )}
           </div>
         </aside>

         <main 
             className={`flex-1 overflow-y-auto bg-slate-50 custom-scrollbar relative lecture-content transition-all duration-500 ease-in-out`} 
             style={isTeacherBoardOpen ? { paddingRight: `${boardWidthVw}vw` } : undefined}
             ref={containerRef} 
             onMouseUp={handleTextSelection}
             onScroll={(e) => {
                 const el = e.currentTarget;
                 // Kiểm tra cuộn đến gần đáy (còn 100px)
                 if (el.scrollHeight - el.scrollTop - el.clientHeight < 100) {
                     setViewedPages(prev => {
                         if (prev.has(currentPage)) return prev;
                         const next = new Set(prev);
                         next.add(currentPage);
                         return next;
                     });
                 }
             }}
         >
             <div className={`min-h-full flex flex-col items-center ${isIframeOnly ? '' : 'py-6 md:py-12 px-0 sm:px-6 lg:px-8'}`}>
                <div className={`w-full flex-none transition-all ${
                    isIframeOnly 
                    ? 'p-0 mb-0 max-w-none' 
                    : `bg-white shadow-sm border border-slate-200 rounded-none sm:rounded-2xl p-5 sm:p-8 md:p-10 mb-8 min-h-[60vh] max-w-[1050px] ${isTeacherBoardOpen ? 'max-w-none' : ''}`
                }`}>
                  {!activeLectureId ? (
                    <div className="flex flex-col items-center justify-center h-full py-20 text-slate-400">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1} stroke="currentColor" className="w-16 h-16 mb-4 opacity-50"><path strokeLinecap="round" strokeLinejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" /></svg>
                        <span className="font-medium text-lg">Chọn bài học ở danh sách bên trái để bắt đầu</span>
                    </div>
                  ) : pages.length === 0 ? (
                    <div className="flex flex-col items-center justify-center h-full py-20 text-slate-400 text-center">
                       <span className="text-4xl mb-3 opacity-50">📖</span>
                       <span className="font-bold text-slate-600">Nội dung bài học hiện đang được cập nhật.</span>
                       <span className="text-sm mt-1">Vui lòng quay lại sau nhé!</span>
                    </div>
                  ) : !currentHtmlContent ? (
                    <div className="flex flex-col items-center justify-center h-full py-20 text-slate-400">
                       <span className="w-8 h-8 border-4 border-[#0ea5e9]/30 border-t-[#0ea5e9] rounded-full animate-spin mb-4"></span>
                       <span className="font-medium">Đang tải nội dung...</span>
                    </div>
                  ) : (
                    <div className="animate-in fade-in duration-500">
                       <h2 className="text-[26px] md:text-[36px] text-slate-900 font-extrabold mb-8 md:mb-12 pb-6 border-b border-slate-100 leading-tight tracking-tight">
                           {activeLecture?.title}
                       </h2>
                       <StaticLectureContent 
                           html={currentHtmlContent} 
                           isIframeOnly={isIframeOnly}
                           onOpenPopup={setPopupUrl} 
                           onOpenDict={triggerDictionary} 
                           onCloseDict={() => setDictPopup(null)} 
                       />
                    </div>
                  )}
               </div>
               
               {activeLectureId && (
                   <div className={`max-w-[1050px] w-full flex justify-between items-center px-4 sm:px-0 pb-16 transition-all ${isTeacherBoardOpen ? 'max-w-none flex-col gap-6 md:flex-row' : ''}`}>
                      <button 
                          onClick={handlePrevPage} 
                          disabled={currentPage === 1 && lectures.findIndex(l => l.id === activeLectureId) === 0} 
                          className="flex items-center gap-2 text-slate-500 font-semibold text-[14px] hover:text-[#0ea5e9] hover:bg-white disabled:opacity-30 transition-all bg-transparent px-5 py-3 rounded-xl disabled:hover:bg-transparent"
                      >
                         <span>←</span> Bài trước
                      </button>
                      
                      {totalPages > 1 && (
                         <div className="flex gap-2 bg-white px-2 py-2 rounded-xl shadow-sm border border-slate-200">
                             {Array.from({ length: totalPages }).map((_, i) => (
                                 <button 
                                     key={i+1} 
                                     onClick={() => setCurrentPage(i+1)} 
                                     className={`w-10 h-10 rounded-lg flex items-center justify-center text-[14px] font-bold transition-all ${currentPage === i+1 ? 'bg-[#0ea5e9] text-white shadow-md' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'}`}
                                 >
                                     {i+1}
                                 </button>
                           ))}
                         </div>
                      )}

                      <button 
                          onClick={handleNextPage} 
                          disabled={isLastLectureAndPage} 
                          className="flex items-center gap-2 text-white font-semibold text-[14px] transition-all bg-[#0ea5e9] hover:bg-[#0284c7] disabled:bg-slate-300 disabled:text-slate-500 disabled:cursor-not-allowed shadow-md shadow-blue-500/20 px-6 py-3 rounded-xl"
                      >
                         {currentPage < pages.length ? 'Trang sau' : 'Bài tiếp theo'} <span>→</span>
                      </button>
                  </div>
               )}
             </div>
         </main>
      </div>

      {dictPopup && dictPopup.show && (
         <div id="dict-popup" className="fixed bg-white rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.15)] ring-1 ring-slate-900/5 w-[90vw] max-w-[340px] flex flex-col overflow-hidden animate-in fade-in zoom-in-95 duration-200"
           style={{ 
             zIndex: 99999, 
             left: Math.max(10, Math.min(dictPopup.x - 170, window.innerWidth - 350)), 
             ...(window.innerHeight - dictPopup.y < 300 ? { bottom: window.innerHeight - dictPopup.rectTop + 15 } : { top: dictPopup.y + 15 }), 
             maxHeight: '400px' 
           }}>
            
            <div className="bg-slate-50/80 backdrop-blur border-b border-slate-100 py-2.5 px-5 flex items-center justify-between shrink-0">
               <div className="flex items-center">
                   <img src="/logo-shield.png" alt="Logo" className="h-4 w-auto object-contain mr-2 opacity-80" />
                   <span className="font-bold text-[11px] text-slate-500 tracking-widest uppercase">Từ điển AI</span>
               </div>
               <button onClick={() => setDictPopup(null)} className="text-slate-400 hover:text-slate-700">✕</button>
            </div>

            <div className="bg-white border-b border-slate-100 p-5 shrink-0 relative">
               <h4 className="text-[20px] font-black text-slate-900 pr-10 leading-tight mb-1">
                   {dictPopup.word}
               </h4>
               {dictPopup.data?.phonetics && (
                   <span className="text-[14px] text-emerald-600 font-mono bg-emerald-50 px-2 py-0.5 rounded">
                       {dictPopup.data.phonetics}
                   </span>
               )}
               {dictPopup.data?.audio && (
                   <button 
                       onClick={() => {
                           if(dictPopup.data.audio) {
                               new Audio(dictPopup.data.audio).play();
                           }
                       }} 
                       className="absolute top-5 right-5 w-10 h-10 rounded-full bg-blue-50 text-[#0ea5e9] flex items-center justify-center hover:bg-[#0ea5e9] hover:text-white transition-colors shadow-sm"
                   >
                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5"><path d="M13.5 4.06c0-1.336-1.616-2.005-2.56-1.06l-4.5 4.5H4.508c-1.141 0-2.318.664-2.66 1.905A9.76 9.76 0 001.5 12c0 .898.121 1.768.35 2.595.341 1.24 1.518 1.905 2.659 1.905h1.93l4.5 4.5c.945.945 2.561.276 2.561-1.06V4.06zM18.584 5.106a.75.75 0 011.06 0c3.808 3.807 3.808 9.98 0 13.788a.75.75 0 11-1.06-1.06 8.25 8.25 0 000-11.668.75.75 0 010-1.06z" /><path d="M15.932 7.757a.75.75 0 011.061 0 4.5 4.5 0 010 6.364.75.75 0 01-1.06-1.06 3 3 0 000-4.244.75.75 0 010-1.06z" /></svg>
                   </button>
               )}
            </div>
            
            <div className="p-5 bg-slate-50 overflow-y-auto custom-scrollbar flex-1 text-[15px]" style={{ WebkitOverflowScrolling: 'touch' }}>
              {dictPopup.isLoading ? (
                 <div className="flex flex-col items-center justify-center py-4 opacity-50">
                     <span className="w-6 h-6 border-2 border-[#0ea5e9] border-t-transparent rounded-full animate-spin mb-2"></span>
                     <span className="text-[13px] font-medium">Đang dịch...</span>
                 </div>
               ) : (
                 <div className="text-slate-700 leading-relaxed font-medium">
                     {dictPopup.data?.translation}
                 </div>
              )}
            </div>
          </div>
      )}

      {/* LỚP PHỦ MEDIA (PDF/YOUTUBE) VÀ ẢNH UPLOAD */}
      {(popupUrl || uploadedBoardImage) && (
        <div className="fixed inset-0 flex flex-col animate-in fade-in duration-200 pointer-events-none" style={{ zIndex: 99998 }}>
          <div 
              className="absolute inset-0 bg-slate-900/95 backdrop-blur-sm pointer-events-auto" 
              onClick={() => {
                  setPopupUrl(null);
                  setUploadedBoardImage(null);
                  window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
                  window.dispatchEvent(new CustomEvent('tony-force-close'));
              }}
          ></div>

          <div 
            className={`w-full h-full relative pointer-events-auto transition-all duration-500 ease-in-out ${isTeacherBoardOpen ? '' : 'w-full'}`}
            style={isTeacherBoardOpen ? { width: `${100 - boardWidthVw}vw` } : undefined}
          >
             
             {/* Render PDF */}
             {popupUrl && popupUrl.toLowerCase().includes('.pdf') && (
                 <PdfVisionViewer 
                    url={popupUrl} 
                    onClose={() => {
                        setPopupUrl(null);
                        window.dispatchEvent(new CustomEvent('tony-force-close'));
                    }} 
                    onCallTutor={handleCallTutor}
                 />
             )}
             
             {/* Render Youtube Video */}
             {popupUrl && !popupUrl.toLowerCase().includes('.pdf') && (
                 <>
                   <div className="absolute top-4 right-4 z-[100000]">
                       <button 
                           onClick={() => {
                               setPopupUrl(null);
                               window.dispatchEvent(new CustomEvent('tony-force-close'));
                           }} 
                           className="w-12 h-12 rounded-full bg-white/10 hover:bg-red-500 flex items-center justify-center text-white transition-colors backdrop-blur-md"
                       >
                           <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                       </button>
                   </div>
                   <div className="absolute inset-0 flex items-center justify-center z-0">
                      <div className="w-8 h-8 border-4 border-white/20 border-t-white rounded-full animate-spin"></div>
                   </div>
                   <iframe 
                       src={getEmbedUrl(popupUrl)} 
                       className="absolute inset-0 w-full h-full border-0 z-10 shadow-2xl" 
                       allowFullScreen
                   ></iframe>
                 </>
             )}

             {/* 🚀 CLASS react-pdf__Document ĐỂ ĐÁNH LỪA BẢNG ĐEN MỞ CÙNG LÚC VỚI ẢNH ĐỀ BÀI MỚI UPLOAD */}
             {uploadedBoardImage && (
                 <div className="react-pdf__Document absolute top-0 left-0 w-full h-full flex flex-col items-center justify-center p-4 md:p-8 z-10 pointer-events-none">
                     <div className="bg-slate-800/80 p-3 rounded-2xl shadow-2xl relative max-h-[90%] max-w-full flex flex-col pointer-events-auto border border-slate-700/50 overflow-hidden">
                         <div className="flex justify-between items-center mb-3 px-2">
                             <span className="text-emerald-400 font-bold text-xs tracking-widest uppercase flex items-center gap-2">
                                 <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shadow-[0_0_8px_#34d399]"></span>
                                 ĐỀ BÀI ĐÍNH KÈM TỪ HỌC SINH
                             </span>
                             <button 
                                 onClick={() => {
                                     setUploadedBoardImage(null);
                                     window.dispatchEvent(new CustomEvent('tony-teacher-board-state', { detail: false }));
                                     window.dispatchEvent(new CustomEvent('tony-force-close'));
                                 }} 
                                 className="text-slate-400 hover:text-white bg-slate-700/50 hover:bg-red-500 rounded-full w-8 h-8 flex items-center justify-center transition-all"
                             >
                                 ✕
                             </button>
                         </div>
                         <img src={uploadedBoardImage} className="max-w-full max-h-full object-contain rounded-xl bg-white/5 min-h-0" />
                     </div>
                 </div>
             )}
             
          </div>
        </div>
      )}
    </div>
  );
}