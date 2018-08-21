# -*- coding: UTF-8 -*-
import requests
url="https://www.btime.com/?from=gjl"
strhtml=requests.get(url)
print(strhtml)
