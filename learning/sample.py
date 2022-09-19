import os
import time
import traceback

from sqlalchemy import create_engine, text

host = os.getenv('WEB_MYSQL_HOST', 'localhost')
port = os.getenv('WEB_MYSQL_PORT', 3306)
user = os.getenv('WEB_MYSQL_USER', 'root')
pwd = os.getenv('WEB_MYSQL_PWD', 'root')
count = int(os.getenv('WEB_LOOP_COUNT', 10000))

url = f'mysql+mysqldb://{user}:{pwd}@{host}:{port}/mysql'
print(url)
engine = create_engine(url, echo=True)
conn1 = None
b = True
while b and count > 0:
    try:
        conn1 = engine.connect()
        res = conn1.execute(text('select * from user limit 1'))
        result = [{k: v for k, v in i._mapping.items()} for i in res]
        print(result)
        b = False
    except Exception as e:
        traceback.print_exception(e)
        time.sleep(10)
        count -= 1
    finally:
        if conn1:
            conn1.close()
'''
输出

[{'Host': '%', 'User': 'fruit', 'Select_priv': 'N', 'Insert_priv': 'N', 'Update_priv': 'N', 'Delete_priv': 'N', 'Create_priv': 'N', 'Drop_priv': 'N', 'Reload_priv': 'N', 'Shutdown_priv': 'N', 'Process_priv': 'N', 'File_priv': 'N', 'Grant_priv': 'N', 'References_priv': 'N', 'Index_priv': 'N', 'Alter_priv': 'N', 'Show_db_priv': 'N', 'Super_priv': 'N', 'Create_tmp_table_priv': 'N', 'Lock_tables_priv': 'N', 'Execute_priv': 'N', 'Repl_slave_priv': 'N', 'Repl_client_priv': 'N', 'Create_view_priv': 'N', 'Show_view_priv': 'N', 'Create_routine_priv': 'N', 'Alter_routine_priv': 'N', 'Create_user_priv': 'N', 'Event_priv': 'N', 'Trigger_priv': 'N', 'Create_tablespace_priv': 'N', 'ssl_type': '', 'ssl_cipher': b'', 'x509_issuer': b'', 'x509_subject': b'', 'max_questions': 0, 'max_updates': 0, 'max_connections': 0, 'max_user_connections': 0, 'plugin': 'mysql_native_password', 'authentication_string': '*A4B6157319038724E3560894F7F932C8886EBFCF', 'password_expired': 'N', 'password_last_changed': datetime.datetime(2022, 9, 19, 7, 31, 34), 'password_lifetime': None, 
'account_locked': 'N', 'Create_role_priv': 'N', 'Drop_role_priv': 'N', 'Password_reuse_history': None, 'Password_reuse_time': None, 'Password_require_current': None, 'User_attributes': None}]
'''
