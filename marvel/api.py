from time import time as now 

import os
import hashlib
import requests

_PUB_KEY = os.getenv("MARVEL_API_PUBLIC_KEY")
if _PUB_KEY is None:
    raise Exception("environment variable MARVEL_API_PUBLIC_KEY is required")
_PRIV_KEY = os.getenv("MARVEL_API_PRIVATE_KEY")
if _PRIV_KEY is None:
    raise Exception("environment variable MARVEL_API_PRIVATE_KEY is required")
BASE_URL = "http://gateway.marvel.com/v1/public/"

def _timestamp():
    right_now = now() * 10_000_000
    return int(right_now)

def _generate_hash(ts, priv_key, pub_key):
    hash_input = str(ts) + priv_key + pub_key 
    hash_result = hashlib.md5(hash_input.encode("utf-8"))
    hash_output = hash_result.hexdigest()
    return hash_output

def _generate_url(relpath):
    ts = _timestamp()
    api_key = _PUB_KEY
    hash_value = _generate_hash(ts, _PRIV_KEY, _PUB_KEY)
    query = "?ts=" + str(ts) + "&apikey=" + api_key + "&hash=" + hash_value
    url = BASE_URL + relpath + query
    return url

def get(relpath):
    url = _generate_url(relpath)
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"get failed with response code {response.status_code}")
    body = response.json()
    return body


