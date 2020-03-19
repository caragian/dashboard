# Deployment script for dashboard deploy
#
# (C) 2020 Nicolae Caragia, Würth Phoenix GmbH
#

import os, configparser, stat, argparse, json
from ldap3 import Server, Connection, ALL
# encoding=utf8
import sys
import logging

dashboard_tmpl = "dashboard.ini"
logging.basicConfig(level=logging.DEBUG)


parser = argparse.ArgumentParser(description='Dashboard Tutorial')
group = parser.add_mutually_exclusive_group()
group.add_argument('--config', '-c', dest='config_file', required=False, type=str, help='Choose Your Config File')
group.add_argument('--ldap', '-l', dest='ldap', required=False, type=str, help='Choose your AD Config File for Authentication')
parser.add_argument('--template', '-t', dest='tmp_ad', required=False, type=str, help='In addition to --ldap/-l, Choose your User Template for distribution')

args = parser.parse_args()


def helpOption():

    print("\nERROR  No arguments ERROR\n")
    print("insert_dashboard.py [-h] [--config CONFIG_FILE] [--ldap LDAP] [--template TMP_AD]")
    print("--config / -c      Choose your Config_File")
    print("--ldap / -l        Choose your AD Config File for Authentication")
    print("--template -t      In addition to --ldap/-l, Choose your User Template for distribution\n")
    print("\nExample:\n")
    print("python3 insert_dashboard.py -c config.json")
    print("python3 insert_dashboard.py -l authentication.json -t template_windows\n")




# The list of command line arguments passed to a Python script. argv[0] is the script name. So:
if len(sys.argv) == 1:
    helpOption()
    sys.exit(1)

config_file = args.config_file
authentication = args.ldap
tmp_ad = args.tmp_ad



def main_script(temp, user_list):
    os.chdir("/neteye/shared/icingaweb2/conf/dashboards")
    user_dash_tmpl = temp
    os.chdir(user_dash_tmpl)
    dashboardConfig = configparser.ConfigParser(interpolation=None)
    dashboardConfig.read(dashboard_tmpl)
    dashboard = open(dashboard_tmpl, "r")
    dashboard_content = dashboard.read()
    dashboard.close()
    os.chdir("/neteye/shared/icingaweb2/conf/dashboards")



    #change owner
    filename = "/neteye/shared/icingaweb2/conf/dashboards"
    st = os.stat(filename)
    usr_own = st.st_uid
    grp_own = st.st_gid

    #print(usr_own)
    #print(grp_own)

    #usr_own = 48    #apache
    #grp_own = 999   #icingaweb2

    #change mode

    dir_mode = stat.S_ENFMT | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP       #directory mode
    f_mode = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP      #file mode

    user_ini = "dashboard.ini"

    for user in user_list:


        path = user.lower()
        logging.debug("[i] Defining dashboard path and configuration file for user: %s" %user)

        if path == "user_dash_tmpl":
            print("\nWARNING : USER_DASH_TMPL IS DEFINE IN group1_users.txt !\n")
            quit()

        if path !="":
            if not os.path.exists(path):
                logging.debug("[+] Going to create dashboard path for user: %s" %path)

                os.mkdir(path)
                os.chown(path, usr_own, grp_own)
                os.chmod(path, dir_mode)
                os.chdir(path)

                content = open(user_ini, "w") 
                content.write(dashboard_content)
                content.close()

                os.chown(user_ini, usr_own, grp_own)
                os.chmod(user_ini, f_mode)

                os.chdir("/neteye/shared/icingaweb2/conf/dashboards")
            elif os.path.exists(path):

                os.chown(path, usr_own, grp_own)
                os.chmod(path, dir_mode)
                os.chdir(path)
            

                if not os.path.exists(user_ini):
                    content = open(user_ini, "w") 
                    content.write(dashboard_content)
                    content.close()

                    os.chown(user_ini, usr_own, grp_own)
                    os.chmod(user_ini, f_mode)
                    
                    os.chdir("/neteye/shared/icingaweb2/conf/dashboards")
                elif os.path.exists(user_ini):

                    os.chown(user_ini, usr_own, grp_own)
                    os.chmod(user_ini, f_mode)

                    file_size = os.stat(user_ini)

                    if file_size.st_size == 0:

                        content = open(user_ini, "w") 
                        content.write(dashboard_content)
                        content.close()
                    
                    elif file_size.st_size != 0:

                        usersConfig = configparser.ConfigParser(interpolation=None)
                        usersConfig.read(user_ini)
                        
                        for section in usersConfig.sections():
                            for section2 in dashboardConfig.sections():
                                exist = usersConfig.has_section(section2)
                                if section == section2:
                                    
                                    usersConfig[section] = dashboardConfig[section2]
                                    
                                elif not exist:
                                    usersConfig.add_section(section2)
                                    if dashboardConfig.has_option(section2, "title"):
                                        title = dashboardConfig.get(section2, "title")
                                        usersConfig.set(section2, "title", title)
                                    if dashboardConfig.has_option(section2, "url"):
                                        url = dashboardConfig.get(section2, "url")
                                        usersConfig.set(section2, "url", url)
                                    
                        with open(user_ini, "w") as configfile:
                            usersConfig.write(configfile)
                            configfile.close()
                        os.chdir("/neteye/shared/icingaweb2/conf/dashboards")
  





if config_file:
    with open(config_file) as f:
        data = json.load(f)
    f.close()
    for local_user in data["local_user"]:
        user_list = []
    
        temp = local_user["template"]
    
        for user in local_user["user"]:
            user_list.append(user)
    
        os.chdir("/neteye/shared/icingaweb2/conf/")
    
        directory = "dashboards"
        if os.path.exists(directory):
            os.chdir(directory)
        elif not os.path.exists(directory):
                os.mkdir(directory)
                os.chdir(directory)
        main_script(temp, user_list)

if authentication:

    if tmp_ad is None:
      print("ERROR !!!!!!!!Choose and template for your AD User !!!!!!!! ERROR")
      quit()

    with open(authentication) as f:
        data = json.load(f)
    f.close()


    host = data["config"][0]["host"]
    port = data["config"][0]["port"]
    user = data["config"][0]["user"]
    password = data["config"][0]["password"]
    base = data["config"][0]["base"]
    search = data["config"][0]["search"]
    attr = data["config"][0]["attr"]
    logging.debug("OK")
    server = Server(host, int(port), get_info=ALL)
    logging.debug("Server OK")
    conn = Connection(server, user, password, auto_bind=True)
    logging.debug("CONN")

    print("\nSuccessfully Connection To Server LDAP \n")
    conn.search(base, search, attributes = attr)


    logging.debug("Ok")
    
    
    result = conn.entries

    # Get list of users in AD group
    logging.debug("Starting to read users from AD Group. Results:\n %s" %(result))

    ad_list = []
    for entry in result:
        value = (json.loads(entry.entry_to_json()))
        ad_list.append((value["attributes"]["sAMAccountName"][0]))
        logging.debug("[i] Found user in AD Group: %s" %value["attributes"]["sAMAccountName"][0])

    conn.unbind()
    user_list = ad_list

    

    temp = tmp_ad
    main_script(temp, user_list)

    print("Deployed Dashboard: ",temp, " For: \n")
    print(*user_list, sep=", ")
    

print("\n Completed \n")
