from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Employee(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)
    title: str = Field(..., min_length=1)
    email: EmailStr

class UpdateEmployee(BaseModel):
    age: Optional[int] = Field(None, gt=0)
    title: Optional[str] = Field(None)
    email: Optional[EmailStr] = Field(None)
