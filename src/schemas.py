from typing import Optional

from pydantic import BaseModel, validator


class VkJokesParams(BaseModel):
    count: int
    lang: Optional[str]

    @validator("count")
    def is_in_range(cls, value: int):
        if value not in range(1, 11):
            raise ValueError("Out of range! Try 1 to 10.")
        return value

    # language selection validation limited to 4 languages
    @validator("lang")
    def language_validator(cls, value: str):
        language_selection = ["pl", "lt", "da", "ru", "tr"]
        if value.lower() not in language_selection:
            raise ValueError(
                "Wrong input! Please type 'pl' for Polish,'lt' for Lithuanian, 'da' for Danish or 'ru' for Russian"
            )
        return value.lower()
