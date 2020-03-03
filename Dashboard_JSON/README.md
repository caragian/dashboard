# Dashboard

The first step is to create a Director User which will serve as template.

**Configuration > Authentication > Users > + Add a New User**

Run the Script "python_dashboard_JSON.sh" to install the necessary requirements.

    [root@mynet /]# chmod 775 python_dashboard_JSON.sh
    [root@mynet /]# ./python_dashboard_JSON.sh
    
Active Python Virtualenv

    source /neteye/shared/icingaweb2/python_virtual_env/custom_dashboard/bin/activate

Create / Modify the users file with users involved in the new configuration.

**Warning : The Dashboard User Template must not be written in the "config.json"**

Run the script specifying the user file and the user template via options and arguments from command line

    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.7.py -c config.json
    
    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.7.py --help
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
