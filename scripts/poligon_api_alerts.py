from scripts.load_aux.read_df import read_df
from scripts.extract_aux.obtain_yesterday_date import obtain_yesterday_date
from scripts.alert_aux.send_email import send_email

def alert_thresholds_gaps(**kwargs):
    execution_date = kwargs.get('execution_date')
    formatted_yesterday_date = obtain_yesterday_date(execution_date)

    df = read_df('normal', formatted_yesterday_date)

    percentage_increase_threshold = 1.8
    percentage_decrease_threshold = -2

    # Calculate the percentage change within each ticker
    df['percentage_change'] = df.groupby('ticker')['close_price'].pct_change() * 100
    
    # Create a column indicating whether the current row exceeded the threshold. gt method compares for equal or greater than, and lt for lower.
    df['exceeded'] = df['percentage_change'].gt(percentage_increase_threshold) | df['percentage_change'].lt(percentage_decrease_threshold)
    
    # Filter the rows that exceeded and the ones inmediately above them. No need to write '==' because their True or False.
    filtered_df = df[df['exceeded'] | df['exceeded'].shift(-1)]

    if not filtered_df.empty:
        formatted_yesterday_date = formatted_yesterday_date.replace('.', '-')
        filtered_df.to_csv('/opt/archives/' + 'alerted_stocks - ' + formatted_yesterday_date + '.csv')
        print('Archive generated Ok.')

        send_email(filtered_df)
        
    else:
        print('No alerts found.')