from clients.conversor_service import ConversorService
from clients.callmebot_service import Callmebot

conversor_service = ConversorService()
conversion = conversor_service.converter('GBP', 'BRL')

wpp_service = Callmebot()
wpp_service.send_message(
    message=f'Cotacao do GBP: £{round(float(conversion), 2)}'
    )


print(conversion)
