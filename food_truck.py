from email.policy import default
from textwrap import indent
from venv import EnvBuilder
from xmlrpc.client import DateTime
from redis_om import (EmbeddedJsonModel, Field, JsonModel)
from pydantic import PositiveInt
from typing import Optional, List

class Event(EmbeddedJsonModel):
    assignedVendors: PositiveInt = Field(index=True)
    endTime: DateTime = Field(index=True)
    startTime: DateTime = Field(index=True)
    locationId: str = Field(index=True)
    locationName: str = Field(index=True)
    name: str = Field(index=True)


class Info(EmbeddedJsonModel):
    address: str = Field(index=True)
    city: str = Field(index=True)
    coordinates: str = Field(index=True)
    region: str = Field(index=True)
    state: str = Field(index=True)
    zipcode: str = Field(index=True)

class Location(EmbeddedJsonModel):
    about: str = Field(index=True, full_text_search=True)
    imageUrl: str = Field(index=True)

    info: Info
    locationType: str = Field(index=True)
    name: str = Field(index=True, full_text_search=True)


class Vendor_Info(EmbeddedJsonModel):
    address: str = Field(index=True, full_text_search=True)
    city: str = Field(index=True, full_text_search=True)
    state: str = Field(index=True, full_text_search=True)
    
class Vendor(EmbeddedJsonModel):
    bannerUrl: Optional[str] = Field(index=False)
    cuisines: list = Field(index=True, full_text_search=True, default=['none', 'no'])
    events: list = Field(index=True, full_text_search=True, default=['none', 'no'])
    bannerUrl: Optional[str] = Field(index=False)
    id: str = Field(index=False)
    logoUrl: Optional[str] = Field(index=False)
    name: str = Field(index=True, full_text_search=True)
    primary_cuisine: str = Field(index=True, full_text_search=True)
    vendor_info = Vendor_Info
