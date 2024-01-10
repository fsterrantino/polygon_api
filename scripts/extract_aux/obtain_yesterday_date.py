from datetime import timedelta

def obtain_yesterday_date(execution_date):
    yesterday_date = execution_date - timedelta(days=1)
    formatted_yesterday_date = yesterday_date.strftime('%Y-%m-%d')
    return formatted_yesterday_date