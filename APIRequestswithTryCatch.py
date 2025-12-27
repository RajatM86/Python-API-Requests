import json
import string
import sys
from os import name

import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
from dotenv import load_dotenv







#base_url
base_url= "https://gorest.co.in/"

#AUTH TOKEN

def validate_token():
    """
        Checks if the access token is present in the environment variables.
        Exits the script with an error message if the token is not found.
        """
    # Use os.getenv() to retrieve the environment variable value

    TOKEN_ENV_VAR_NAME = "AUTH_TOKEN"

    auth_token = os.getenv(TOKEN_ENV_VAR_NAME)

    if not auth_token:
        # If the variable is missing or empty, print an error and exit
        print(f"Error: Environment variable '{TOKEN_ENV_VAR_NAME}' not found or is empty.")
        print("Please set the environment variable before running the script.")
        # Exit with a non-zero status code to indicate an error
        sys.exit(1)

    # If the token is found, you can return it for use in your application
    print(f"Success: Access token loaded from environment variable '{TOKEN_ENV_VAR_NAME}'.")
    print(auth_token)
    return auth_token



def getrandomemail():
    email_length=10
    domain="automation.com"
    random_email= "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(email_length))
    email = random_email + "@" + domain
    print (email)
    return email
#Get Request

def get_request():
    url= base_url + "/public/v2/users"
    headers={'Authorization': validate_token()}
    response= requests.get(url, headers=headers)
    assert response.status_code == 200
    json_body= response.json()
    #print(json_body)
    final_json=json.dumps(json_body,indent=4)
    print(final_json)


#POST Request
def post_request():
    url= base_url + "/public/v2/users"

    print("POST URL", url)
    headers={'Authorization': auth_token}
    data ={

        "name": "ABCD",
        "email": getrandomemail(),
        "gender": "female",
        "status": "active"
    }

    response_post= requests.post(url, headers=headers, json=data)
    assert response_post.status_code==201
    response_post_body= response_post.json()
    final_post= json.dumps(response_post_body,indent=4)
    print(final_post)
    user_id=response_post_body['id']
    return user_id




def put_request(user_id):
    url= base_url +  f"/public/v2/users/{user_id}"
    print("PUT URL", url)
    headers={'Authorization': auth_token}
    data ={

        "name": "ABCD",
        "email": getrandomemail(),
        "gender": "female",
        "status": "inactive"
    }

    response_put= requests.put(url, headers=headers, json=data)
    assert response_put.status_code==200
    response_put_body= response_put.json()
    final_post= json.dumps(response_put_body,indent=4)
    print(final_post)

validate_token()
get_request()
getrandomemail()
#user_id= post_request()
#put_request(user_id)




