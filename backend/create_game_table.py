###################################################################
# Create the table for game data
###################################################################
import boto3


###################################################################
# Define constants
###################################################################
endpoint_url = "http://localhost:8000"
endpoint_url = None


###################################################################
# Helper functions
###################################################################
def create_game_data_table(dynamodb=None):
    global endpoint_url
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

    table = dynamodb.create_table(
        TableName='game_details',
        KeySchema=[{
            'AttributeName': 'play_date', 'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {'AttributeName': 'play_date', 'AttributeType': 'N'}],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


###################################################################
# MAIN PROGRAM
###################################################################
if __name__ == '__main__':
    game_data_tbl = create_game_data_table()
    status = game_data_tbl.table_status
    print(f"Table status: {status}")
