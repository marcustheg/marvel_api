"""
comics
characters
creators
events
stories
series
"""

from marvel import api

def get_character_by_name(name):
    return api.get("characters", params={"name": name})

def character_name(character):
    results = get_results(character)
    return results[0]["name"]

def get_characters_by_series(series):
    return api.get("characters", params={"series": series})
    
def get_results(response_body):
    return response_body["data"]["results"]
