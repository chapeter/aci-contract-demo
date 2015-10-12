#!/usr/bin/env python
import requests
import json

apicip = ""
apicuser = ""
apicpass = ""

url = "http://" + apicip + "/api/mo/uni/tn-chapeter/ap-icmp_test/epg-t1.json"
deletedata = {"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"ICMP", "status":"deleted"}}}
logindata = {
  "aaaUser" : {
    "attributes" : {
        "name" : apicuser,
        "pwd" : apicpassword
    }
  }
}
deleteurl = "http://" + apicip + "/api/mo/uni/tn-chapeter/ap-icmp_test/epg-t1.json"
loginurl = "http://" + apicip + /api/aaaLogin.json"
myheaders = {'content-type':'application/json'}
loginresponse = requests.post(loginurl, data=json.dumps(logindata), headers=myheaders).json()

token = loginresponse['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-Cookie'] = token

dataresponse = requests.post(deleteurl, data=json.dumps(deletedata), headers=myheaders, cookies=cookies)

if dataresponse.ok == True:
  print("Contract Deleted from t1")
