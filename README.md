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
    
 Move the script into custom_dashboard directory
 
    (custom_dashboard) [root@mynet Dashboard] mv insert_dashboard_v0.4.py ../custom_dashboard

Modify the users file **"group_users.txt"** with users involved in the new configuration.

**Warning : The Dashboard User Template must not be written in the "group1_users.txt"**

Run the script

    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.4.py


If doesn't exists a **"dashboard.ini"** for a new user, the first **"dashboard.ini"** will be set by **"dashboard.ini"** from the Dashboard User Template Directory.
