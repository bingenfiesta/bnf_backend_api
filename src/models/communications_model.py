from pydantic import BaseModel


class CommunicationTemplate(BaseModel):
    ID: str
    type_of_communication: str
    template: str
    photos: list[str]


class CommunicationsList(BaseModel):
    communications: list[CommunicationTemplate]
