import requests
import pytest
import json

products_endpoint = "https://automationexercise.com/api/productsList"
brands_endpoint = "https://automationexercise.com/api/brandsList"
account_details_endpoint = "https://automationexercise.com/api/getUserDetailByEmail"

def payload_to_get(email):
    return {
        "email": email
    }

# API 1: Get All Products List

def test_Get_All_Products_List():
    response = requests.get(products_endpoint)
    json_response = json.loads(response.text)
    assert response.status_code == 200

# API 3: Get All Brands List

def test_Get_All_Brands_List():
    response = requests.get(brands_endpoint)
    json_response = json.loads(response.text)
    print(json_response)
    assert response.status_code == 200

# API 14: GET user account detail by email

def test_Get_User_Details():
    user_email = payload_to_get("arthasthelichking@gmail.com")
    response = requests.get(account_details_endpoint, data=user_email)
    json_response = json.loads(response.text)
    print(json_response)
    assert response.status_code == 200 
    assert "message" in json_response


