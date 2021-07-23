import requests
from datetime import datetime  
import json
from requests.api import head
cookie  = ""

def sign_up(acn ,pwd):
    my_data = {"account":acn , "password":pwd}
    jsonData = json.dumps(my_data)
    my_header = {'Content-Type' : 'application/json'}
    r = requests.post('http://tsukumonet.ddns.net:21126/signup' , headers=my_header, data=jsonData)
    if r.status_code == 200:
        print("OK!")
        print(r.text)
        print('---------------------------------')
        print(r.headers)
    else:
        print("ERROR!")

def login(acn,pwd):
    global cookie
    my_data = {"account":acn , "password":pwd}
    my_header = {'Content-Type' : 'application/json'}
    json_data = json.dumps(my_data)
    r = requests.post('http://tsukumonet.ddns.net:21126/login', headers= my_header, data=json_data)
    if r.status_code == 200:
        print('OK!')
        print(r.text , '\n---------------------------------\n' , r.headers['Set-Cookie'])
        cookie = r.headers['Set-Cookie']
    else:
        print("ERROR!")

def change_name():
    global cookie
    now = datetime.now()
    my_nickname = now.strftime("%Y%m%d%H%M%S")
    my_data ={'userNick':my_nickname}
    my_header = {'Content-Type' : 'application/json','Cookie':cookie}
    json_data = json.dumps(my_data)
    r = requests.post('http://tsukumonet.ddns.net:21126/post_userNick',headers = my_header , data=json_data)

    if r.status_code == 200:
        print("OK!")
        print("Nick name change complete.")
    else:
        print("ERROR!")



    

if __name__ == '__main__':
    acn = input('Input account:')
    pwd = input('Input password:')
    sign_up(acn,pwd)
    print('***********************************************')
    login(acn,pwd)
    print('***********************************************')
    change_name()