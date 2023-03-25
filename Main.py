from twilio.rest import Client
import requests
import json
import weather_get
import assignments



def sms_main(my_num):
    Account_SID = "AC333eb2b4e2d12197aad4cff3d16a8a59"
    Auth_Tocken = "a4f7e03cfbce4a3d7f8a5f7aa5e1809a"

    twiliocli = Client(Account_SID, Auth_Tocken)

    twilio_num = "+18663480857"


    if weather_get.temp <= 66:
        body = f""""
        Hello Master the Temputare is {weather_get.temp}°F don't forget to wear a jacket!
        Here is your next upcoming assingmnet:{assignments.event_info}
         """
        
        message = twiliocli.messages.create(body = body, from_ = twilio_num, to = my_num)

        print(message)
    else:
        body = f" Hello Master the Temputare is {weather_get.temp}°F Have a great day!, Here are your upcoming assingments: {assignments.event_info}"
        message = twiliocli.messages.create(body = body, from_ = twilio_num, to = my_num)
        print(message)

sms_main("+12142743718")

