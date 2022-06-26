from typing import Iterable, Optional

import requests

from src.atl_adjuster.itad_api_classes import APIGetPlain, Lowest, Plain


class API(APIGetPlain):
    base_url_v1: str = 'https://isthereanydeal.com/api/v01/game/'
    base_url_v2: str = 'https://isthereanydeal.com/api/v02/game/'
    default_params: dict[str, str]

    def __init__(self, api_key: str) -> None:
        self.default_params = {'key': api_key}

    def get_plain(self,
                  shop: Optional[str] = None,
                  game_id: Optional[str] = None,
                  game_name: Optional[str] = None) -> Plain:
        url = f'{self.base_url_v2}plain/'
        params = self.default_params
        if shop is not None and game_id is not None:
            params |= {'shop': shop, 'game_id': game_id}
        if game_name is not None:
            params |= {'title': game_name}
        response = requests.get(url, params=params)
        return Plain(**response.json())

    def get_lowest(self,
                   plains: Iterable[str] | str,
                   country: str = 'US',
                   shops: Iterable[str] | str = 'steam') -> Lowest:
        url = f'{self.base_url_v1}lowest/'
        plains_str = ','.join(plains) if type(plains) == Iterable else plains
        shops_str = ','.join(shops) if type(shops) == Iterable else shops
        params = self.default_params | {
            'plains': plains_str,
            'country': country,
            'shops': shops_str
        }
        response = requests.get(url, params=params)
        return Lowest(**response.json())

    def get_plain_name_for_game_by_steam_id(self, game_id: str) -> str:
        return self.get_plain(shop='steam', game_id=game_id).data.plain

    def get_plain_name_for_game_by_name(self, game_name: str) -> str:
        return self.get_plain(game_name=game_name).data.plain
