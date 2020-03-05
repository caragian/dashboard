mkdir -p /neteye/shared/icingaweb2/extras/custom_dashboard
mkdir /neteye/shared/icingaweb2/extras/python_virtual_env
cd /neteye/shared/icingaweb2/extras/python_virtual_env
virtualenv-3 custom_dashboard
/neteye/shared/icingaweb2/extras/python_virtual_env/custom_dashboard/bin/pip install configparser ldap3
cd /neteye/shared/icingaweb2/extras/custom_dashboard
cp <git_repo>/Dashboard_JSON/*.json .
cp <git_repo>/Dashboard_JSON/*.py .

chmod 775 insert_dashboard.py



#Perform ldapsearch of group
```
ldapsearch -D "username" -W -p 3268 -h xxx.xxx -b "dc=xxx,dc=xxx" -s sub "(objectclass=Group)"

```







