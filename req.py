import requests
http_proxy = "http://c.shobhit:robosho14@202.141.80.19:3128"
https_proxy = "https://c.shobhit:robosho14@202.141.80.19:3128"
ftp_proxy = "ftp://c.shobhit:robosho14@202.141.80.19:3128"

proxyDict = {
"http" : http_proxy,
"https" : https_proxy,
"ftp" : ftp_proxy
}

r= requests.post('http://172.16.26.78:8001/desk2/', proxies=proxyDict)
print r.text