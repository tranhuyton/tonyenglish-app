const url = process.env.VITE_SUPABASE_URL + "/rest/v1/tests?select=id,content_json-%3EbasicInfo-%3Ecategory&limit=1";
fetch(url, {
  headers: {
    'apikey': process.env.VITE_SUPABASE_ANON_KEY,
    'Authorization': 'Bearer ' + process.env.VITE_SUPABASE_ANON_KEY
  }
}).then(res => res.json()).then(data => console.log(JSON.stringify(data, null, 2))).catch(err => console.error(err));
