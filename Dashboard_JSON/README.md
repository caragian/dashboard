# Dashboard

The first step is to create a Director User which will serve as template.

**Configuration > Authentication > Users > + Add a New User**

Create a directory, witch contains the script and the user file in :

    [root@mynet /]# mkdir /neteye/shared/icingaweb2/conf/custom_dashboard
    
Requirement is also the creation of a Python Virtualenv, so create a directory in **/neteye/shared/icingaweb2/**, wich contains the Virtualenv configuration:

    [root@mynet icingaweb2]# mkdir /neteye/shared/icingaweb2/python_virtual_env

    [root@mynet icingaweb2]# yum install -y python-pip python-virtualenv
    
    [root@mynet icingaweb2]# virtualenv custom_dashboard

    [root@mynet icingaweb2]# source $PWD/custom_dashboard/bin/activate

Now is necessary to install the module configparser

    (custom_dashboard) [root@mynet icingaweb2]# pip install configparser
    
Clone the Dashboard directory from Github.

    (custom_dashboard) [root@mynet custom_dashboard]# git clone https://github.com/caragian/Dashboard.git
    
 Move the script into custom_dashboard directory and give it 775 permission
 
    (custom_dashboard) [root@master Dashboard_JSON]#] mv insert_dashboard_v0.6.py ../custom_dashboard
    
    (custom_dashboard) [root@mynet custom_dashboard] chmod 775 insert_dashboard_v0.6.py

Create / Modify the users file with users involved in the new configuration.

**Warning : The Dashboard User Template must not be written in the "config.json"**

Run the script specifying the user file and the user template via options and arguments from command line

    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.6.py -c config.json
    
    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.6.py --help
    Dashboard Tutorial

    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG_FILE, -c CONFIG_FILE
                            Choose Your Config File
                            
**EXAMPLE JSON CONFIG_FILE**

    #CREDENTIALS TO CONNECT TO LDAP SERVER
    {   
        "config" : [

        {
            "host" : "SECRET",
            "port" : 3268,
            "user" : "USER",
            "password" : "PASSWORD",
            "ldap_server" : "server",
            "ldap_user" : "user1",
            "ldap_password": "password",
            "base" : "BASE",
            "search" : "FILTER"
        }
        ],
        
    #DEFINE USERS AND TEMPLATE TO ASSIGN
        "local_user" : [
        { "template" : "win", "user" : [ "User1", "User2" ]  },
        { "template" : "lin", "user" : [ "User3", "User4" ]  }
        ]
    }
