'''
Utils module.
'''
import requests

def register(name: str) -> str: 
    response = requests.post("127...../register_player/"+name)
    json_response = response.json()
    player_id = json_response         # TODO: implement API call
    return player_id


def is_my_turn(player_id: str) -> bool:

    my_turn = True          # TODO: implement API call
    return my_turn

