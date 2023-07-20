from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent,
    StickerSendMessage, ImageSendMessage, LocationSendMessage,
    TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackAction,
    PostbackEvent, FlexSendMessage, QuickReplyButton, QuickReply, ConfirmTemplate, MessageAction
)

line_bot_api = LineBotApi('2YjwKF4Yc0OAPL7UYf+v4eanzNIT2QolotvesvIB3TKvaMkuY8/9DC9yT/vtIowHrcKoLseqn+5e96t5UEFKK3VTkAk4xFVweCr5hNwJhMsyqVaNXuslAOCEoziWoEv0vK7ya0WEyyu2wvHg+Tsw+gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('834cfe72d9c4fb61d7bfab4e3546b16e')