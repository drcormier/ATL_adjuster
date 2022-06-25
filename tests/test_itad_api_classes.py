import unittest
from src.atl_adjuster.itad_api_classes import Plain, Lowest


class PlainTester(unittest.TestCase):
    def test_plain(self):
        data = {
            ".meta": {
                "match": "title",
                "active": True
            },
            "data": {
                "plain": "roguetower"
            }
        }
        Plain(**data)


class LowestTest(unittest.TestCase):
    def test_lowest(self):
        data = {
            ".meta": {
                "currency": "USD"
            },
            "data": {
                "roguetower": {
                    "shop": {
                        "id": "steam",
                        "name": "Steam"
                    },
                    "price": 11.99,
                    "cut": 20,
                    "added": 1651512112,
                    "urls": {
                        "game": "https:\/\/isthereanydeal.com\/game\/roguetower\/info\/",
                        "history": "https:\/\/isthereanydeal.com\/game\/roguetower\/history\/"
                    }
                }
            }
        }
        Lowest(**data)


if __name__ == '__main__':
    unittest.main()
