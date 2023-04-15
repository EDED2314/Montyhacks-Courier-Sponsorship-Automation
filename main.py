from trycourier import Courier
import os
from dotenv import load_dotenv

load_dotenv()


def sendemail(name_with_prefix, nameOfCompany):
    auth = os.getenv("AUTH")
    temp = os.getenv("template")

    client = Courier(auth_token=f"{auth}")

    resp = client.send_message(
        message={
            "to": {
                "email": "eddietang2314@gmail.com",
            },
            "template": f"{temp}",
            "data": {
                "name_with_prefix": name_with_prefix,
                "nameofCompany": nameOfCompany,
            },
        }
    )

    # print(resp['requestId'])


sendemail("Mr. Eddie Tang", "Montgomery High School")
