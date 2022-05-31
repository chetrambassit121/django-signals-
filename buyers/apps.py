from django.apps import AppConfig


class BuyersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buyers'

    def ready(self):                                               # setting up buyers app with the signals file 
        import buyers.signals









# from django.apps import AppConfig


# class BuyersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'buyers'

    
