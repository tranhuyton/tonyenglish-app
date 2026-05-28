import { serve } from "https://deno.land/std@0.168.0/http/server.ts";

serve((req) => {
  if (req.headers.get("upgrade")?.toLowerCase() !== "websocket") {
    return new Response("Chỉ hỗ trợ WebSocket", { status: 400 });
  }

  const { socket: clientWs, response } = Deno.upgradeWebSocket(req);

  clientWs.onopen = () => {
    const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY');
    if (!GEMINI_API_KEY) {
      clientWs.send(JSON.stringify({ error: "LỖI SUPABASE: Chưa nạp GEMINI_API_KEY" }));
      clientWs.close();
      return;
    }

    const HOST = 'generativelanguage.googleapis.com';
    // 🚀 ĐÃ TRẢ VỀ CỔNG v1alpha ĐỂ HỖ TRỢ ĐÚNG LUỒNG LIVE AUDIO
    const URL = `wss://${HOST}/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=${GEMINI_API_KEY}`;
    
    try {
      const geminiWs = new WebSocket(URL);
      let messageQueue: any[] = [];

      geminiWs.onopen = () => {
        while (messageQueue.length > 0) {
          geminiWs.send(messageQueue.shift());
        }
      };

      geminiWs.onmessage = (event) => {
        if (clientWs.readyState === WebSocket.OPEN) {
          clientWs.send(event.data);
        }
      };

      geminiWs.onclose = (e) => {
        if (clientWs.readyState === WebSocket.OPEN) {
          clientWs.send(JSON.stringify({ error: `GOOGLE DẬP MÁY: Mã lỗi ${e.code} - ${e.reason || 'Internal Error'}` }));
          clientWs.close();
        }
      };

      geminiWs.onerror = (e) => {
        if (clientWs.readyState === WebSocket.OPEN) {
          clientWs.send(JSON.stringify({ error: "LỖI CÁP QUANG: Không thể chạm tới Google API" }));
        }
      };

      clientWs.onmessage = (event) => {
        if (geminiWs.readyState === WebSocket.OPEN) {
          geminiWs.send(event.data);
        } else {
          messageQueue.push(event.data);
        }
      };

      clientWs.onclose = () => {
        if (geminiWs.readyState === WebSocket.OPEN) geminiWs.close();
      };

    } catch (err: any) {
      clientWs.send(JSON.stringify({ error: `LỖI MẠNG SUPABASE: ${err.message}` }));
      clientWs.close();
    }
  };

  return response;
});