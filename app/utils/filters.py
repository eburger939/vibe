


def format_date(date):
    return date.strftime('%m/%d/%y')


def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

from datetime import datetime
print(format_date(datetime.now()))