import os
class os_funs:
    def make_user():
        os.system('sh ~/lab/test_project1/test_pro/get_services/user_ad_delete_modify.sh')
        exist_user = os.system('ls /etc/passwd | grep "user_agent" | sed -e "s/:.*//g"')
        #exist_user = USER="agent_user"; EXISTS=$( cat /etc/passwd | grep $USER | sed -e "s/:.*//g" ); echo $EXISTS
        if exist_user != "user_agent":
            #user = "user_agent"
            #sudoPassword = getpass.getpass('password: ')
            os.system('sh ~/lab/test_project1/test_pro/get_services/user_ad_delete_modify.sh')
            #os.system('echo %s|sudo -S %s\n' % (sudoPassword, command))
            #os.system('echo %s|sudo -S %s\n' % (sudoPassword, command_1))

    def get_uuid():
        uuid = os.system('dmidecode -s system-uuid')
        return uuid
