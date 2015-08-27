#!/usr/bin/python

import xforceAPI

def dictAdd(dicDst,dicSrc):
    for key in dicSrc:
        dicDst[key]=dicSrc[key]

dictRes={}
print "Search : "
searching=str(raw_input(""))

dictAdd(dictRes,xforceAPI.get_dns_infos(searching))
dictAdd(dictRes,xforceAPI.get_ip_infos(searching))
dictAdd(dictRes,xforceAPI.get_malware_infos(searching))
dictAdd(dictRes,xforceAPI.get_url_infos(searching))
dictAdd(dictRes,xforceAPI.get_vulnerabilities_infos(searching))


xforceAPI.printIpHistory(dictRes)
xforceAPI.printIpMalware(dictRes)
xforceAPI.printDNS(dictRes)
xforceAPI.printMalware(dictRes)
xforceAPI.printUrl(dictRes)
xforceAPI.printVulnerabilitiesByRef(dictRes)
xforceAPI.printVulnerabilitiesByName(dictRes)
xforceAPI.printVulnerabilitiesByMsid(dictRes)
