#!/usr/bin/python

import urllib2
import json

def get_auth_token():
    '''
    get an auth token
    '''
    req=urllib2.Request("https://xforce-api.mybluemix.net/auth/anonymousToken")
    response=urllib2.urlopen(req)
    html=response.read()
    json_obj=json.loads(html)
    token_string=json_obj["token"].encode("ascii","ignore")
    return token_string

def get_response_json_object(url, auth_token):
    '''
    returns json object with info
    '''
    auth_token=get_auth_token()
    req=urllib2.Request(url, None, {"Authorization": "Bearer %s" %auth_token})
    response=urllib2.urlopen(req)
    html=response.read()
    json_obj=json.loads(html)
    return json_obj

base="https://xforce-api.mybluemix.net"

def get_ip_infos(ip):
    dict={}
    for arg in ["/history","/malware"]:
        url=base+"/ipr"+arg+"/"+ip
        print(arg,url)
        dict[arg]=get_response_json_object(url, get_auth_token)
    return dict


def printHistory(xforceIPElt):
    print("History for")
    _printSection(xforceIPElt["/history"])



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
    print("________")
    for key in xforceInfo:
        subItem=xforceInfo[key]
        if type(subItem)==type({}):
            if len(subItem) > 0 :
                for subkey in  subItem:
                    print(subkey+": "+str(subItem[subkey]))
        else:
            print(key+": "+str(subItem))

