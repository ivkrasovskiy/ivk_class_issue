from typing import Dict, NoReturn
from keyword import iskeyword


class Json_parserMixin:
    @staticmethod
    def keyword_renaming(mapping: Dict) -> NoReturn:
        keys_set = set(mapping.keys())
        for old_key in keys_set:
            if iskeyword(old_key):
                mapping[old_key + '_'] = mapping.pop(old_key)

    def __init__(self, mapping):
        self.keyword_renaming(mapping)
        self.__dict__ = mapping


class ColorizeMixin:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f'\033[0;{self.color};0m '

    repr_color_code = 33  # yellow


class Advert(Json_parserMixin, ColorizeMixin):
    repr_color_code = 32  # green

    def __init__(self, mapping):
        if 'price' in mapping:
            mapping['_price'] = mapping.pop('price')
        else:
            mapping['_price'] = 0
        super().__init__(mapping)

        if "location" in self.__dict__:
            self.location = Json_parserMixin(self.location)

        self.color = super().repr_color_code

    def __repr__(self):
        return super().__repr__() + f'{self.title} | {self.price} ₽\033[0m]'

    @property
    def price(self):
        if self._price >= 0:
            return self._price
        else:
            raise ValueError('must be >= 0')
