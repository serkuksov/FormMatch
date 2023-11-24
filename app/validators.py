from datetime import date, datetime
from typing import Any

from phonenumbers import NumberParseException
from pydantic import BaseModel, ValidationError, EmailStr, field_validator
import phonenumbers


class ValidateEmail(BaseModel):
    value: EmailStr

    def __str__(self):
        return "email"


class ValidatePhoneNumber(BaseModel):
    value: str

    @field_validator("value", mode="before")
    @classmethod
    def parse_phone_number(cls, value):
        try:
            phone_number = phonenumbers.parse(str(value), "RU")
        except NumberParseException:
            return None
        national_number = phone_number.national_number
        if national_number and len(str(national_number)) == 10:
            return f"+7{phone_number.national_number}"

    def __str__(self):
        return "phone"


class ValidateDate(BaseModel):
    value: date

    @field_validator("value", mode="before")
    @classmethod
    def parse_date(cls, value):
        try:
            return datetime.strptime(str(value), "%d.%m.%Y").date()
        except ValueError:
            pass
        try:
            return datetime.strptime(str(value), "%Y-%m-%d").date()
        except ValueError:
            pass

    def __str__(self):
        return "date"


class ValidateString(BaseModel):
    value: str

    @field_validator("value", mode="before")
    @classmethod
    def parse_string(cls, value):
        return str(value)

    def __str__(self):
        return "string"


class ValidateParameters:
    validators = (
        ValidateEmail,
        ValidatePhoneNumber,
        ValidateDate,
        ValidateString,
    )

    def __init__(self, parameters: dict[str, Any]):
        self.parameters = parameters

    def get_type_parameters(self) -> dict[str, str]:
        """Возвращает словарь параметров с их типами"""
        type_parameters = {}
        for key, value in self.parameters.items():
            type_parameters[key] = str(self._get_type_value(value))
        return type_parameters

    def _get_type_value(self, value: Any) -> BaseModel:
        """Возвращает тип параметра"""
        for validator in self.validators:
            try:
                type_parameter = validator(value=value)
                return type_parameter
            except ValidationError:
                continue
        raise ValueError(f"Тип параметра {value} не определен")
