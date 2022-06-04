import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market2.settings')
import django
django.setup()
from django.core.mail import send_mail
from market2.settings import EMAIL_HOST_USER
from users.models import NewUser
from alert.models import Alert
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from requests import Request, Session
import json
import pprint


url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'e2c50768-59f3-46ff-a09b-94026cdfa15c'
}

session = Session()
session.headers.update(headers)


#sched = BlockingScheduler()


#@sched.scheduled_job('interval', minutes=1)
def get_price():


    alert_list = Alert.objects.all().values()
    #user_list = NewUser.objects.all().values()
    for i in alert_list:
        if i['status'] == 'active':
            coin = i['symbol']
            user_id = i['author_id']
            mail = 'mahdivafaii1999@gmail.com'
            mail = NewUser.objects.get(id=user_id).email
            parameters = {
                'symbol': f'{coin}',
                'convert': 'USD',
            }
            response = session.get(url, params=parameters)
            result = json.loads(response.text)['data'][f'{coin}'][0]['quote']['USD']['price']
            if i['low_price'] < result < i['high_price']:
                subject = f'Update in {coin} price'
                message = f'Current {coin} price is {result}'
                recepient = f'{mail}'
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

get_price()
