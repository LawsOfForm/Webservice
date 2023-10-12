#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""html form webservice"""

import json
import os
from http import HTTPStatus
import urllib.request     #neu
import urllib.parse
import logging
import sys
import pandas as pd

from aiohttp import web

SERVER_ADDRESS = (os.environ.get("HOST", ""), int(os.environ.get("PORT", 4785)))
#change directory for script
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")


async def post_handler(request):
    """
    Coroutine given to the server, st. it knows what to do with an HTTP request.

    This one handles a POST, checks its content, and forwards it to the matrix room.
    
   
    """
    data = await request.read()
    content_type = request.content_type or guess_content_type(data)
    if content_type == "application/x-www-form-urlencoded":
        try:
            #urllib.request.urlretrieve("http://localhost:8080/Fragebogen_VerFlu_test.html", "test.txt")
            #data = urllib.parse.parse_qs(data, strict_parsing=True, max_num_fields=1000000)
            data = urllib.parse.parse_qs(data.decode(), strict_parsing=True, max_num_fields=1000000)
             #max_num_fields=n give correct number alle item otherwise "500 Internal Server error)	
            data = {key: value[0] for key, value in data.items()}
            
        except ValueError as e:
            logging.error(f"Invalid urlencoded data: {e}\n" + data)
            return create_json_response(
                HTTPStatus.BAD_REQUEST, "Invalid urlencoded data"
            )
    else:
        try:
            #data = json.loads(data)
            data = json.loads(data)
            
        except json.decoder.JSONDecodeError as e:
            logging.error(f"Invalid json: {e}\n" + data)
            return create_json_response(HTTPStatus.BAD_REQUEST, "Invalid JSON")

    train = pd.DataFrame.from_dict(data, orient='index')
    train.reset_index(level=0, inplace=True)
    
    if train['index'].iloc[5]=='Aktiv':
    	order='postscan'
    else:	
    	order='prescan'
    print('Daten:',data)
    print('ID:',train[0].iloc[3])
    print('ses:',train[0].iloc[4])
    print('All',train)    
    json.dump(data, open("%s_ses-%s_%s_survey.json" %(train[0].iloc[3], train[0].iloc[4],order),"w"), ensure_ascii=False)
    # do something with data here see aiohttp


    return create_json_response(HTTPStatus.OK, "OK")
    #return   aiohttp 

def create_json_response(status, ret):
    """Create a JSON response."""
    response_data = {"status": status, "ret": ret}
    return web.json_response(response_data, status=status)


def guess_content_type(payload: str) -> str:
    """Based on the payload, guess the content type.

    Either application/json or application/x-www-form-urlencoded."""
    if payload.startswith("{"):
        return "application/json"
    return "application/x-www-form-urlencoded"


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(
        [web.post("/", post_handler), web.static("/", path=STATIC_DIR, show_index=True)]
    )
    web.run_app(app)
