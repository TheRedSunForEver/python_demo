import requests

# response = requests.get('http://www.baidu.com')
# response.encoding = "utf-8"
# print(response.text)

# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
# resp = requests.get("http://www.baidu.com", headers=headers)
# print(resp.content.decode())

# resp = requests.get("https://www.x.org:8443/test", verify=False)
# print(resp.content.decode())

# 失败
resp = requests.get("https://www.x.org:8443/test", verify="/Users/hongyangxiao/xtemp/back/simpleval.cer")
print(resp.content.decode())
