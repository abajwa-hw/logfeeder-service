#!/usr/bin/env python
from resource_management import *
import os
from resource_management.libraries.functions.default import default

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()

hdp_version = default("/commandParams/version", None)

logfeeder_downloadlocation = config['configurations']['logfeeder-config']['logfeeder_download_location']

if logfeeder_downloadlocation == 'RPM':
  logfeeder_dir = '/usr/hdp/'+hdp_version+'/logfeeder'
else:  
  logfeeder_dir = config['configurations']['logfeeder-config']['logfeeder_dir']



logfeeder_downloadlocation = config['configurations']['logfeeder-config']['logfeeder_download_location']

  
#solr configs
solr_znode = config['configurations']['solr-config']['solr.znode']
#solr_dir = config['configurations']['solr-config']['solr.dir']
#solr_downloadlocation = config['configurations']['solr-config']['solr.download.location']
#solr_cloudmode = config['configurations']['solr-config']['solr.cloudmode']

#if solr_downloadlocation == 'HDPSEARCH':
#  solr_dir='/opt/lucidworks-hdpsearch/solr'
#  solr_bindir = solr_dir + '/bin/'
#else:
#  solr_bindir = solr_dir + '/latest/bin/' 

#solr_host = config['configurations']['logfeeder-config']['solr_host']
#solr_port = str(config['configurations']['logfeeder-config']['solr_port'])

#otherconfigs
java64_home = config['hostLevelParams']['java_home']  
zookeeper_port=default('/configurations/zoo.cfg/clientPort', None)
#get comma separated list of zookeeper hosts from clusterHostInfo
index = 0 
zookeeper_quorum=""
for host in config['clusterHostInfo']['zookeeper_hosts']:
  zookeeper_quorum += host + ":"+str(zookeeper_port)
  index += 1
  if index < len(config['clusterHostInfo']['zookeeper_hosts']):
    zookeeper_quorum += ","




# logfeeder-env configs
logfeeder_user = config['configurations']['logfeeder-env']['logfeeder_user']
logfeeder_group = config['configurations']['logfeeder-env']['logfeeder_group']
logfeeder_log_dir = config['configurations']['logfeeder-env']['logfeeder_log_dir']
logfeeder_log = logfeeder_log_dir+'/logfeeder.log'

logfeeder_env_content = config['configurations']['logfeeder-env']['content']

#e.g. /var/lib/ambari-agent/cache/stacks/HDP/2.2/services/solr-stack/package
service_packagedir = os.path.realpath(__file__).split('/scripts')[0]

#get comma separated list of zookeeper hosts from clusterHostInfo
zookeeper_hosts = ",".join(config['clusterHostInfo']['zookeeper_hosts'])
