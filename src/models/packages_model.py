from pydantic import BaseModel


class Package(BaseModel):
    ID: str
    name: str
    description: str
    photo: str
    video: str
    price: float
    theatre_id: str
    decoration_id: str
    addon_id: str
    addon_options: list[str]
    # conditions: list[str]


class PackagesList(BaseModel):
    packages: list[Package]
