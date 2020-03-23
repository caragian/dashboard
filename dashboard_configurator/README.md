# NetEye 4 Dashboard deployment 

This script allows you to deploy a template dashboard to 
- a list of users
- all members of a specific AD group 


### 1. Create a template dashboard via Director
The first step is to create a Director User which will serve as template.

**Configuration > Authentication > Users > + Add a New User**

Create a suitable dashboard we can deploy.
Hint: Dashboard is stored in dashboard.ini within a folder having the same name as the user:
example: /neteye/shared/icingaweb2/conf/dashboards/tmpl_1/dashboard.ini

### 2. Setup: Prepare the environment

Follow the single steps as commands from "setup_environment.sh" to install the necessary requirements.
As alternative execute the script making sure to check provided output.

```
# chmod 775 "setup_environment.sh"
# ./setup_environment.sh
```
    

### 3.A Configuration of AD Group based deployment

Troubleshooting: Perform ldapsearch of group
Install dependencies if needed:
```
yum install openldap-clients.x86_64
```

Perform ldap search:
```
ldapsearch -D "username" -W -p 3268 -h DC-server -b "dc=mydomain,dc=lan" -s sub "(objectclass=Group)"
```

Now you should get the AD group with OU -Path like:
```
CN=group_name,OU=team1,OU=organisation1,OU=Users,OU=Companies,DC=mydomain,DC=lan
```

Take this path and assemble authentication.json

```
 **EXAMPLE JSON CREDENTIALS FILE TO LDAP SERVER**
 
 To specify the group to deploy the dashboard, is necessary to change the field **memberOf=CN=xxxxx**
 
     {   
        "config" : [

        {
            "host" : "xxxxx",
            "port" : xxxxx,
            "user" : "xxxxx",
            "password" : "xxxxx",
            "base" : "xxxxx",
            "search" : "(&(objectCategory=user)(memberOf=CN=xxxxx,OU=xxxxx,OU=xxxxx,OU=xxxxx,DC=xxxxx,DC=xxxxx))",
            "attr" :  ["samAccountName"]
        }
        ]
    }
```

### 3.B Configuration of Local user list based deployment

EXAMPLE JSON CONFIG_FILE FOR LOCAL USERS

```
#DEFINE USERS AND TEMPLATE TO ASSIGN
        "local_user" : [
        { "template" : "win", "user" : [ "User1", "User2" ]  },
        { "template" : "lin", "user" : [ "User3", "User4" ]  }
        ]
    }
```

### 4. Script execution

Scipt is executed using the python 3 envirionent created during setup:

- Go into the intallation paht of custom_dashboard
- Run script indicating the LDAP-authentication file and the name of the template 
```
cd /neteye/shared/icingaweb2/extras/custom_dashboard/
../python_virtual_env/custom_dashboard/bin/python3 insert_dashboard.py --ldap authentication.json --template tmpl_1
```

Executing script with list of local users:
```
../python_virtual_env/custom_dashboard/bin/python3 insert_dashboard.py -c config.json
```


Script help page:
```
../python_virtual_env/custom_dashboard/bin/python3 insert_dashboard.py --help
   Dashboard Tutorial || For more info and examples type "python3
insert_dashboard.py"

optional arguments:
  -h, --help      show this help message and exit
  -c CONFIG_FILE  Choose Your Config File
  -l LDAP         Choose your AD Config File for Authentication
  -t TMP_AD       In addition to -l, Choose your User Template for
                  distribution
  -d DISCOVER     Discover Users from AD Group

```


## 5. Discover Users From AD Group

Run the script with a parameter -d to just discover the users from AD group and show the usernames (samaccountnames) in console.
   
    python3 insert_dashboard.py -l authentication.json -d admin_group
    
 To activate the distribution of dashboards to discovered users is necessary to add only the template -t.
    
    python3 insert_dashboard.py -l authentication.json -d admin_group -t template_windows

 
 

        

