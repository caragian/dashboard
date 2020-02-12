# Dashboard

The first step is to create a Director User which will serve as template.

**Configuration > Authentication > Users > + Add a New User**

Create a directory, wirch contains the script and the user file in :

    [root@mynet /]# mkdir /neteye/shared/icingaweb2/conf/custom_dashboard

Requirement is also the creation of a Python Virtualenv.

    [root@mynet /]# yum install -y python-pip python-virtualenv
    
    [root@mynet /]# virtualenv custom_dashboard

    [root@mynet /]# source $PWD/custom_dashboard/bin/activate

Now is necessary to install the module configparser

    (custom_dashboard) [root@mynet /]# pip install configparser

Modify the users file **"group_users.txt"** with users involved in the new configuration.

**Warning : The Dashboard User Template must not be written in the "group1_users.txt"**

Run the script

    (custom_dashboard) [root@mynet custom_dashboard]# python insert_dashboard_v0.4.py


If doesn't exists a **"dashboard.ini"** for a new user, the first **"dashboard.ini"** will be set by **"dashboard.ini"** from the Dashboard User Template Directory.
