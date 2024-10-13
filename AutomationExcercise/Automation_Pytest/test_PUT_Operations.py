import requests
import json
import pytest

brands_endpoint = "https://automationexercise.com/api/brandsList"
update_account_endpoint = "https://automationexercise.com/api/updateAccount"

def update_payload(name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, 
                   company, address1, address2, country, zipcode, state, city, mobile_number):
    return {
        "name": name,
        "email": email,
        "password": password,
        "title": title,
        "birth_date": birth_date,
        "birth_month": birth_month,
        "birth_year": birth_year,
        "firstname": firstname,
        "lastname": lastname,
        "company": company,
        "address1": address1,
        "address2": address2,
        "country": country,
        "zipcode": zipcode,
        "state": state,
        "city": city,
        "mobile_number": mobile_number
    }

# API 4: PUT To All Brands List

def test_Put_To_All_Brands_List():
    response = requests.put(brands_endpoint)
    json_response = json.loads(response.text)
    assert json_response["responseCode"] == 405 # 405 status code on purpose

# API 13: PUT METHOD To Update User Account
def test_Update_User_Account():
    try:
        payload_to_update_account = update_payload("gregorythetailor", "gregoryflask@gmail.com", "gogonono", 
                                                    "Mr", "13", "February", "1984", "Gregory", "Flask", "Loar Ltd.", 
                                                    "1748 Irving Road", "1430 Beagle Drive", "United States", "45701", "Ohio", "Athens",
                                                    "740-517-0014")
        response = requests.put(update_account_endpoint, data=payload_to_update_account)
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert json_response["responseCode"] == 200
    assert "message" in json_response
    assert json_response["message"] == "User updated!"
