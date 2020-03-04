mkdir /neteye/shared/icingaweb2/extras/custom_dashboard
mkdir /neteye/shared/icingaweb2/extras/python_virtual_env
cd /neteye/shared/icingaweb2/extras/python_virtual_env
yum install -y python-pip python-virtualenv
virtualenv custom_dashboard
sleep 5
source /neteye/shared/icingaweb2/extras/python_virtual_env/custom_dashboard/bin/activate
pip install configparser
pip install ldap3
cd /root/git-rep
git clone https://github.com/caragian/Dashboard.git
cd
cd git-rep/Dashboard/Dashboard_JSON/
chmod 775 insert_dashboard.py
cp insert_dashboard.py /neteye/shared/icingaweb2/extras/custom_dashboard
cp config.json /neteye/shared/icingaweb2/extras/custom_dashboard
cp authentication.json /neteye/shared/icingaweb2/extras/custom_dashboard








