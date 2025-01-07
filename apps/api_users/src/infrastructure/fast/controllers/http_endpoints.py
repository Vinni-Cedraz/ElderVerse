HTTP_ENDPOINTS = {
    "USERS": {
        "REGISTER": "/users/register",
        "PROFILE": {
            "GET": "/users/{id}",
            "UPDATE": "/users/{id}/update",
            "CHANGE_PASSWORD": "/users/{id}/password",
        },
    },
    "AUTH": {
        "LOGIN": "/auth/login",
        "LOGOUT": "/auth/logout",
    },
    "ELDERS": {
        "GIFT_CARDS": {
            "GENERATE": "/elders/gift_cards/generate",
            "GET": "/elders/gift_cards/{id}",
            "GET_ALL": "/elders/gift_cards",
            "DELETE": "/elders/gift_cards/{id}",
        },
    },
    "HEALTH": {
        "MAIN": "/health",
        "NATS": "/health/nats",
    },
}
