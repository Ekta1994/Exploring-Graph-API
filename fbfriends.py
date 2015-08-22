# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:55:22 2015

@author: Ekta Goel
Email-id: ektagoel04@gmail.com
"""

import requests
import json
import urllib
import os

"""
Select user_friends field in User Data Permissions while generating the token.
"""

TOKEN = "Your generated token here";

def getpics():

	"""
	Generate the FQL query. The result is a combination of dictionaries and lists inside one another. For manually testing it, go on the link provided in readme.md and click on FQL query and type the query below in the space provided.
	"""
    query= ("SELECT first_name, last_name , pic FROM user WHERE uid IN  (SELECT uid2 FROM friend WHERE uid1 = me() ) LIMIT 5")
    payload = {'q' : query , 'access_token' : TOKEN}
	
	"""
	The requests.get() method needs the URL as a parameter. For appending key value pairs to this URL, the keyword params is used.
	"""
	
    r = requests.get("https://graph.facebook.com/fql", params = payload)
    result = json.loads(r.text)
    
    cnt = 0
	"""
	This command creates a folder named ProfilePics in your current working directory and all the profile pictures downloaded will be saved in this folder.
	"""
    imagepath = os.getcwd() + '\ProfilePics' ;
    os.chdir(imagepath)

	# the key data maps to a list of dictionaries, which contain information about your friends
    for pics in result['data']:
	
	   # We now have URLs of all the profile pics we want
       print("Downloading cover pic of : " + pics['first_name'] + pics['last_name'])
       resp = urllib.request.urlopen(pics['pic'])
	   
	   #By checking the response code, we ensure that the HTTP request has been processed successfully. Not checking it may lead to more waiting time.
	   
       if(resp.code == 200):         
           imagepath = str(cnt) +'.jpg';
           f = open("pic" + str(cnt) + ".jpg",'wb')
           f.write(requests.get(pics['pic']).content)
           f.close()
           cnt = cnt + 1;
       else:
           print("The profile pic of this user cant be downloaded ")
      

if __name__ == '__main__' :
    getpics()
    
