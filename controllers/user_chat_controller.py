from fastapi import APIRouter
from typing import Literal
from models.chat_validation_models import SessionRequest
from models.message_validation_models import MessageValidation
from source.user_chat_source import UserSessionStorage
user_chat=APIRouter()

user_obj=UserSessionStorage()
@user_chat.post('/sessions',status_code=201)
def store_new_user_chat(new_chat:SessionRequest):
    response=user_obj.store_new_user_session(new_chat.model_dump_json())
    return response

@user_chat.post('/sessions/{session_id}/messages',status_code=200)
def add_messages_to_session(session_id:int,messages:MessageValidation):
    response=user_obj.store_session_messages(session_id,messages.model_dump_json())
    return response

@user_chat.get('/sessions/{session_id}/messages')
def get_messages_per_session(session_id:int,role:Literal['user','assistant']=None):
    response= user_obj.get_messages(session_id,role)
    return response