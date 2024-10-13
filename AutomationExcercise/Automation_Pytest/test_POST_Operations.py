import requests
import json
import pytest

products_endpoint = "https://automationexercise.com/api/productsList"
search_endpoint = "https://automationexercise.com/api/searchProduct"
verify_login_endpoint = "https://automationexercise.com/api/verifyLogin"
create_account_endpoint = "https://automationexercise.com/api/createAccount"

payload_for_search = {
    "search_product": "tshirt"
}

payload_for_verify = {
    "email": "razafafda@gmail.com",
    "password": "testpassword"
}

payload_for_invalid_case = {
    "password": "testpassword"
}

payload_for_valid_case = {
    "email": "arthasthelichking@gmail.com",
    "password": "testpassword"
}


def create_payload(name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, 
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

# API 2: POST To All Products List

def test_Post_All_Products_List():
    response = requests.post(products_endpoint)
    json_response = json.loads(response.text)
    assert json_response["responseCode"] == 405

# API 5: POST To Search Product

def test_Post_To_Search_Product():
    try:
        response = requests.post(search_endpoint, data=payload_for_search)
        response.raise_for_status()
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert response.status_code == 200
    assert 'responseCode' in json_response
    assert json_response['responseCode'] == 200

# API 6: POST To Search Product without search_product parameter

def test_Post_To_Search_Product_without_parameter():
    try:
        response = requests.post(search_endpoint)
        response.raise_for_status()
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert response.status_code == 200
    assert 'responseCode' in json_response
    assert json_response['responseCode'] == 400

# API 7: POST To Verify Login with invalid details

def test_Post_To_Verify_Login_with_invalid_details():
    try:
        response = requests.post(verify_login_endpoint, data=payload_for_verify)
        response.raise_for_status()
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert response.status_code == 200
    assert 'message' in json_response
    assert json_response['message'] == "User not found!"

# API 8: POST To Verify Login without email parameter

def test_Post_To_Verify_Login_without_email_parameter():
    try:
        response = requests.post(verify_login_endpoint, data=payload_for_invalid_case)
        response.raise_for_status()
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert response.status_code == 200
    assert 'message' in json_response
    assert json_response['message'] == "Bad request, email or password parameter is missing in POST request."

# API 10: POST To Verify Login with valid details

def test_Post_To_Verify_Login_with_valid_details():
    try:
        response = requests.post(verify_login_endpoint, data=payload_for_valid_case)
        response.raise_for_status()
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert response.status_code == 200
    assert 'message' in json_response
    assert json_response['message'] == "User exists!"

# API 11: POST To Create/Register User Account

    payload_to_register_account = create_payload("gregorythetailor", "gregoryflask@gmail.com", "gogonono", 
                                                 "Mr", "13", "October", "1984", "Gregory", "Flask", "Loar Ltd.", 
                                                 "1748 Irving Road", "1430 Eagle Drive", "United States", "45701", "Ohio", "Athens",
                                                 "740-517-0014")
    try:
        response = requests.post(create_account_endpoint, data=payload_to_register_account)
        response.raise_for_status()
        json_response = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, f"Request failed: {e}"
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        assert False, f"JSON decoding failed: {e}"
    assert response.status_code == 200
    assert 'message' in json_response
    assert json_response['message'] == "User created!" or json_response['message'] == "Email already exists!"
