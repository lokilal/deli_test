from datetime import datetime

import requests


def get_time_context_processor(request):
    response = requests.post('https://api.taxideli.ru/test/gettime')
    date = datetime.fromtimestamp(response.json()['dataAns']/1000)
    print(date)
    return {'hi': date}
