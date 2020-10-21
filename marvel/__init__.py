"""
comics
characters
creators
events
stories
series
"""

from marvel import api

def get_characters_by_series(series):
    return api.get("characters", params={"series": series})

def get_character_by_name(name):
    return api.get("characters", params={"name": name})

def character_name(character_resp):
    # return character["data"]["results"][0]["name"]
    results = get_results(character_resp)
    return results[0]["name"]
    
def get_results(character_resp):
    return character_resp["data"]["results"]

def character_names(character_resp):
    results = get_results(character_resp)
    return [character["name"] for character in results]

SAMPLE_NAMES = ['Daken',
 'Dark Avengers',
 'Hulk',
 'Sentry (Robert Reynolds)',
 'She-Hulk (Jennifer Walters)',
 'She-Hulk (Lyra)',
 'Thundra']

def split_name(name):
    raw_names = name.split(" ")
    return [p.replace("(", "").replace(")", "") for p in raw_names]

def split_names(list_of_names):
    return [name for name in list_of_names]
    