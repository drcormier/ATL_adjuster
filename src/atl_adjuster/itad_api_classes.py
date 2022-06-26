"""
This module contains the underlying classes used to interact with the ITAD API,
including:
    - Pydantic models for the JSON data returned by the API
    - Interfaces for the ITAD API
"""
import re
from abc import ABC, abstractmethod
from typing import Iterable

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


class APIGetLowest(ABC):
    """
    Interface defining a method for getting the lowest price of a game
    """

    def get_lowest_price_for_game(self,
                                  plain_name: str,
                                  lowest: Lowest) -> float:
        return lowest.data[plain_name].price

    def get_lowest_price_for_games(self,
                                   plain_names: Iterable[str],
                                   lowest: Lowest) -> Iterable[float]:
        return (lowest.data[plain_name].price for plain_name in plain_names)


class APIGetPlain(ABC):
    """
    Interface defining a method for getting the plain name of a game
    """
    id_pattern = re.compile(
        r'^https://store\.steampowered\.com/(\w+?/\d+?)/\w+/?$'
    )

    @abstractmethod
    def get_plain_name_for_game_by_name(self, game_name: str) -> str:
        pass

    def get_plain_name_for_game_by_steam_url(self, game_url: str) -> str:
        """
        Converts a Steam URL to a Steam ID and then calls
        get_plain_name_for_game_by_steam_id
        """
        return self.get_plain_name_for_game_by_steam_id(
            self.steam_url_to_steam_id(game_url)
        )

    @abstractmethod
    def get_plain_name_for_game_by_steam_id(self, game_id: str) -> str:
        pass

    def steam_url_to_steam_id(self, steam_url: str) -> str:
        """
        Converts a Steam URL to a Steam ID
        """
        match self.id_pattern.match(steam_url):
            case match if isinstance(match, re.Match):
                return match.group(1)
            case None:
                raise ValueError(
                    f'Could not convert Steam URL "{steam_url}" to Steam ID'
                )
        raise ValueError(
            f'Could not convert Steam URL "{steam_url}" to Steam ID'
        )
