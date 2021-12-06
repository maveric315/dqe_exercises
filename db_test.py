import pytest
import pymssql
from queries import *


@pytest.fixture(scope='module')
def db_start_stop():
    """Connects to db before tests, disconnects after tests."""
    # Setup : start db
    conn = pymssql.connect(host='host.docker.internal', user='testuser', password='testpassword',
                           database='AdventureWorks2012', port='65134')
    global cursor
    cursor = conn.cursor()

    yield

    # Teardown : stop db
    conn.close()


@pytest.mark.aw2012
def test_min_value_of_column(db_start_stop):
    """ Verifies min value of column 'StateProvinceID' in table '[Person].[Address]'.
    Expected result: 1.
    """
    print('\n', test_min_value_of_column.__doc__)
    column_min = get_min_value_of_column(cursor, table_name='[Person].[Address]', column_name='StateProvinceID')
    assert column_min == 1, "The minimal value of column 'StateProvinceID' in table '[Person].[Address]' " \
                            "is different from the expected."


@pytest.mark.aw2012
def test_max_value_of_column(db_start_stop):
    """ Verifies max value of column 'StateProvinceID' in table '[Person].[Address]'.
    Expected result: 181.
    """
    print('\n', test_max_value_of_column.__doc__)
    column_max = get_max_value_of_column(cursor, table_name='[Person].[Address]', column_name='StateProvinceID')
    assert column_max == 181, "The maximal value of column 'StateProvinceID' in table '[Person].[Address]' " \
                              "is different from the expected."


@pytest.mark.aw2012
def test_average_value_of_column(db_start_stop):
    """ Verifies average value of column 'ChangeNumber' in table '[Production].[Document]'.
    Expected result: 35.
    """
    print('\n', test_average_value_of_column.__doc__)
    column_avg = get_average_value_of_column(cursor, table_name='[Production].[Document]', column_name='ChangeNumber')
    assert column_avg == 35, "The average value of column 'ChangeNumber' in table '[Production].[Document]' " \
                             "is different from the expected."


@pytest.mark.aw2012
def test_count_of_null_values_for_column(db_start_stop):
    """ Verifies count of null values for column 'DocumentSummary' in table '[Production].[Document]'.
    Expected result: 8.
    """
    print('\n', test_count_of_null_values_for_column.__doc__)
    column_count = get_count_of_null_values_for_column(cursor, table_name='[Production].[Document]',
                                                       column_name='DocumentSummary')
    assert column_count == 8, "The count of null values for column 'DocumentSummary' " \
                              "in table '[Production].[Document]' is different from the expected."


@pytest.mark.aw2012
def test_count_for_column(db_start_stop):
    """ Verifies count for column 'UnitMeasureCode' in table '[Production].[UnitMeasure]'.
    Expected result: 38.
    """
    print('\n', test_count_for_column.__doc__)
    column_count = get_count_for_column(cursor, table_name='[Production].[UnitMeasure]', column_name='UnitMeasureCode')
    assert column_count == 38, "The actual count result for column 'UnitMeasureCode' " \
                               "in table '[Production].[UnitMeasure]' is different from the expected."


@pytest.mark.aw2012
def test_count_of_not_null_values_for_column(db_start_stop):
    """ Verifies count of not null values for column 'Name' in Table '[Production].[UnitMeasure]'.
    Expected result: 38.
    """
    print('\n', test_count_of_not_null_values_for_column.__doc__)
    column_count = get_count_of_not_null_values_for_column(cursor, table_name='[Production].[UnitMeasure]',
                                                           column_name='Name')
    assert column_count == 38, "The count of not null values for column 'Name' in table '[Production].[UnitMeasure]' " \
                               "is different from the expected."
