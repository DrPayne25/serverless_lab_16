from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path 
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if 'pokemon' in dic:
      url = 'https://pokeapi.co/api/v2/pokemon-species/'
      r = requests.get(url + dic['pokemon'])
      data = r.json()
      pokemon_list = []
      for pokemon_data in data:
        pokemon = pokemon_data['flavor_text_entries'][0]['flavor_text'][0]
        pokemon_list.append(pokemon)
      message = str(pokemon_list)
    else:
      message = "Please give me a pokemon to lookup"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return
