from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import json
from random import choice

from app.color_blind_html import generate_html, landing_page
from app.notifier import Notifier

with open('all_combinations.json', 'r') as f:
    all_combinations = json.load(f)


notifier = Notifier()

origins = ["*"]

app = FastAPI(title='game_table', 
        redoc_url='/game_table/docs',
        openapi_url='/game_table/openapi.json')


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ws_type, ws = ['ws', 'ws://127.0.0.1:8080/notsober/ws']
# ws_type, ws = ['wss', 'wss://gametable-xolpakqy5q-ez.a.run.app/notsober/wss']

@app.get("/color_blind", response_class=HTMLResponse)
async def read_item():

    return landing_page(ws)


@app.get("/notsober/{winning_color}", response_class=HTMLResponse)
async def read_item(request: Request, winning_color: str):

    if winning_color not in all_combinations.keys():
        raise HTTPException(status_code=404, detail=f"Supported colors: {list(all_combinations.keys())}")

    html = generate_html(*choice(all_combinations[winning_color]))
    await notifier.push(html) 

@app.websocket(f"/notsober/{ws_type}")
async def websocket_endpoint(websocket: WebSocket):
    await notifier.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except WebSocketDisconnect:
        notifier.remove(websocket)

@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await notifier.generator.asend(None)