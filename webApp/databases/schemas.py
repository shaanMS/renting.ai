from pydantic import BaseModel, Field


class SearchRequest(BaseModel):

    query: str = Field(
        min_length=2,
        max_length=100
    )


class PropertyResponse(BaseModel):

    property_id: str
    property_type: str
    purpose: str
    city: str
    area_name: str
    bedrooms: int
    rent: int
    description: str