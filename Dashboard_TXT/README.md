# Dashboard

The first step is to create a Director User which will serve as template.

**Configuration > Authentication > Users > + Add a New User**

Run the Script "python_dashboard_TXT.sh" to install the necessary requirements.

    [root@mynet /]# chmod 775 python_dashboard_TXT.sh
    [root@mynet /]# ./python_dashboard_JSON_TXT.sh
    
Active Python Virtualenv

    source /neteye/shared/icingaweb2/python_virtual_env/custom_dashboard/bin/activate

Create / Modify the users file with users involved in the new configuration.

**Warning : The Dashboard User Template must not be written in the "group_user.txt"**

Run the script specifying the user file and the user template via options and arguments from command line

    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.5.py -g group1_user.txt -t user_template
    
    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.5.py --help
    insert_dashboard_v0.4.py --group USERS_FILE --template USER_DASH_TMPL

    Dashboard Tutorial

      --group USERS_FILE, -g USERS_FILE
                            Choose the User Group
                            
      --template USER_DASH_TMPL, -t USER_DASH_TMPL
                            Choose the Template
