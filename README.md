# market2

for adding new alarm run py manage.py runserver and for sending them run alert/alarming.py
views are not successfully made so create user and alart from django admin panel, create a superuser first and then go on.

next steps are:
  * making better views for watching your alarms, editing them, deleting them and view just "your" alarms.
  * make a function that if price was in requested range, update interval to 10 minute and if price come out of range make it back to 1 minute.

coinmarketcap api does not supported less than 60 second interval api calls so be carefull what interval you set
