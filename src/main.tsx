import 'drag-drop-touch';
import 'katex/dist/katex.min.css';
import React from 'react';
import ReactDOM from 'react-dom';
import './tailwind.css';
import App from './App';

import { initChunkErrorListener } from './chunkReload';

// 🚀 Khởi tạo lắng nghe lỗi nạp chunk tự động reload trang khi cập nhật phiên bản mới
initChunkErrorListener();

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
