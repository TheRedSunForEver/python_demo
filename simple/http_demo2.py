import http.client
import ssl

context = ssl.create_default_context(cafile="/Users/xtemp/back/ssl/server.crt")
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
conn = http.client.HTTPSConnection("www.x.org", context=context, port=8080)
conn.request("GET", "/test")
resp = conn.getresponse()
print(resp.read().decode("utf-8"))



