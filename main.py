from fastapi import FastAPI,Request
from core.exceptions import SessionNotFound
from fastapi.responses import JSONResponse
from controllers.user_chat_controller import user_chat
app = FastAPI(
    title="AI_CHAT_APP", openapi_url="/openapi.json"
)
@app.exception_handler(SessionNotFound)
async def exception_handler(request: Request, exc:SessionNotFound):
    return JSONResponse(
        status_code=404,
        content={"message": f"{exc}"},
    )


app.include_router(user_chat)
