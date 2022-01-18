from typing import Optional

from pydantic import BaseModel, validator


class VkJokesParams(BaseModel):
    """Validates and limits input parameters:
    "count" for number of jokes
    "lang" for language selection
    """

    count: int
    lang: Optional[str]

    @validator("count")
    def is_in_range(cls, value):
        if value not in range(1, 11):
            raise ValueError("Out of range! Try 1 to 10.")
        return value

    # language selection validation limited to 4 languages
    @validator("lang")
    def language_validator(cls, value):
        language_selection = ["pl", "lt", "da", "ru", "lv"]
        if value.lower() not in language_selection:
            raise ValueError(
                f"Wrong input! Please type one of the following {language_selection}"
            )
        return value.lower()
