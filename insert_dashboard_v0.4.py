import os 
import configparser
import stat


#read file

dashboardConfig = configparser.ConfigParser()
dashboardConfig.read("modifica.ini")

f = open("users.txt", "r")
dashboard_tmpl = "dashboard_tmpl.ini"
dashboard = open(dashboard_tmpl, "r")
dashboard_content = dashboard.read()
dashboard.close()

#every line is a user directory

user = f.readline()
user = user.strip("\n")
list = [user]

while user:
    user = f.readline()
    user = user.strip("\n")
    list.append(user) 
f.close()

os.chdir("..")

#create directory dashboard

directory = "dashboards"
if os.path.exists(directory):
    os.chdir(directory)
elif not os.path.exists(directory):
        os.mkdir(directory)
        os.chdir(directory)


#create user directory and configuration files for every user

user_ini = "dashboard.ini"

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


for user in list:
    path = user

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

                usersConfig = configparser.ConfigParser()
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


