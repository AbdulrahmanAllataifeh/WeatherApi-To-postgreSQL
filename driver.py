from weathersearch import WeatherSearch
from auth import api_key
from queries import insert_weather_table
from dbdriver import DatabaseDriver
import argparse


parser = argparse.ArgumentParser(
        description="A hourly weather report based on parameters city and date")


def to_string(data):
    return [str(value) for value in data.values()]

def main():
    args = parser.parse_args()
    b = WeatherSearch(date=args.date,city=args.city)
    db = DatabaseDriver()
    db.setup()

    queries = [insert_weather_table.format(*to_string(result)) for result in b.get_results()]
    query_to_execute = "BEGIN; \n" + '\n'.join(queries) + "\nCOMMIT;"
    db.execute_query(query_to_execute)

if __name__ == "__main__":
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-d", "--date",  metavar='', required=True,
                          help="Search Date, for example \"2024-05-27\" or \"2024-05-26\" and up to a year.")
    optional.add_argument("-c", "--city", metavar='', required=False, default='Dubai',
                          help="Search City Default: Dubai")

    main()