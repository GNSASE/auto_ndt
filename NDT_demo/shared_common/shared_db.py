#!python

import MySQLdb
from django.conf import settings # import the settings file

# Import database configuration settings from django settings file.
_db = settings.DATABASES['default']

def db_connect():
    # Open database connection
    db = MySQLdb.connect(_db['HOST'],
                         _db['USER'],
                         _db['PASSWORD'],
                         _db['NAME'])
    return db

def search_ndt(pid):
    """
    This database call will return True with data if existing ndt record is found or
    false if no data is returned.
    """
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT pid,scale_unit FROM ndt_index WHERE pid = '{}'".format(pid))

    # Fetch one row using fetchone() method.
    data = cursor.fetchone()

    # disconnect from server
    db.close()
    # return results back to caller
    return data

def create_ndt(pid,scale_unit):
    """
    This database insert will attempt to insert a new record to the ndt_index table.
    """
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("""INSERT INTO ndt_index (pid, scale_unit) VALUES('{}','{}')""".format(pid,
                                                                                              scale_unit))

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchall()

    # disconnect from server
    db.close()
    # return results back to caller
    return data

def delete_ndt(pid):
    """
    This database call will delete an ndt entry from the ndt_index table based upon the
    pid provided by the user.
    """
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("DELETE FROM ndt_index WHERE pid = "'{}'"".format(pid))

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchall()

    # disconnect from server
    db.close()
    # return results back to caller
    return data

def fetch_xml_template(scale_unit):
    """
    This database call will query the scale_unit_index table within the database and
    return back the filename for the scale unit xml ndt template.
    """
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT xml_template_filename FROM scale_unit_index WHERE scale_unit = '{}'".format(scale_unit))

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchone()

    # disconnect from server
    db.close()
    # return results back to caller
    return data

def fetch_base_standard_url(scale_unit):
    """
    This database call will query the scale_unit_index table within the database and
    return back the url for the scale unit xml ndt template.
    """
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT network_standard_url FROM scale_unit_index WHERE scale_unit = '{}'".format(scale_unit))

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchone()

    # disconnect from server
    db.close()
    # return results back to caller
    return data

def fetch_scale_unit():
    """
    This database call will return the scale unit values currently stored in the database.
    """
    results = []
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT scale_unit FROM scale_unit_index")

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchall()
    for row in data:
        results.append(row[0])

    # disconnect from server
    db.close()
    # return results back to caller
    return results

def insert_form_key_value(pid, scale_unit, key, value):
    """
    This database call will insert/update form gathered key/value data into the ndt_form_data table.
    """
    results = []
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("REPLACE INTO ndt_form_data (pid, scale_unit, data_key, data_value) VALUES ('{}', '{}', '{}', '{}')".format(pid,
                                                                                                                               scale_unit,
                                                                                                                               key,
                                                                                                                               value))

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchall()
    for row in data:
        results.append(row[0])

    # disconnect from server
    db.close()
    # return results back to caller
    return results

def fetch_ndt_form_data(pid):
    """
    This database call will return the key/value pairs gathered from the dynamic user form for the specific PID requested.
    """
    # prepare a cursor object using cursor() method
    db = db_connect()
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM ndt_form_data")

    # Fetch all row(s) using fetchall() method.
    data = cursor.fetchall()

    # disconnect from server
    db.close()
    # return results back to caller
    return data