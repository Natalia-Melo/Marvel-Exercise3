import requests
import json
import hashlib

# Requests input from the user
character_name = input('Please state name of the character: ')


#Requesting API information
public_key = '5af6d4a87ce76ae3171db660e48ed1db'
private_key = '45b56518f41ced2d5ad2fb507e885ca4ccb51de1'
ts = '5'

# Create hash
hashkey = hashlib.md5()
hashkey.update(f'{ts}{private_key}{public_key}'.encode())
hashed = hashkey.hexdigest()

# Only domain and path for the request.get
r = requests.get('http://gateway.marvel.com/v1/public/characters' + '?' +'name=' + character_name +'&ts=' + ts +'&apikey=' +
                   public_key + '&hash=' + hashed)

r_json = r.json()

results = r_json['data']['results']

