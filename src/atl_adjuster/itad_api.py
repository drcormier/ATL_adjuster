from typing import Iterable

import requests

from src.atl_adjuster.itad_api_classes import Plain, Lowest


class API:
    base_url_v1: str = 'https://isthereanydeal.com/api/v01/game/'
    base_url_v2: str = 'https://isthereanydeal.com/api/v02/game/'
    default_params: dict[str, str]

    def __init__(self, api_key: str) -> None:
        self.default_params = {'key': api_key}

    def get_plain(self, game_name: str) -> Plain:
        url = f'{self.base_url_v2}plain/'
        params = self.default_params | {'title': game_name}
        response = requests.get(url, params=params)
        return Plain(**response.json())

    def get_lowest(self, plains: Iterable[str], country: str = 'US', shops: Iterable[str] = ['steam']) -> Lowest:
        # sourcery skip: default-mutable-arg
        url = f'{self.base_url_v1}lowest/'
        params = self.default_params | {
            'plains': ','.join(plains),
            'country': country,
            'shops': ','.join(shops)
        }
        response = requests.get(url, params=params)
        return Lowest(**response.json())
