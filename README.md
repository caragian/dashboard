# Dashboard

The first step is to create a Director User which will serve as template.

NOTE : Place the directory dashboard_custom in :

  /neteye/shared/icingaweb2/conf/

Requirement is also the creation of a Python Virtualenv.

yum install -y python-pip python-virtualenv

virtualenv custom_dashboard 

source $PWD/custom_dashboard/bin/activate

Now is necessary to install the module configparser

pip install configparser




1. Modify the users file **"users.txt"** with users involved in the new configuration.


Notes

If doesn't exists a **"dashboard.ini"** for a new user, the first **"dashboard.ini"** will be setted by **"dashboard_tmpl.ini"**
