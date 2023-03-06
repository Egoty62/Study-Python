from analysis import series
from crawling.parser import parser_test
from database.connection import connection_test

if __name__ == '__main__' :
    series.series_test()
    parser_test()
    connection_test()