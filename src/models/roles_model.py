from pydantic import BaseModel


class Role(BaseModel):
    ID: str
    name: str
    description: str
    permissions: list[str]


class RoleList(BaseModel):
    roles: list[Role]
