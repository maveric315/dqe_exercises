""" The module contains functions, that perform queries to db.
:param cursor: a cursor object, that is used to make queries and fetch results from the database,
see https://www.pymssql.org/ref/pymssql.html#pymssql.Connection.cursor for details,
:param table_name: table name,
:param column_name: column name,
:return: result of the query.
"""


def get_count_for_column(cursor, table_name, column_name):
    cursor.execute('SELECT COUNT(' + column_name + ') AS COUNT FROM ' + table_name + ';')
    return cursor.fetchall()[0][0]


def get_average_value_of_column(cursor, table_name, column_name):
    cursor.execute('SELECT AVG(' + column_name + ') FROM ' + table_name + ';')
    return cursor.fetchall()[0][0]


def get_min_value_of_column(cursor, table_name, column_name):
    cursor.execute('SELECT MIN(' + column_name + ') FROM ' + table_name + ';')
    return cursor.fetchall()[0][0]


def get_max_value_of_column(cursor, table_name, column_name):
    cursor.execute('SELECT MAX(' + column_name + ') FROM ' + table_name + ';')
    return cursor.fetchall()[0][0]


def get_sum_of_column(cursor, table_name, column_name):
    cursor.execute('SELECT SUM(' + column_name + ') FROM ' + table_name + ';')
    return cursor.fetchall()[0][0]


def get_count_of_null_values_for_column(cursor, table_name, column_name):
    cursor.execute('SELECT COUNT(*) FROM ' + table_name + ' WHERE ' + column_name + ' IS NULL;')
    return cursor.fetchall()[0][0]


def get_count_of_not_null_values_for_column(cursor, table_name, column_name):
    cursor.execute('SELECT COUNT(*) FROM ' + table_name + ' WHERE ' + column_name + ' IS NOT NULL;')
    return cursor.fetchall()[0][0]
