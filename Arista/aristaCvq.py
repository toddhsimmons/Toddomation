# Enjoy this Toddomation

import requests
import json
from decouple import config

BASE_URL = config("BASE_URL")
TYPE = config("TYPE")
KEY_ID = config("KEY_ID")
KEY_VALUE = config("KEY_VALUE")
TIMEOUT = config("TIMEOUT")
CLIENT_IDENTIFIER = config("CLIENT_IDENTIFIER")


def getCookie():
    url = f"{BASE_URL}/session"

    payload = json.dumps(
        {
            "type": TYPE,
            "keyId": KEY_ID,
            "keyValue": KEY_VALUE,
            "timeout": TIMEOUT,
            "clientIdentifier": CLIENT_IDENTIFIER,
        }
    )
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    cookie = response.cookies["JSESSIONID"]

    return cookie


def getSession(cvcue_cookie):
    url = f"{BASE_URL}/session"

    payload = json.dumps({})
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"JSESSIONID={cvcue_cookie}",
        "Version": "10",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def getLocations(cvcue_cookie):
    url = f"{BASE_URL}/locations"

    payload = json.dumps({})
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"JSESSIONID={cvcue_cookie}",
        "Version": "11",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def getAps(cvcue_cookie):
    url = f"{BASE_URL}/manageddevices/aps?active=true&startindex=0&pagesize=1000"

    payload = json.dumps({})
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"JSESSIONID={cvcue_cookie}",
        "Version": "15",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def getClients(cvcue_cookie):
    url = f"{BASE_URL}/clients?activestatus=true&startindex=0&pagesize=1000"

    payload = json.dumps({})
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"JSESSIONID={cvcue_cookie}",
        "Version": "12",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
