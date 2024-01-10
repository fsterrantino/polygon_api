def insert_df_into_db(df, engine):
    try:
        df.to_sql('stocks_data', engine, index=False, if_exists='append')
        print("Data inserted into Redshift table successfully!")

    except Exception as e:
        raise print("Error inserting data into Redshift:", e)