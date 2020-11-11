"""
comics
characters
creators
events
stories
series
"""

from marvel import api

import random 

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

def _unique_names(all_names):
    return list(set(all_names))
   
def split_name(name):
    # we take a name string and we split into a list of name strings
    # by spliting on the spaces
    raw_names = name.split(" ")
    # we use a list comprehension to clean up unwanted characters
    # from each of the names
    return [p.replace("(", "").replace(")", "") for p in raw_names]

def split_names(list_of_names):
    # return [split_name(name) for name in list_of_names]
    all_names = []
    for full_name in list_of_names:
        # short names looks like this: ["daken"]
        short_names = split_name(full_name)
        for short_name in short_names:
            # short name looks like this: "daken"
            all_names.append(short_name)
            # all names looks like this: [daken]
    return all_names

def random_character_name(character_resp):
    full_names = character_names(character_resp)
    short_names = split_names(full_names)
    uniques = _unique_names(short_names)
    new_name_parts = random.choices(uniques, k=2)
    new_name = " ".join(new_name_parts)
    return new_name
    