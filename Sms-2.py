#!/usr/bin/python
import random
import twilio

  
ACCOUNT_SID = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"

client =twilio.rest.TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
reasons =(
	"someone skullfucked the system",
	"New Doctor who",
	 "who dis?",
	 "Hungover",
	 "Can't talk now",

	)
y= random.randint(0,4)
message = client.messages.create(

	body = "On my way "+reasons[y],
	to = "+XXX",
	from_="+XXXX",

	)
print message.sid