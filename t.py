# -*- coding:utf-8 -*-
import requests

url = "http://liyubao.dev.zzcrowd.com/stream-edit-submit/10707"

payload = "{\"skip\":false,\"results\":{\"results_type\":\"ok\",\"results_reason\":\"\",\"results_value\":[{\"entities\":[{\"type\":\"FaceBeautyPK\",\"value\":{\"images\":[\"8a640d82bb20be3cd3f820c899014031222be635\",\"01029ea743102b07d58a976f5407d260e5a27eb3\"],\"winner\":0,\"editor_name\":\"r\"}}]}]}}\r\n"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "95574eba-c819-4627-7546-d7ec8ac350b8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

