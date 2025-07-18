import json
from helpers.custom_helpers import utc_time_calculator
from loguru import logger
from core.exceptions import SessionNotFound


class UserSessionStorage:
    def __init__(self):
        self.chat_storage = {}
        self.session_storage = []

    def store_new_user_session(self, session_chat):
        session_id = str(len(self.session_storage) + 1)
        current_time = utc_time_calculator()
        session_chat_json = json.loads(session_chat)
        db_payload = {"session_id": session_id, "created_at": current_time,
                      "session_user": session_chat_json.get("session_user")}
        self.session_storage.append(db_payload)
        logger.debug(f"{self.session_storage=}")
        self.chat_storage[int(session_id)] = []
        logger.debug(f"{self.chat_storage=}")
        return db_payload


    def store_session_messages(self, session_id: int, messages):
        messages_json = json.loads(messages)
        if session_id in self.chat_storage:
            self.chat_storage[session_id].append(messages_json)
            logger.debug(f"{self.chat_storage=}")
            return {"message": "messages added to the session successfully!"}
        else:
            raise SessionNotFound("Session ID not Found!")

    def get_messages(self, session_id, role):
        if session_id in self.chat_storage:
            if role:
                result = [user_chat for user_chat in self.chat_storage[session_id] if role==user_chat["role"]]
                return result
            return self.chat_storage[session_id]
        else:
            raise SessionNotFound("Session ID not Found!")
