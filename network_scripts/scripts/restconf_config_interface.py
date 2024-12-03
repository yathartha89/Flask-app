import requests

from requests.auth import HTTPBasicAuth

from getpass import getpass

import urllib3

import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = getpass("Enter the username: ")

password = getpass("Enter the password: ")

ios_cred = HTTPBasicAuth(username=username,password=password)

ios_headers = {"Content-Type": "application/yang-data+json"}

ios_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

interface_config = {

              "ietf-interfaces:interface": {

                                  "name": "Loopback40",

                                  "description": "Loopback interface configured by YV using restconf",

                                  "enabled": "true",

                                  "type": "iana-if-type:softwareLoopback",

                                  "ietf-ip:ipv4": {
 
                                        "address": [

                                               {

                                                "ip": "4.4.4.4",

                                                "netmask": "255.255.255.255"

}
]
} 
}
}



                          
 
def interface():

   config = requests.post(url=ios_url,auth=ios_cred,headers=ios_headers,data=json.dumps(interface_config),verify=False)

   if config.status_code in [200, 201, 204]:

      print("The configuration is pushed successfully\n")

      print("The status code is: ",config.status_code)

   else:

      print("The request is not successful\n")

      print("The status code is: ",config.status_code)
 
      print("The response is: ",config.text)

interface()



   
