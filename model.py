from pydantic import BaseModel, Field, field_validator
import re

class User(BaseModel):
    id: int
    name: str

class Userr(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    feedback: str = Field(alias="message")

class Feeedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    feedback: str = Field(alias="message",  min_length=10, max_length=500)

    @field_validator("feedback")
    def validate_feedback(cls, value):
        patterns = [r"кринж..", r"вайб..", "рофл.."]
        for pattern in patterns:
            if re.search(pattern, value):
                raise ValueError("Использование недопустимых слов")
        return value