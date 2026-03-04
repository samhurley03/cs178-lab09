# read_movies.py
# Reads all items from the DynamoDB Movies table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Movies"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(movie):
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")
    runtime = movie.get("Runtime (Hours)", "Unknown Runtime")

    print(f"  Title   : {title}")
    print(f"  Year    : {year}")
    print(f"  Ratings : {ratings}")
    print(f"  Runtime : {runtime}")
    print()

# adding a random comment to test git
# and another one!!

def get_movie_by_title():
    """Prompt user for a movie title and search the table."""
    table = get_table()
    
    title_input = input("Enter movie title: ").strip()
    
    response = table.scan(
        FilterExpression=Attr("Title").eq(title_input)
    )
    
    items = response.get("Items", [])
    
    if not items:
        print("\nMovie not found.\n")
    else:
        print("\nMovie found:\n")
        for movie in items:
            print_movie(movie)


def print_all_movies():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No movies found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} movie(s):\n")
    for movie in items:
        print_movie(movie)


def main():
    print("===== Reading from DynamoDB =====\n")
    
    print_all_movies()
    
    print("===== Search for a Movie =====\n")
    get_movie_by_title()


if __name__ == "__main__":
    main()