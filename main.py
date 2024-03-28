import random
import httpx
import os
import time
import requests

ppkeys = requests.get('https://raw.githubusercontent.com/NiREvil/vless/main/edge/24pbgen/wpbase-keys')
pkeys = ppkeys.content.decode('UTF8')
keys = pkeys.split(',')
gkeys = []

value_int = int(input("\033[1;31;40mPlease enter the number of WARP+ License keys you need to generate by REvil：\n> "))
a = 0

while a < value_int:
  a += 1
    print("<======================================WARP+ Generate======================================>")
    print("Key is being created:", a)
    
  try:
    headers = {
      "CF-Client-Version": "a-6.11-2223",
      "Host": "api.cloudflareclient.com",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip",
      "User-Agent": "okhttp/3.12.1",
    }

    with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223",
                      headers=headers,
                      timeout=30.0) as client:

      r = client.post("/reg")
      id = r.json()["id"]
      license = r.json()["account"]["license"]
      token = r.json()["token"]

      r = client.post("/reg")
      id2 = r.json()["id"]
      token2 = r.json()["token"]

      headers_get = {"Authorization": f"Bearer {token}"}
      headers_get2 = {"Authorization": f"Bearer {token2}"}
      headers_post = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {token}",
      }

      json = {"referrer": f"{id2}"}
      client.patch(f"/reg/{id}", headers=headers_post, json=json)

      client.delete(f"/reg/{id2}", headers=headers_get2)

      key = random.choice(keys)

      json = {"license": f"{key}"}
      client.put(f"/reg/{id}/account", headers=headers_post, json=json)

      json = {"license": f"{license}"}
      client.put(f"/reg/{id}/account", headers=headers_post, json=json)

      r = client.get(f"/reg/{id}/account", headers=headers_get)
      account_type = r.json()["account_type"]
      referral_count = r.json()["referral_count"]
      license = r.json()["license"]

      client.delete(f"/reg/{id}", headers=headers_get)
      gkeys.append(license)
      print(f"License Key: {license}\nData remaining: +{referral_count}GB over 24.59 petabyte")

  except:
    print("Error occurred.")
    time.sleep(15)
  if a % 3 == 0:
    time.sleep(30)

os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;36;40mBelow is the generated key list.")
print("\033[1;34;40mEach key is usable on up to a maximum of five devices.\nplease copy/paste for later use.")
for x in gkeys:
  print(x)

input('\n\n\033[2;35;40many question >>>> t.me/F_NiREvil\npress "Enter" to exit.\n')
