#-*- coding: utf-8 -*-

#MYSQL
MYSQL_HOST = '10.32.24.8'
MYSQL_PORT = '3306'
MYSQL_USER = 'ops1'
MYSQL_PASS = 'MyNewPass4!'
MYSQL_DB = 'cango_cmdb'

#SALT
SALT_API_URL = 'salt.cango.local'
SALT_PORT = '80'
SALT_MASTER_PORT = '4505'
SALT_API_USER = 'saltapi'
SALT_API_PASSWD = 'pass4saltapi'
SALT_EAUTH = 'pam'
SALT_API_TIMEOUT = 30

#RABBIT
BROKER_HOST = '10.32.24.8'
BROKER_PORT = 5672
BROKER_M_PORT = 15672
BROKER_USER = 'admin'
BROKER_PASSWORD = '111qqq!'
BROKER_VHOST = 'myvhost'

#LDAP
#正式环境
LDAP_URL = '10.32.24.2'
LDAP_PORT = '389'
LDAP_BIND = 'CN=Ldap,CN=Users,DC=cangoonline,DC=com'
LDAP_PWD = "X3cWdP@dLQ9\gCf"
LDAP_OU = unicode('OU=灿谷,DC=cangoonline,DC=com', 'utf8')

#SESSION
Expire = 3600
#!|%t|tQi7&Dt~ON

#docker启动mysql
'''docker run --net=host --restart=always --privileged=true -v /usr/docker_dat/mysql/data:/var/lib/mysql --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -v /etc/localtime:/etc/localtime:ro -d mysql --lower_case_table_names=1'''  

#jenkis节点java和maven环境变量配置
'''
export JAVA_HOME=/usr/java/jdk1.8.0_151
export M3=/usr/local/maven
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$M3/bin:$PATH
'''

#docker Harbor 登陆配置
'''
/etc/sysconfig/docker
HTTP_PROXY=http://192.168.121.237:808
export HTTP_PROXY
INSECURE_REGISTRY="--insecure-registry=10.42.0.17"
'''
