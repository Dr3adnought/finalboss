#!/usr/bin/env python3
import requests
from pprint import pprint

URL = "http://localhost:5000/"

resp = requests.get(URL).json()

pprint(resp)
