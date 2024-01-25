create table if not exists stocks_data (
  ticker VARCHAR(4),
  volume FLOAT,
  volume_weighted_avg_price FLOAT,
  open_price FLOAT,
  close_price FLOAT,
  highest_price FLOAT,
  lowest_price FLOAT,
  transactions_number FLOAT,
  datetime timestamp without time zone,
  extraction_date date,
  load_date date
)