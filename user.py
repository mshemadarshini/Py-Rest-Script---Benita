#/usr/local/bin/python3.6


import json, time, os, urllib.request



class CollectUser:
    def __init__(self):
        print("New User to Collect ")


    # add users coming from rest to the list of sudo users of an Ubuntu machine

    def get_sudo_users(self,hostname):
        ip_address  = hostname.replace(' ','%20')
        url = "https://database.company.com/devices/" + ip_address + "/allowedUsers"
        json_obj= urllib.request.urlopen(url)
        userlist = json.load(json_obj)

        for user in userlist:
            # get the list of user from rest
            print(user['name'])
            # add the user into os sudo group
            # assuming os is linux bistro
            os.system("sudo usermod -a -G sudo " + user)



if __name__ == '__main__':
    CollectUser.get_sudo_users("<<enter the hostname here replacing the string>>")


