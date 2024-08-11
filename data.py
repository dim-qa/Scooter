METHOD_CODE = [
    {'login': 'api/v1/courier/login', 'OK': 200, 'Bad Request': 400, 'Not Found': 404},
    {'create': 'api/v1/courier', 'Created': 201, 'Bad Request': 400, 'Conflict': 409},
    {'delete': 'api/v1/courier/', 'OK': 200, 'Bad Request': 400, 'Not Found': 404},
    {'create_buy': '/api/v1/orders', 'Created': 201},
    {'get_buy': '/api/v1/orders/track?t=', 'Bad Request': 400, 'Not Found': 404}
]
BUY_BLACK = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
BUY_GREY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GREY"
    ]
}
BUY_BLACK_AND_GREY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK",
              "GREY"
              ]
}
BUY_NOT_COLOUR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
              ]
}
