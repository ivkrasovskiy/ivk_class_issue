import json
from issue import Advert, Json_parserMixin, ColorizeMixin

class_objects = (
    """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25",
    "metro_stations": ["Спортивная", "Гагаринская"]
      }
    }""",
    """{
      "title": "Вельш-корги",
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25",
        "metro_stations": ["Спортивная", "Гагаринская"]
      }
    }""",
    """{
      "title": "Вельш-корги",
      "price": 10000,
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25",
        "metro_stations": ["Спортивная", "Гагаринская"]
      }
    }""",
    """{
      "title": "Вельш-корги",
      "price": -100,
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25",
        "metro_stations": ["Спортивная", "Гагаринская"]
      }
    }""")


# ----------------------------------------------------------------------------------------------------------------------
for i, class_object in enumerate(class_objects):
    corgi_dict = json.loads(class_object)
    corgi_adv = Advert(corgi_dict)
    print(f'Test{i}:\nrepr: {corgi_adv}, address: {corgi_adv.location.metro_stations}'
          f', corrected price: {corgi_adv.price}, class: {corgi_adv.class_},')
    print(corgi_adv)
