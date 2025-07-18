from pydantic import BaseModel, Field, field_validator


class SessionRequest(BaseModel):
    session_user: str = Field(min_length=1)

    @field_validator('session_user')
    def name_must_contain_space(cls, v):
        if not v.strip():
            raise ValueError('Must not be a space')
        return v.strip().lower()