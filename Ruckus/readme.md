This folder contains Python automation for Ruckus.

The code here was created for The Commscope Ruckus Virtual SmartZone (vSZ).  The API calls are detailed on the Commscope Ruckus website:  https://docs.ruckuswireless.com/smartzone/6.1.0/vszh-public-api-reference-guide-610.html


I created a class type in the ruckusVSM.py file that is used to call the different methods.  This code is used to show you how to get started with the Ruckus APIs.  Here are the 6 methods I created as part of this turtorial:

vsmAuth()
This is how you login to the vSZ and get a Token to be able to use the APIs

deleteToken()
This is how you can delete the Token created

getAllZones()
This will return all zones the user that created the Token has access to

filterZone()
This takes all the zones and creates a simple list that can be searched

getZone()
This gets all the configuration specific information for a specified Zone

getSessions()
This shows all of the sessions that are current active in vSZ