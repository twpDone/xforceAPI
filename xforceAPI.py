#!/usr/bin/python

import urllib2
import json

### Functions and definitions needed to use the API

base="https://xforce-api.mybluemix.net"

def _get_auth_token():
    '''
    get an auth token
    '''
    req=urllib2.Request("https://xforce-api.mybluemix.net/auth/anonymousToken")
    response=urllib2.urlopen(req)
    html=response.read()
    json_obj=json.loads(html)
    token_string=json_obj["token"].encode("ascii","ignore")
    return token_string

def _get_response_json_object(url):
    '''
    returns json object with info
    '''
    auth_token=_get_auth_token()
    req=urllib2.Request(url, None, {"Authorization": "Bearer %s" %auth_token})
    response=urllib2.urlopen(req)
    html=response.read()
    json_obj=json.loads(html)
    return json_obj

### Get results from API

def get_ip_infos(ip):
    dico={}
    for arg in ["/history","/malware"]:
        url=base+"/ipr"+arg+"/"+ip
        print(arg,url)
        dico[arg]=_get_response_json_object(url)
    return dico

def get_dns_infos(dns):
    dico={}
    for arg in ["/resolve"]:
        url=base+arg+"/"+dns
        print(arg,url)
        dico[arg]=_get_response_json_object(url)
    return dico

### Print Objects 

def printHistory(xforceIPElt):
    print("History for")
    _printSection(xforceIPElt["/history"])

def printMalware(xforceIPElt):
    print("Malware for")
    _printSection(xforceIPElt["/malware"])

def printDNS(xforceDNS):
    print("DNS for")
    _printSection(xforceDNS["/resolve"])

### Utility functions to display received objects in shell

def _printSection(xforceSection):
    for key in xforceSection:
        xforceCategorie=xforceSection[key]
        if type(xforceCategorie)==type("") or type(xforceCategorie)==type(u""):
            print(key+": "+xforceCategorie)
        elif type(xforceCategorie)==type([]):
            if len(xforceCategorie) > 0 :
                print(key+"----")
                for info in xforceCategorie:
                    _printInfo(info)
                print("")

def _printInfo(xforceInfo):
    #parcours dictionaire
    if type(xforceInfo)==type("") or type(xforceInfo)==type(u""):
        print(xforceInfo)
    elif type(xforceInfo)==type([]):
        print("________")
        for elt in xforceInfo:
            _printInfo(elt)
    else:
        print("________")
        for key in xforceInfo:
            subItem=xforceInfo[key]
            if type(subItem)==type({}):
                if len(subItem) > 0 :
                    for subkey in  subItem:
                        print(subkey+": "+str(subItem[subkey]))
            else:
                print(key+": "+str(subItem))


