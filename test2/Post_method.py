#coding:utf-8
import requests
import json
def get_translate_date(word=None):
   url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
   Form_data={
'action':'	FY_BY_CLICKBUTTION','client':'	fanyideskweb','doctype':'json','from':'AUTO',
'i': '我爱中国','keyfrom': 'fanyi.web','salt': '1532659244247','sign': 'dd85bcb1d4b04dfb5582805ed3797f78',
'smartresult':'dict','to':'UTO','typoResult':'false','version':	'2.1'
}
   response=requests.post(url,data=Form_data)
   content=json.loads(response.text)
   print (content['translateResult'][0][0]['tgt'])
if __name__=='_main_':
    get_translate_date('我爱中国')

