from django.apps import AppConfig


class FlightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flights'

class TicketsConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'tickets'

class RoutesConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'routes'

class AirportsConfig(AppConfig):
                default_auto_field = 'django.db.models.BigAutoField'
                name = 'airports'
