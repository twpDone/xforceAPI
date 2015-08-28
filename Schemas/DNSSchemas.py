#!/usr/bin/python


class DNSRecord(dict):
    """
        Object to represent a DNS Record for xforce json API.
    """
    def __init__(self,value="",valueType="",recordType="",last="",first="",jsonDict=None):
        """
            You can provide the following attributes :
                @var value string
                @var valueType string
                @var recordType string
                @var last string
                @var first string

            or a dict object wich will become the DNSRecord object itself.
                @var jsonDict dict
        __________________________

        """
        if not jsonDict:
            # strings
            self["value"]= value
            self["type"]= valueType
            self["recordType"]= recordType
            self["last"]= last
            self["first"]= first
        else:
            # dict
            self=jsonDict

    def __str__(self):
        retStr=""
        for key in self:
            retStr+=key+": "+str(self[key])+"\n"
        return retStr

class DNSMX(dict):
    """
        Object to represent a DNS MX entity for xforce json API.
    """
    def __init__(self,exchange="",priority=0,jsonDict=None):
        """
            
            You can provide the following attributes :
                @var exchange str
                @var priority int 

            or a dict object wich will become the DNSMX object itself.
                @var jsonDict dict
        __________________________

        """
        if not jsonDict:
            # str
            self["exchange"]= exchange
            # int
            self["priority"]= priority
        else:
            # dict
            self=jsonDict

    def __str__(self):
        retStr=""
        for key in self:
            retStr+=key+": "+str(self[key])+"\n"
        return retStr

class DNSPassive(dict):
    """
        Object to represent a DNS Passive entity for xforce json API.
    """
    def __init__(self,query="",records=[DNSRecord()],jsonDict=None):
        """
            You can provide the following attributes :
                @var query str
                @var records list (of DNSRecord objects) 

            or a dict object wich will become the DNSPassive object itself.
                @var jsonDict dict
        __________________________

        """
        if not jsonDict:
            # Str
            self["query"]= query
            # list of DNSRecord Objects
            self["records"]= records
        else:
            # dict
            self=jsonDict

    def __str__(self):
        retStr="\nQuery : "+str(self["query"])+"\n"
        retStr+=self.printdnsRecords()
        return retStr

    def printdnsRecords(self):
        retStr=""
        for dnsRecord in self["records"]:
            retStr+=str(dnsRecord)+"\n"
        return retStr

class DNSObj(dict):
    """
        Object to represent a DNS Passive entity for xforce json API.
    """
    def __init__(self,A=[""],AAAA=[""],MXObjList=[DNSMX()],TXT=[""],RDNS=[""],Passive=DNSPassive(),jsonDict=None):
        """
            You can provide the following attributes :
                @var A str
                @var AAAA str
                @var MXObjList list (of DNSMX objects) 
                @var TXT str
                @var RDNS str
                @var Passive DNSPassive object 

            or a dict object wich will become the DNSPassive object itself.
                @var jsonDict dict
        __________________________

        """
        if not jsonDict:
            # Str lists
            self["A"]=A
            self["AAAA"]=AAAA
            self["TXT"]=TXT
            self["RDNS"]=RDNS
            # DNSMX Object List
            self["MX"]=MXObjList
            # DNSPassive Object
            self["Passive"]=Passive 

        else:
            # dict
            self=jsonDict

    def __str__(self):
        retStr="\n"
        retStr+=self.printARecords()
        retStr+=self.printAAAARecords()
        retStr+=self.printTXTRecords()
        retStr+=self.printRDNSRecords()
        retStr+=self.printMXRecords()
        retStr+=self.printPassiveRecords()
        return retStr
        
    def printARecords(self): 
        retStr=""
        for ARecord in self["A"]:
            retStr+="A: "+str(ARecord)+"\n"
        return retStr

    def printAAAARecords(self): 
        retStr=""
        for AAAARecord in self["AAAA"]:
            retStr+="AAAA: "+str(AAAARecord)+"\n"
        return retStr

    def printTXTRecords(self): 
        retStr=""
        for TXTRecord in self["TXT"]:
            retStr+="TXT: "+str(TXTRecord)+"\n"
        return retStr

    def printRDNSRecords(self): 
        retStr=""
        for RDNSRecord in self["RDNS"]:
            retStr+="RDNS: "+str(RDNSRecord)+"\n"
        return retStr

    def printMXRecords(self): 
        retStr=""
        for MXRecord in self["MX"]:
            retStr+="MX: "+str(MXRecord)+"\n"
        return retStr

    def printPassiveRecords(self): 
        retStr=""
        for PassiveRecord in self["Passive"]:
            retStr+="Passive: "+str(PassiveRecord)+"\n"
        return retStr

