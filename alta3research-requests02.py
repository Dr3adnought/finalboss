#!/usr/bin/env python3
"""-----FINAL PROJECT: FLASK API (Jeffrey Lee)-----"""
"""--- this file to show proficiency with Requests ---"""


import requests
from pprint import pprint
URL = "http://localhost:5000/"

resp = requests.get(URL).json()

print(resp)
