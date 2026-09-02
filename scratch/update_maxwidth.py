import requests

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
HDRS = {"apikey": KEY, "Authorization": f"Bearer {KEY}"}

# All pages that have images (topics 1.1 - 2.3), both P1 and P2
page_ids = [
    # 1.1
    "90d85cb0-b984-4083-864a-8ead0c4119f7",  # p1
    "c27766f1-0030-4641-8d82-d3771b354e01",  # p2
    # 1.2
    "ce4f09bd-c09b-4cc4-8700-18162e86b316",
    "4dfe49c5-2756-4ee4-8db3-615131e39e0b",
    # 1.3
    "fb591348-a75b-4594-851b-d6b9baafbef4",
    "cf88e936-fa2c-48f2-a9ed-6f81362ba421",
    # 2.1
    "4d3d8e74-308a-45b3-a271-300ca98aa673",
    "47c476d8-285c-41a9-a158-24194cfaf273",
    # 2.2
    "55d26cc1-d2f2-4c0e-ac01-b5390cb4315d",
    "ae8dd7f6-0215-45c3-bb94-f60f373c170f",
    # 2.3
    "5d5f042f-1017-4ca5-ba80-5359f111ac0f",
    "225ae3ec-3ab8-485e-b935-551a8df25bed",
]

total_updated = 0
total_skipped = 0

for pid in page_ids:
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{pid}&select=content_html",
        headers=HDRS
    )
    data = r.json()
    if not data:
        print(f"SKIP {pid}: not found")
        total_skipped += 1
        continue
    html = data[0].get("content_html", "") or ""
    if "max-width: 420px" not in html:
        print(f"SKIP {pid}: no 420px found")
        total_skipped += 1
        continue
    new_html = html.replace("max-width: 420px", "max-width: 660px")
    r2 = requests.patch(
        f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{pid}",
        json={"content_html": new_html},
        headers={**HDRS, "Prefer": "return=minimal", "Content-Type": "application/json"}
    )
    status = "OK" if r2.status_code in (200, 201, 204) else "FAIL"
    print(f"{status} {pid}: HTTP {r2.status_code}")
    if r2.status_code in (200, 201, 204):
        total_updated += 1
    else:
        print(f"  Response: {r2.text[:200]}")

print(f"\nDone: {total_updated} updated, {total_skipped} skipped (already 660px or not found)")
