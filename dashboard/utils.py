import locale
from datetime import datetime, timedelta

def set_locale():
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except locale.Error:
        pass  # Fail silently if locale not supported

def get_today_date():
    return datetime.now()

def get_yesterday_date():
    return datetime.now() - timedelta(days=1)

def format_date(date_obj):
    return date_obj.strftime('%d de %B')
