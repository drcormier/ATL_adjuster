from pydantic import BaseModel, Field


class MetaPlain(BaseModel):
    """
    Class for the MetaPlain model
    """
    match: str
    active: bool


class DataPlain(BaseModel):
    """
    Class for the DataPlain model
    """
    plain: str


class Plain(BaseModel):
    """
    Class for the Plain model
    """
    data: DataPlain
    meta: MetaPlain = Field(alias='.meta')


class MetaLowest(BaseModel):
    """
    Class for the MetaLowest model
    """
    currency: str


class ShopLowest(BaseModel):
    """
    Class for the ShopLowest model
    """
    id: str
    name: str


class UrlsLowest(BaseModel):
    """
    Class for the UrlsLowest model
    """
    game: str
    history: str


class GameLowest(BaseModel):
    """
    Class for the GameLowest model
    """
    shop: ShopLowest
    price: float
    cut: int
    added: int
    urls: UrlsLowest


class Lowest(BaseModel):
    """
    Class for the Lowest model
    """
    data: dict[str, GameLowest]
    meta: MetaLowest = Field(alias='.meta')
