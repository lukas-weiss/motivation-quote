import json
import os.path
import logging
import csv
from random import randint

logger = logging.getLogger()
logger.setLevel(logging.INFO)
def get_quote(file):
    if os.path.exists(file):
        with open(file) as csvfile:
            quotes = list(csv.reader(csvfile, delimiter=';'))
            max_quotes = len(quotes) - 1
            rand_quotes_idx = randint(0, max_quotes)
            logger.debug(quotes[rand_quotes_idx])
            return quotes[rand_quotes_idx]
    else:
        logger.info(file + " not found")


def lambda_handler(event, context):
    # logger.debug(context.aws_request_id)
    quote_entry = get_quote("quotes.csv")
    logger.debug(quote_entry)
    quote = ""
    author = ""
    if quote_entry is not None:
        quote = quote_entry[0]
        author = quote_entry[1]
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "quote": quote,
            "author": author
        }),
    }
