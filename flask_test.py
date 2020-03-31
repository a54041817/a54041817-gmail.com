from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from linebot import LineBotApi,WebhookParser,WebhookHandler
from flask import Flask, request, abort
from linebot.models import *
import os
from django.views.decorators.csrf import csrf_exempt
from linebot.exceptions import (
    InvalidSignatureError
)
app = Flask(__name__)
TOKEN="6EIQ0qOrSCgGBqvgiOXW+oJVgfouREp9LkvIpXz/go2CiFzQdjS7h7f/H/JB3RqMJQq4u1istZYhVnJCziX3IagBWglkdbe8WXOIN8amy2Gz+5+FAhzYlNbXV5r8LDm83HvUkCbrg4FRi27iyAsVuQdB04t89/1O/w1cDnyilFU="
SECRET="e8519daf3649e52fb64e22914e9ffe88"
line_bot_api = LineBotApi(TOKEN)
handler = WebhookHandler(SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent)
def handle_message(event):
    import BotSay as by


    line_bot_api.reply_message(event.reply_token,by.main(event.message.text))

                            
@app.route('/')
def homepage():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])