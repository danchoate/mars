###################################################################
# Bulk loader of raw game data
###################################################################
from decimal import Decimal
import json
import os
import boto3

###################################################################
# Define constants
###################################################################
endpoint_url = "http://localhost:8000"
endpoint_url = None


###################################################################
# Helper functions
###################################################################
def add_game(file_path, table):
    with open(file_path) as json_file:
        game_details = json.load(json_file, parse_float=Decimal)
        play_date = game_details["date"].replace("-", "")
        game_details["play_date"] = int(play_date)
        print(f"Adding game from: {play_date}")
        table.put_item(Item=game_details)


###################################################################
# MAIN PROGRAM
###################################################################
if __name__ == '__main__':
    # Start by creating a dynamo db instance and grabbing the table
    dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
    table = dynamodb.Table('game_details')

    # Now determine all the files in the directory
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, "data")
    file_list = os.listdir(data_dir)
    json_files = [x for x in file_list if x.endswith(".json")]

    # Filter to files we care about
    json_files = [
        "game_log_2022_04_04.json", "game_log_2022_04_23.json",
        "game_log_2022_05_02.json", "game_log_2022_05_16.json",
        "game_log_2022_06_13.json"
    ]

    # Loop through each file
    for file_name in json_files:
        file_path = os.path.join(data_dir, file_name)
        if os.path.isfile(file_path):
            add_game(file_path, table)
