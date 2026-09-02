import json
import urllib.request

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

def upload(page_id, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    url = f"https://ubkvzgwespfvrlpjuxkp.supabase.co/rest/v1/lecture_pages?id=eq.{page_id}"
    headers = {
        "apikey": API_KEY,
        "Authorization": f"Bearer " + API_KEY,
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    data = json.dumps({"content_html": html}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Uploaded {page_id} from {filename} - HTTP {response.status}")
    except Exception as e:
        print(f"Failed {page_id}: {e}")

if __name__ == '__main__':
    upload("684fe808-3289-4fbc-86d3-7a3269b1dd69", "scratch/91_p1.html")
    upload("6af4feb9-020d-4e0c-a5f6-6ba1efac260a", "scratch/91_p2.html")
    upload("5959ac13-2cd3-4ad7-8ed6-065e124e3956", "scratch/92_p1.html")
    upload("da2cfee9-f56c-4b4f-9ff5-f7d5dfecf491", "scratch/92_p2.html")
    upload("b01642e1-f7a3-472a-ad61-141c49f96057", "scratch/93_p1.html")
    upload("eb51c2af-fbd1-4e0e-8332-93e89631c669", "scratch/93_p2.html")
