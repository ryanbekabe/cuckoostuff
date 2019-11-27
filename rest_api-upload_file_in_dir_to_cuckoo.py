#Ryan Bekabe - bekabeipa@gmail.com - hanyajasa.com
import requests, json, os
arr = os.listdir("./exedir")
REST_URL = "http://IP_Cuckoo_server:PORT_Rest_API/tasks/create/file"
HEADERS = {"Authorization": "Bearer S4MPL3"}
i=0
for filenya in arr:
   print i, ' - >', str(filenya)
   i=i+1
   SAMPLE_FILE = str(filenya)
   with open(str('./exedir/') + SAMPLE_FILE, "rb") as sample:
      files = {"file": (SAMPLE_FILE, sample)}
      r = requests.post(REST_URL, headers=HEADERS, files=files)
      #os.remove(str('./exedir/') + SAMPLE_FILE)
      task_id = r.json()["task_id"]
      print i, ' - >', str(filenya), ' | Task ID = ', task_id
