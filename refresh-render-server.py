import urllib.request
import time
import urllib.request



while(True):
  webUrl=urllib.request.urlopen('https://www.python.org/')
  print("result: "+str(webUrl.getcode()))
  time.sleep(900)


