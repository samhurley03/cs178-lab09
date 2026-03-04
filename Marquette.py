# read_marquette.py
# Reads all items from the DynamoDB Marquette table

import boto3

REGION = "us-east-1"
TABLE_NAME = "Marquette"


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_player(player):
    name = player.get("Player Name", "Unknown")
    number = player.get("Number", "Unknown")
    position = player.get("Position", "Unknown")

    print(f"  Name     : {name}")
    print(f"  Number   : {number}")
    print(f"  Position : {position}")
    print()


def print_all_players():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No players found.")
        return

    print(f"Found {len(items)} player(s):\n")
    for player in items:
        print_player(player)


def main():
    print("===== Marquette Roster =====\n")
    print_all_players()


if __name__ == "__main__":
    main()