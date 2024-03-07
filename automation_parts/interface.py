import urllib.request
import urllib.request
import urllib.error

try:
    with urllib.request.urlopen('http://10.117.27.38:8090/') as f:
        print(f.read())
        print(f.status)
        print(f.getheader("content-length"))
except urllib.error.URLError as e:
    print(e.reason)