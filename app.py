import json
import os
import pymysql

def lambda_handler(event, context):
    try:
        # Connect using the environment variables
        connection = pymysql.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            database=os.environ['DB_NAME']
        )
        
        # Run a test query to get the MySQL version
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(f'Success! Connected to RDS MySQL version: {db_version[0]}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(f'Database connection failed: {str(e)}')
        }
