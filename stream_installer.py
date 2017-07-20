#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: stream_installer.py
@time: 2017/07/20/22:21
"""



def do_install(service_name, url = "http://192.168.5.30:8088/jenkins/view/%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%BA%BF/job/build_platform_fsp_stream/lastSuccessfulBuild/artifact/fsp-sss-stream-1.0.0.1.tar.gz"):

    parts = urlparse.urlparse(url)

    # parts中包含5部分，分别是：scheme='http',netloc='192.168.5.30:8088',path='/jenkins/vxxxxxxxx‘，params='', query='', fragment=''
    pkgname = parts.path.split("/")[-1] #通过/分割path中的各个字段，取最后一个，也就是包名：fsp-sss-stream-1.0.0.1.tar.gz
    uncompress_destdir = "/tmp"
    uncompress_dirname = pkgname.rstrip(".tar.gz")
    install_dirname = "/fsp_sss_stream"
    filepath = parts.path


     #这个if 主要是做下载安装包的操作
    if parts.scheme or parts.netloc:
        filepath = pkgname#此时filepath=fsp-sss-stream-1.0.0.1.tar.gz
        retcode = subprocess.call(["rm", filepath])# 这一步主要是做删除操作：如果本地有跟将要下载的连接中的包的名字一致，那么久将本地的安装包fsp-sss-stream-1.0.0.1.tar.gz删除。
        #这个主要是为了防止当开发有心改动合并进来，但是包名跟本地的一致，然后就下载失败的问题
        if retcode != 0:
            print "rm {0} is failed".format(filepath)
            return (None, None)
        retcode = subprocess.call(["curl", "-C", "-", url, "-o", filepath])
        print "curl return {0}".format(retcode)
        if retcode != 0:
            print "download {0} failed".format(url)
            return (None, None)
    # 如果第一个if 写进去了，那么filepath是fsp-sss-stream-1.0.0.1.tar.gz，此时这个一个都是返回TRUE，然后not true 就是FALSE了
    if not os.path.exists(filepath):
        print "{0} not exists".format(filepath)
        return (None, None)

    os.chdir("{0}".format(uncompress_destdir))
    if os.path.exists(uncompress_dirname):
       retcode = subprocess.call(["rm","-rf", uncompress_dirname])
       if retcode != 0:
           print "delete pkg files in {0} is failed".format(uncompress_destdir)
           return (None, None)

    os.chdir("{0}/smd".format(install_dirname))
    retcode = subprocess.call(["tar", "xf", filepath, "-C", uncompress_destdir])
    if retcode != 0:
        print "uncompress {0} failed".format(filepath)
        return (None, None)

    install_script_path = "{0}/{1}/tools/install_server.sh".format(uncompress_destdir, uncompress_dirname)
    if not os.path.exists(install_script_path):
        print "install script {0} not exist".format(install_script_path)
        return (None, None)

    if service_name in ["cp", "ss", "gs", "stream_as", "group_as", "ice", "sc", "gc", "sp", "access", "ma", "ms", "rule"]:
        curdir = os.getcwd()
        os.chdir("{0}/{1}/tools".format(uncompress_destdir, uncompress_dirname))
        subprocess.call(["./install_server.sh", service_name])
        os.chdir(curdir)

    # install.sh 将会 service_name 安装到 /fsp_sss_stream/service_name 目录下
    return (install_dirname, service_name)

def save_service_status(name, script, pid=[], destdir="/fsp_sss_stream/smd/stop"):
    if not os.path.exists(destdir):
        os.mkdir(destdir)

    status = {
        "service_name": name,
        "script": script,
        "pid": pid
    }

    loc = "{dirname}/{filename}.json".format(dirname=destdir, filename=name)
    with open(loc, "w") as fileobj:
        json.dump(status, fileobj, indent=8)

def stop_service(name, dir="/fsp_sss_stream/smd/stop"):
    filename = "{dirname}/{service_name}.json".format(dirname=dir, service_name=name)
    with open(filename) as fileobj:
        status = json.load(fileobj)
        pids = status["pid"]
        if (pids is not None) and len(pids) > 0:
            for pid in pids:
                subprocess.call(["kill", "-KILL", str(pid)])
        else:
            script = status["script"]
            subprocess.call([script])
    subprocess.call(["rm", filename])
