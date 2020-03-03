mkdir /neteye/shared/icingaweb2/conf/custom_dashboard
mkdir /neteye/shared/icingaweb2/python_virtual_env
cd /neteye/shared/icingaweb2/python_virtual_env
yum install -y python-pip python-virtualenv
virtualenv custom_dashboard
pip install configparser
cd /root/git-rep
git clone https://github.com/caragian/Dashboard.git
cd
cd git-rep/Dashboard/Dashboard_TXT/
chmod 775 insert_dashboard_v0.5.py
cp insert_dashboard_v0.5.py /neteye/shared/icingaweb2/conf/custom_dashboard
cp group1_user1.txt /neteye/shared/icingaweb2/conf/custom_dashboard
cp exaple_dashboard.txt /neteye/shared/icingaweb2/conf/custom_dashboard




