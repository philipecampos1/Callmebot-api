import requests
import hide


class Callmebot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = hide.api_whatsapp
        self.__my_number = hide.my_number

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__my_number}&text={message}&apikey={self.__api_key}'
        )
        return response.text
