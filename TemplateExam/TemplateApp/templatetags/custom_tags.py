from django import template
from datetime import datetime
import math

register = template.Library()


@register.filter(name='caliculate_date_time_to_now')
def cariculate_datetime_to_now(value):
    join_datetime = datetime.strptime(value, '%Y/%m/%d')
    now_datetime = datetime.now()

    diff_datetime = now_datetime - join_datetime
    diff_days = diff_datetime.days
    diff_years = math.floor(diff_days / 365)
    diff_moth = math.floor((diff_days - 365*diff_years)/30)
    return f'{diff_years}年{diff_moth}ヶ月'
