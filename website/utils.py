#-*- coding: utf-8 -*-

#MYSQL
MYSQL_HOST = '10.42.0.19'
MYSQL_PORT = '3306'
MYSQL_USER = 'ops1'
MYSQL_PASS = 'MyNewPass4!'
MYSQL_DB = 'cmdb'

#SALT
SALT_API_URL = 'salt'
SALT_PORT = '80'
SALT_MASTER_PORT = '4505'
SALT_API_USER = 'saltapi'
SALT_API_PASSWD = 'pass4saltapi'
SALT_EAUTH = 'pam'
SALT_API_TIMEOUT = 30

#RABBIT
BROKER_HOST = '10.42.0.20'
BROKER_PORT = 5672
BROKER_M_PORT = 15672
BROKER_USER = 'admin'
BROKER_PASSWORD = '111qqq!'
BROKER_VHOST = 'cmdb'

#LDAP
#测试环境
LDAP_URL = '192.168.121.237'
LDAP_PORT = '389'
LDAP_BIND = 'CN=administrator,CN=Users,DC=cangoad,DC=con,DC=cn'
LDAP_PWD = "Cango24a"
LDAP_OU = unicode('DC=cangoad,DC=con,DC=cn', 'utf8')

#Jenkins
JENKINS_URL = '10.42.0.18'
JENKINS_PORT = '8080'
JENKINS_USERNAME = 'admin'
JENKINS_PWD = '111qqq!'

#SESSION
Expire = 3600
#!|%t|tQi7&Dt~ON

#TokenExpired

DAY = 1

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
