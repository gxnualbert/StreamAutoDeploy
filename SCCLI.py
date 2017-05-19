#-*-coding:utf-8-*-
import json
import subprocess
import sys
import ConfigParser

import pb.fsp_common_pb2 as pb_common

from pb import fsp_smd_pb2 as smd

class DataParse():

    def ParseCPJson(self,filename):
        f = open("./json/"+filename)
        cp=json.load(f)

        cp_conf=smd.CpConf()
        cp_conf.local_ip=cp["local_ip"]
        cp_conf.local_port=cp["local_port"]
        cp_conf.ice_ip=cp["ice_ip"]
        cp_conf.session_app_id=cp["session_app_id"]
        cp_conf.instance_id=cp["instance_id"]
        cp_conf_data=cp_conf.SerializeToString()
        return cp_conf_data
    def ParseGroupASJson(self,filename):
        f=open("./json/"+filename)
        group_as=json.load(f)
        group_as_conf=smd.GroupAsConf()
        group_as_conf.access_addr=group_as["access_addr"]
        group_as_conf.local_addr=group_as["local_addr"]
        group_as_conf.app_id=group_as["app_id"]
        group_as_conf.app_verify_code=group_as["app_verify_code"]
        group_as_conf.ice_server_ip=group_as["ice_server_ip"]
        group_as_conf.ice_server_port=group_as["ice_server_port"]
        group_as_conf.listen_port=group_as["listen_port"]
        group_as_conf.dev_id=group_as["dev_id"]
        group_as_conf.dev_verify_code=group_as["dev_verify_code"]
        group_as_conf.dev_group=group_as["dev_group"]
        group_as_conf_data=group_as_conf.SerializeToString()
        return group_as_conf_data
    def ParseStreamASJson(self,filename):
        f = open("./json/" + filename)
        stream_as=json.load(f)

        stream_as_conf=smd.StreamAsConf()
        stream_as_conf.addr=stream_as["addr"]
        stream_as_conf.port=stream_as["port"]
        stream_as_conf.session_app_id=stream_as["session_app_id"]
        stream_as_conf.url=stream_as["url"]
        stream_as_conf.debug_mode=stream_as["debug_mode"]
        stream_as_conf_data=stream_as_conf.SerializeToString()

        return stream_as_conf_data
    def ParseSSJson(self,filename):
        f = open("./json/" + filename)
        print filename
        ss=json.load(f)
        ss_conf=smd.SsConf()
        ss_conf.port=ss["port"]
        ss_conf.instance_id=ss["instance_id"]
        ss_conf.brokers=ss["brokers"]
        ss_conf_data=ss_conf.SerializeToString()
        return ss_conf_data
    def ParseAccessJson(self,filename):
        f = open("./json/" + filename)
        access = json.load(f)

        access_conf = smd.AccessConf()
        access_conf.proxy = access["proxy"]
        access_conf_data = access_conf.SerializeToString()
        return access_conf_data
    def ParseGCJson(self,filename):
        f = open("./json/" + filename)
        gc=json.load(f)

        gc_conf=smd.GcConf()
        gc_conf.kafka_brokers=gc["kafka_brokers"]
        gc_conf.zookeeper_servers=gc["zookeeper_servers"]
        gc_conf.ice_addr=gc["ice_addr"]
        gc_conf.topic_partitions=gc["topic_partitions"]
        gc_conf.topic_replication=gc["topic_replication"]
        gc_conf.topic_gc_name=gc["topic_gc_name"]
        gc_conf.topic_gc_group_name=gc["topic_gc_group_name"]
        gc_conf.topic_sc_group_name=gc["topic_sc_group_name"]
        gc_conf.instance_id=gc["instance_id"]
        gc_conf.addr=gc["addr"]
        gc_conf.port=gc["port"]
        gc_conf.protocol_version=gc["protocol_version"]

        gc_conf_data=gc_conf.SerializeToString()
        return gc_conf_data
    def ParseGSJson(self,filename):
        f = open("./json/" + filename)
        gs=json.load(f)

        # iplist=smd.IpList()
        # iplist.ip.extend(gs["nat_ip_list"])

        gs_conf=smd.GsConf()
        # gs_conf.nat_ip_list.add()

        gs_conf.log_save_days=gs["log_save_days"]
        gs_conf.ice_server_addr=gs["ice_server_addr"]
        gs_conf.ice_server_port=gs["ice_server_port"]
        gs_conf.process_name=gs["process_name"]
        gs_conf.tcp_addr=gs["tcp_addr"]
        gs_conf.tcp_port=gs["tcp_port"]
        gs_conf.udp_addr=gs["udp_addr"]
        gs_conf.udp_port=gs["udp_port"]
        gs_conf.guid=gs["guid"]
        gs_conf.service_name=gs["service_name"]
        gs_conf.priority=gs["priority"]
        gs_conf.session_app_id=gs["session_app_id"]
        gs_conf.debug_mode=gs["debug_mode"]
        gs_conf.instance_id=gs["instance_id"]
        gs_conf.brokers=gs["brokers"]
        gs_conf.group_id=gs["group_id"]
        gs_conf.sc_topic=gs["sc_topic"]
        gs_conf.gc_topic=gs["gc_topic"]
        gs_conf.sys_log_interval=gs["sys_log_interval"]

        gs_conf_data=gs_conf.SerializeToString()

        return gs_conf_data
    def ParseICEJson(self,filename):
        f = open("./json/" + filename)
        ice = json.load(f)

        ice_conf=smd.IceConf()
        ice_conf.redis_addr=ice["redis_addr"]

        ice_conf_data=ice_conf.SerializeToString()

        return ice_conf_data
    def ParseSCJson(self,filename):

        f = open("./json/" + filename)
        sc = json.load(f)

        sc_conf=smd.ScConf()
        sc_conf.kafka_brokers=sc["kafka_brokers"]
        sc_conf.zookeeper_servers=sc["zookeeper_servers"]
        sc_conf.ice_addr=sc["ice_addr"]
        sc_conf.topic_partitions=sc["topic_partitions"]
        sc_conf.topic_replication=sc["topic_replication"]
        sc_conf.topic_sc_name=sc["topic_sc_name"]
        sc_conf.topic_sc_group_name=sc["topic_sc_group_name"]
        sc_conf.consumer_client_id=sc["consumer_client_id"]
        sc_conf.protocol_version=sc["protocol_version"]

        sc_conf_data=sc_conf.SerializeToString()

        return sc_conf_data
    def ParseSPJson(self,filename):
        f = open("./json/" + filename)
        sp = json.load(f)

        sp_conf=smd.SpConf()
        sp_conf.kafka_brokers=sp["kafka_brokers"]
        sp_conf.zookeeper_servers=sp["zookeeper_servers"]
        sp_conf.ice_addr=sp["ice_addr"]
        sp_conf.topic_partitions=sp["topic_partitions"]
        sp_conf.topic_replication=sp["topic_replication"]
        sp_conf.topic_sp_name=sp["topic_sp_name"]
        sp_conf.topic_sp_group_name=sp["topic_sp_group_name"]
        sp_conf.topic_sc_group_name=sp["topic_sc_group_name"]
        sp_conf.instance_id=sp["instance_id"]
        sp_conf.addr=sp["addr"]
        sp_conf.port=sp["port"]
        sp_conf.protocol_version=sp["protocol_version"]

        sp_conf_data=sp_conf.SerializeToString()
        return sp_conf_data
    def ServiceConfData(self,name,down_url,conf_data,smdname=None):
        service_conf=smd.ServiceConf()

        service_conf.name=name
        service_conf.download_url=down_url
        service_conf.config=conf_data
        if smdname:
            service_conf.smd_name="smdname"
        serial_data=service_conf.SerializeToString()
        return serial_data
    def SendData(self,data,url):
        p = subprocess.Popen("curl -v --data \'" + service_data + "\' " + url, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout = p.stdout.read()
        return stdout
    def ParseRsp(self,rsp_data):
        rsp=smd.ServiceConfRsp()
        rsp.ParseFromString(rsp_data)
        print "服务名称是：",rsp.service_name
        print "服务部署在：",rsp.service_dest_addr
        CommonResponse_obj = pb_common.CommonResponse()
        CommonResponse_obj = rsp.response
        print "响应码是：",CommonResponse_obj.response_code
        print "响应消息是：",CommonResponse_obj.response_msg
        print "\t"
    def IniConfFile(self):
        iniFileUrl = "./json/conf.ini"
        conf = ConfigParser.ConfigParser()  # 生成conf对象
        conf.read(iniFileUrl)
        return conf
    def GetConfSections(self):
        conf=self.IniConfFile()
        sections = conf.sections()
        return sections
    def GetConfOption(self,option):
        conf = self.IniConfFile()
        keylist=conf.options(option)
        return keylist
    def GetConfSectionKeyValue(self,myoption):
        conf = self.IniConfFile()
        key_value_list=conf.items(myoption)
        return key_value_list
    def GetValueOfOption(self,myoption,key):
        conf = self.IniConfFile()
        value=conf.get(myoption,key)
        return value

    def ConfigService(self,servicename,sectionname,download_url):
        jsonfile=self.GetValueOfOption(sectionname,"json_file_name")
        servic_ename=self.GetValueOfOption(sectionname,"service_name")
        service_keys=self.GetConfOption(sectionname)
        if servicename=='cp':
            conf=self.ParseCPJson(jsonfile)
        elif servicename=='gc':
            conf = self.ParseGCJson(jsonfile)
        elif servicename=='access':
            conf=self.ParseAccessJson(jsonfile)
        elif servicename=='group_as':
            conf=self.ParseGroupASJson(jsonfile)
        elif servicename=='gs':
            conf=self.ParseGSJson(jsonfile)
        elif servicename=='ice':
            conf=self.ParseICEJson(jsonfile)
        elif servicename=='sc':
            conf=self.ParseSCJson(jsonfile)
        elif servicename=='sp':
            conf=self.ParseSPJson(jsonfile)
        elif servicename=='ss':
            conf=self.ParseSSJson(jsonfile)
        elif servicename=='stream_as':
            conf=self.ParseStreamASJson(jsonfile)
        else:
            print "wrong service name was using!!!!!!"

        if "smd_name" in service_keys:
            smd_name=self.GetValueOfOption(sectionname,"smd_name")
            print smd_name
            service_data=self.ServiceConfData(servic_ename,download_url,conf,smdname=smd_name)
        else:
            service_data = self.ServiceConfData(servic_ename, download_url, conf)
        return service_data



    def PostDataToServer(self,service_data,request_url):
        stdout = self.SendData(service_data, request_url)
        scc.ParseRsp(stdout)


if __name__=="__main__":
    # request_url=sys.argv[1]
    # json_file_name=sys.argv[2]
    # service_name=sys.argv[3]
    # download_url=sys.argv[4]
    #
    # rsp = smd.ServiceConfRsp()
    # a = DataParse()
    # conf=a.ParseCPJson(json_file_name)
    # service_data = a.ServiceData(service_name,download_url,conf)

    scc = DataParse()

    request_url=scc.GetValueOfOption("common","request_url")
    download_url=scc.GetValueOfOption("common","download_url")
    sectionKeyList=scc.GetConfSections()
    print sectionKeyList
    # ['access', 'cp', 'gc', 'group_as', 'gs', 'ice', 'sc', 'sp', 'ss', 'stream_as', 'common']

    # for i in range(len(sectionKeyList)):
    #     if 'access' in sectionKeyList[i]:
    #         service_data = scc.ConfigService('access', sectionKeyList[i], download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'cp' in sectionKeyList[i]:
    #         service_data=scc.ConfigService('cp',sectionKeyList[i],download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'gc' in sectionKeyList[i]:
    #         service_data=scc.ConfigService('gc',sectionKeyList[i],download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'gs' in sectionKeyList[i]:
    #         service_data = scc.ConfigService('gs', sectionKeyList[i], download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'ice' in sectionKeyList[i]:
    #         service_data = scc.ConfigService('ice', sectionKeyList[i], download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'sc' in sectionKeyList[i]:
    #         service_data = scc.ConfigService('sc', sectionKeyList[i], download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'sp' in sectionKeyList[i]:
    #         service_data = scc.ConfigService('sp', sectionKeyList[i], download_url)
    #         scc.PostDataToServer(service_data, request_url)
    #     if 'ss' in sectionKeyList[i] and len(sectionKeyList[i])==2:
    #         service_data = scc.ConfigService('ss', sectionKeyList[i], download_url)
    #         scc.PostDataToServer(service_data, request_url)
        # if 'stream_as' in sectionKeyList[i]:
        #     service_data = scc.ConfigService('stream_as', sectionKeyList[i], download_url)
        #     scc.PostDataToServer(service_data, request_url)

    service_data = scc.ConfigService('ice', 'ice', download_url)
    scc.PostDataToServer(service_data, request_url)








