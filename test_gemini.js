const GEMINI_API_KEY = "AIzaSyAwTqP7jueSQ_vvys6wB20lIManuCXebIM";
async function test() {
  const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      contents: [{ parts: [{ text: "Hello" }] }],
      generationConfig: {
        temperature: 0.7,
        responseMimeType: "application/json"
      }
    })
  });
  const text = await res.text();
  console.log(res.status, text);
}
test();
