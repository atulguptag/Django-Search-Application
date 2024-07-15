import csv
import os
import django
from restaurant.models import Dish

def setup_django_environment():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_search.settings')
    django.setup()

setup_django_environment()

def load_data_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            restaurant_name = row[1]
            restaurant_location = row[2]
            items_data_string = row[3]
            restaurant_lat_long = row[4]

            # Extract dish information from the dictionary within "items" (if present)
            if items_data_string:
                try:
                    items_data = eval(items_data_string) # Data is a dictionary string
                    for item_name in items_data.items():
                       
                        Dish.objects.update_or_create(
                            name=item_name,
                            location=restaurant_location,
                            lat_long=restaurant_lat_long,
                        )
                except (NameError, SyntaxError):
                    print(f"Error processing items data for restaurant: {restaurant_name}")

load_data_from_csv('csv_file_path/restaurants_small.csv')





# import sqlite3
# import pandas as pd

# df = pd.read_csv('CSV_FILE/restaurants_small.csv')

# df.columns = df.columns.str.strip()

# connection = sqlite3.connect('db.sqlite3')

# df.to_sql('restaurant_dish', connection, if_exists='replace')

# connection.close()