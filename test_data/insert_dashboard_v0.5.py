import os 
import configparser
import stat
import argparse
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#file

dashboard_tmpl = "dashboard.ini"

parser = argparse.ArgumentParser(description='Dashboard Tutorial')
parser.add_argument('--group', '-g', dest='users_file', required=True, type=str, help='Choose the User Group')
parser.add_argument('--template', '-t', dest='user_dash_tmpl', required=True, type=str, help='Choose the Template')

args = parser.parse_args()


users_file = args.users_file
user_dash_tmpl = args.user_dash_tmpl


#every line is a user directory

f = open(users_file, "r")
user = f.readline()
user = user.strip("\n")
list = [user]

while user:
    user = f.readline()
    user = user.strip("\n")
    list.append(user) 
f.close()

#create directory dashboard

os.chdir("..")

directory = "dashboards"
if os.path.exists(directory):
   os.chdir(directory)
elif not os.path.exists(directory):
        os.mkdir(directory)
        os.chdir(directory)

#read dashboard template

#directory user template
#user_dash_tmpl="user_dash_tmpl"


os.chdir(user_dash_tmpl)
dashboardConfig = configparser.ConfigParser(interpolation=None)
dashboardConfig.read(dashboard_tmpl)
dashboard = open(dashboard_tmpl, "r")
dashboard_content = dashboard.read()
dashboard.close()
os.chdir("..")



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

for user in list:

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

            os.chdir("..")
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
                
                os.chdir("..")
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
                                
                            elif exist == False:
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
                    os.chdir("..")

print("\n Completed \n")
