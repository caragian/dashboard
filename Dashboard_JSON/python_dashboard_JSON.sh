mkdir -p /neteye/shared/icingaweb2/extras/custom_dashboard
mkdir /neteye/shared/icingaweb2/extras/python_virtual_env
cd /neteye/shared/icingaweb2/extras/python_virtual_env
yum install -y python-pip python-virtualenv
virtualenv custom_dashboard
sleep 5s
/neteye/shared/icingaweb2/extras/python_virtual_env/custom_dashboard/bin/pip install configparser ldap3
cd /root/git-rep
cd neteye_community/Dashboard/Dashboard_JSON/
chmod 775 insert_dashboard.py
cp insert_dashboard.py /neteye/shared/icingaweb2/extras/custom_dashboard
cp config.json /neteye/shared/icingaweb2/extras/custom_dashboard
cp authentication.json /neteye/shared/icingaweb2/extras/custom_dashboard








