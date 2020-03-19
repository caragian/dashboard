# Install python 3 software
yum --enablerepo=neteye-extras install python3-devel.x86_64 python3-pip.noarch python36-virtualenv

# Configure
# Create folders and copy files
echo "Going to configure folders and files..."
mkdir -p /neteye/shared/icingaweb2/extras/custom_dashboard
mkdir /neteye/shared/icingaweb2/extras/python_virtual_env

cp authentication.json /neteye/shared/icingaweb2/extras/custom_dashboard/
cp config.json /neteye/shared/icingaweb2/extras/custom_dashboard/
cp insert_dashboard.py /neteye/shared/icingaweb2/extras/custom_dashboard/

# Install virtual environment
echo "Going to install python3 virtual environment ...."
cd /neteye/shared/icingaweb2/extras/python_virtual_env
virtualenv-3 custom_dashboard
/neteye/shared/icingaweb2/extras/python_virtual_env/custom_dashboard/bin/pip3 install configparser ldap3
cd /neteye/shared/icingaweb2/extras/custom_dashboard

#Set script writable
chmod 775 insert_dashboard.py

