###################################################################
# Bulk loader of raw game data
###################################################################
from decimal import Decimal
import json
import boto3
from botocore.exceptions import ClientError

###################################################################
# Define constants
###################################################################
endpoint_url = "http://localhost:8000"
endpoint_url = None


###################################################################
# Helper classes
###################################################################
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o)
        return super(DecimalEncoder, self).default(o)


###################################################################
# Helper functions
###################################################################
def get_game(date, dynamodb=None):
    # Configure dynamo connection
    global endpoint_url
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url=endpoint_url)

    # Grab the table and fix the input
    table = dynamodb.Table('game_details')
    play_date = int(date)
    item = {}

    try:
        response = table.get_item(Key={'play_date': play_date})
        item = response.get("Item", {})
    except ClientError as e:
        print(e.response['Error']['Message'])
    
    return item


def game_to_str(game: dict):
    return json.dumps(game, cls=DecimalEncoder)


###################################################################
# MAIN PROGRAM
###################################################################
if __name__ == '__main__':
    date_str = "20210524"
    game = get_game(date_str)
    obj = game_to_str(game)
