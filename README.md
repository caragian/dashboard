# Dashboard

The first step is to create a Director User which will serve as template.

NOTE : Place the directory dashboard_custom in :

    [root@mynet /]# /neteye/shared/icingaweb2/conf/

Requirement is also the creation of a Python Virtualenv.

    [root@mynet /]# yum install -y python-pip python-virtualenv
    
    [root@mynet /]# virtualenv custom_dashboard

    [root@mynet /]# source $PWD/custom_dashboard/bin/activate

Now is necessary to install the module configparser

    [root@mynet /]# pip install configparser




1. Modify the users file **"users.txt"** with users involved in the new configuration.


Notes

If doesn't exists a **"dashboard.ini"** for a new user, the first **"dashboard.ini"** will be setted by **"dashboard_tmpl.ini"**
