#-*-coding:utf-8-*-
import json
import fsp_common_pb2 as pb_common
import fsp_smd_pb2 as smd
import os,subprocess


class DataParse():

    def ParseCPJson(self,filename):
        f = open(filename)
        cp=json.load(f)

        cp_conf=smd.CpConf()
        cp_conf.local_ip=cp["local_ip"]
        cp_conf.local_port=cp["local_port"]
        cp_conf.ice_ip=cp["ice_ip"]
        cp_conf.session_app_id=cp["session_app_id"]
        cp_conf.instance_id=cp["instance_id"]
        cp_conf_data=cp_conf.SerializeToString()
        return cp_conf_data

    def ParseGroupASJson(self):
        f=open("group_as.json")
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

    def ParseStreamASJson(self):
        f=open("stream_as.json")
        stream_as=json.load(f)

        stream_as_conf=smd.StreamAsConf()
        stream_as_conf.addr=stream_as["addr"]
        stream_as_conf.port=stream_as["port"]
        stream_as_conf.session_app_id=stream_as["session_app_id"]
        stream_as_conf.url=stream_as["url"]
        stream_as_conf.debug_mode=stream_as["debug_mode"]
        stream_as_conf_data=stream_as_conf.SerializeToString()

        return stream_as_conf_data

    def ParseSSJson(self):
        f=open("ss.json")
        ss=json.load(f)

        ss_conf=smd.SsConf()
        ss_conf.port=ss["port"]
        ss_conf.instance_id=ss["instance_id"]
        ss_conf.brokers=ss["brokers"]
        ss_conf_data=ss_conf.SerializeToString()

        return ss_conf_data




    def ServiceData(self,name,down_url,conf_data):
        service_conf=smd.ServiceConf()
        service_conf.name=name
        service_conf.download_url=down_url
        service_conf.config=conf_data
        serial_data=service_conf.SerializeToString()
        return serial_data


    def SendData(self,data,url):
        os.system("curl -v --data \'"+data+"\' "+url)

    def ParseRsp(self,rsp_data):

        # import pdb
        # pdb.set_trace()
        rsp=smd.ServiceConfRsp()
        rsp.ParseFromString(rsp_data)
        print rsp.service_name
        print rsp.service_dest_addr
        CommonResponse_obj = pb_common.CommonResponse()
        CommonResponse_obj=rsp.response
        print CommonResponse_obj.response_code
        print CommonResponse_obj.response_msg



if __name__=="__main__":
    url="http://192.168.7.75:36900/api/v1.0/service_conf_req"
    rsp = smd.ServiceConfRsp()
    a=DataParse()
    cp_conf=a.ParseCPJson("cp.json")
    service_data=a.ServiceData("albert","http",cp_conf)

    # rsp_data=a.SendData(service_data,url)
    # rsp_data=os.system("curl -v --data \'"+service_data+"\' "+url)
    p = subprocess.Popen("curl -v --data \'"+service_data+"\' "+url, stdin = subprocess.PIPE,stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    a=p.stdout.read()

    # print rsp_data
    # import pdb
    # pdb.set_trace()
    rsp.ParseFromString(a)
    print "服务名称是：",rsp.service_name
    print "服务部署在：",rsp.service_dest_addr
    CommonResponse_obj = pb_common.CommonResponse()
    CommonResponse_obj = rsp.response
    print "响应码是：",CommonResponse_obj.response_code
    print "响应消息是：",CommonResponse_obj.response_msg
    # # a.ParseRsp(rsp)
    #
    #
    #
    # print "finish"
    # print
    # print rsp_data,"1"
    # print rsp_data,"2"
    # print rsp_data,"3"