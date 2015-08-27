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

def get_url_infos(url):
    dico={}
    for arg in ["","/malware"]:
        url=base+"/url"+arg+"/"+url
        print(arg,url)
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            print(ex.message)
    return dico

def get_malware_infos(malware):
    dico={}
    for arg in ["","/familyext"]:
        url=base+"/malware"+arg+"/"+malware
        print(arg,url)
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            print(ex.message)
    return dico

def get_dns_infos(dns):
    dico={}
    for arg in ["/resolve"]:
        url=base+arg+"/"+dns
        print(arg,url)
        dico[arg]=_get_response_json_object(url)
    return dico

### Print Objects 

def printIpHistory(xforceIPElt):
    print("History for IP :")
    _printSection(xforceIPElt["/history"])

def printIpMalware(xforceIPElt):
    print("Malware for IP :")
    _printSection(xforceIPElt["/malware"])

def printUrl(xforceUrlElt):
    print("Url :")
    try:
        _printInfo(xforceUrlElt[""])
    except Exception as ex:
        print(ex.message)
    try:
        _printSection(xforceUrlElt["/malware"])
    except Exception as ex:
        print(ex.message)

def printMalware(xforceMalwareElt):
    print("Malware :")
    try:
        _printSection(xforceMalwareElt[""])
    except Exception as ex:
        print(ex.message)
    try:
        _printSection(xforceMalwareElt["/familyext"])
    except Exception as ex:
        print(ex.message)

def printDNS(xforceDNS):
    print("DNS resolve :")
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


