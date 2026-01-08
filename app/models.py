from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class ProfileBase(BaseModel):
    email: EmailStr
    display_name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    date_of_birth: Optional[str] = Field(default=None, description="YYYY-MM-DD")
    height_cm: Optional[int] = None
    weight_kg: Optional[float] = None
    preferred_activity_time: Optional[str] = Field(default=None, description="Morning/Afternoon/Evening/Night")
    preferred_language: Optional[str] = None
    unit_system_code: Optional[str] = Field(default="ME", description="ME or IM")

class ProfileCreate(ProfileBase):
    username: str

class ProfileUpdate(BaseModel):
    display_name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    date_of_birth: Optional[str] = None
    height_cm: Optional[int] = None
    weight_kg: Optional[float] = None
    preferred_activity_time: Optional[str] = None
    preferred_language: Optional[str] = None
    unit_system_code: Optional[str] = None

class ProfileSummary(BaseModel):
    username: str
    email: str
    display_name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    date_of_birth: Optional[str] = None
    height_cm: Optional[int] = None
    weight_kg: Optional[float] = None
    preferred_activity_time: Optional[str] = None
    preferred_language: Optional[str] = None
    unit_system_name: str
    created_at_utc: str
    updated_at_utc: str
    preferred_activities: str
