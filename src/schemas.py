from pydantic import BaseModel, validator
from typing import Optional

class MultipleJokesRequestParams(BaseModel):
    count: int
    language: Optional[str]

    @validator('count')
    def is_in_range(cls, value):
        if value not in range(1,11):
            raise ValueError("Out of range! Try 1 to 10.")
        return value

    #language selection validation limited to 4 languages
    @validator('language')
    def language_validator(cls, value):
        language_selection = ['pl','lt','da','ru']
        if value.lower() not in language_selection:
            raise ValueError("Wrong input! Please type 'pl' for Polish,'lt' for Lithuanian, 'da' for Danish or 'ru' for Russian")
        return value.lower()