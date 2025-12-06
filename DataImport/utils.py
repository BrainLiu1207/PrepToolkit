def import_to_db_with_fast_executemany(df, schema_name, table_name, engine):
    column_list_string = ','.join([f'[{x}]' for x in df.columns])
    question_mark_string = ','.join(['?' for _ in df.columns])
    connection = engine.raw_connection()
    cursor = connection.cursor()
    cursor.fast_executemany = True 
    
    insert_string = f'insert into {schema_name}.{table_name} ' + \
        f'({column_list_string} values ({question_mark_string}))'
        
    cursor.executemany(insert_string, df.values.tolist())
    cursor.commit()
    cursor.close()
    connection.close()