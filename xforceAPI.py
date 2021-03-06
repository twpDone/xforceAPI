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
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            errorHandle(ex)
    return dico

def get_url_infos(url):
    dico={}
    for arg in ["","/malware"]:
        url=base+"/url"+arg+"/"+url
        print(arg,url)
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            errorHandle(ex)
    return dico

def get_malware_infos(malware):
    dico={}
    for arg in ["","/familyext"]:
        url=base+"/malware"+arg+"/"+malware
        print(arg,url)
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            errorHandle(ex)
            print(ex.message)
    return dico

def get_vulnerabilities_infos(vulnerabilities):
    dico={}
    for arg in ["/fulltext","/search","/msid"]:
        url=base+"/vulnerabilities"+arg+"/"+vulnerabilities
        if arg == "/fulltext":
            url=base+"/vulnerabilities"+arg+"?q="+vulnerabilities
        print(arg,url)
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            errorHandle(ex)
    return dico

def get_dns_infos(dns):
    dico={}
    for arg in ["/resolve"]:
        url=base+arg+"/"+dns
        print(arg,url)
        try:
            dico[arg]=_get_response_json_object(url)
        except Exception as ex:
            errorHandle(ex)
    return dico

### Print Objects 

def printIpHistory(xforceIPElt):
    try:
        print("History for IP :")
        _printSection(xforceIPElt["/history"])
    except Exception as ex:
        errorHandle(ex)

def printIpMalware(xforceIPElt):
    try:
        print("Malware for IP :")
        _printSection(xforceIPElt["/malware"])
    except Exception as ex:
        errorHandle(ex)

def printUrl(xforceUrlElt):
    try:
        print("Url :")
        _printInfo(xforceUrlElt[""])
    except Exception as ex:
        errorHandle(ex)
    try:
        print("Url :")
        _printSection(xforceUrlElt["/malware"])
    except Exception as ex:
        errorHandle(ex)

def printMalware(xforceMalwareElt):
    try:
        print("Malware :")
        _printSection(xforceMalwareElt[""])
    except Exception as ex:
        errorHandle(ex)
    try:
        print("Malware :")
        _printSection(xforceMalwareElt["/familyext"])
    except Exception as ex:
        errorHandle(ex)

def printVulnerabilitiesByName(xforceVulnerabilitiesElt):
    try:
        print("Vulnerabilities :")
        print("\n#Search by name")
        _printSection(xforceVulnerabilitiesElt["/fulltext"])
    except Exception as ex:
        errorHandle(ex)

def printVulnerabilitiesByRef(xforceVulnerabilitiesElt):
    try:
        print("Vulnerabilities :")
        print("\n#Search by ref eg : CVE")
        for sect in (xforceVulnerabilitiesElt["/search"]):
            _printSection(sect)
    except Exception as ex:
        errorHandle(ex)

def printVulnerabilitiesByMsid(xforceVulnerabilitiesElt):
    try:
        print("Vulnerabilities :")
        print("\n#Search by ref Microsoft Bulletin : MSID")
        r_msid=xforceVulnerabilitiesElt["/msid"]
        if type(r_msid)==type("") or type(r_msid)==type(u""):
            _printInfo(r_msid)
        else:
            _printInfo(r_msid)
    except Exception as ex:
        errorHandle(ex)

def printDNS(xforceDNS):
    try:
        print("DNS resolve :")
        _printSection(xforceDNS["/resolve"])
    except Exception as ex:
        errorHandle(ex)

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


### Error Handeling Functions

def errorHandle(exception):
    if type(exception) == KeyError:
        print("This index is empty or dont exists")
    else:
        print(exception,exception.message)
