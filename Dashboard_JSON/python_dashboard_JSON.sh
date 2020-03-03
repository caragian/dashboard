mkdir /neteye/shared/icingaweb2/conf/custom_dashboard
mkdir /neteye/shared/icingaweb2/python_virtual_env
cd /neteye/shared/icingaweb2/python_virtual_env
yum install -y python-pip python-virtualenv
virtualenv custom_dashboard
pip install configparser
cd /root/git-rep
git clone https://github.com/caragian/Dashboard.git
cd
cd git-rep/Dashboard/Dashboard_JSON/
chmod 775 insert_dashboard_v0.6.py
cp insert_dashboard_v0.6.py /neteye/shared/icingaweb2/conf/custom_dashboard
cp config.json /neteye/shared/icingaweb2/conf/custom_dashboard



