import os, configparser, stat, argparse, json
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dashboard_tmpl = "dashboard.ini"


parser = argparse.ArgumentParser(description='Dashboard Tutorial')
parser.add_argument('--config', '-c', dest='config_file', required=True, type=str, help='Choose Your Config File')
parser.add_argument('--local', '-l', dest='local', required=False, type=str, help='Choose Local User')
parser.add_argument('--ad', '-a', dest='ad', required=False, type=str, help='Choose AD User')

args = parser.parse_args()
config_file = args.config_file
local = args.local
ad = args.ad


with open(config_file) as f:
  data = json.load(f)
f.close()

n=0
user_list = []
for local_user in data["local_user"]:
    y=0

    temp = local_user["template"]

    for elemet in local_user:
        user = local_user["user"][y]
        y+=1
        user_list.append(user)
    os.chdir("/neteye/shared/icingaweb2/conf/")

    directory = "dashboards"
    if os.path.exists(directory):
        os.chdir(directory)
    elif not os.path.exists(directory):
            os.mkdir(directory)
            os.chdir(directory)

    #read dashboard template


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

        path = user

        if path == "user_dash_tmpl":
            print("\nWARNING : USER_DASH_TMPL IS DEFINE IN group1_users.txt !\n")
            quit()

        if path !="":
            if not os.path.exists(path):

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
  
    n+=1


    

print("\n Completed \n")
