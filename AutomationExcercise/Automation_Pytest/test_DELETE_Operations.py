import requests
import json
import pytest

verify_endpoint = "https://automationexercise.com/api/verifyLogin"
delete_endpoint = "https://automationexercise.com/api/deleteAccount"

def delete_payload(email, password):
    return {
        "email": email,
        "password": password 
    }

# API 9: DELETE To Verify Login

def test_Delete_To_Verify_Login():
    response = requests.delete(verify_endpoint)
    json_response = json.loads(response.text)
    assert json_response["responseCode"] == 405

# API 12: DELETE METHOD To Delete User Account

def test_Delete_Method_To_Delete_User_Account():
    payload_to_delete = delete_payload("gregoryflask@gmail.com", "gogonono")
    response = requests.delete(delete_endpoint, data=payload_to_delete)
    json_response = json.loads(response.text)
    assert json_response["responseCode"] == 200
    assert "message" in json_response
    assert json_response["message"] == "Account deleted!"

