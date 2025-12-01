from datetime import date, timedelta

def get_week_start():
    today = date.today()
    start = today - timedelta(days=today.weekday())  # Monday
    return start.isoformat()

def get_month_start():
    today = date.today()
    return today.replace(day=1).isoformat()
