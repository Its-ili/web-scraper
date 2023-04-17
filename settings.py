# settings.py

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

CONCURRENT_REQUESTS = 10

DOWNLOAD_DELAY = 0.5

RETRY_TIMES = 3

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

ITEM_PIPELINES = {
    '<project_name>.pipelines.<pipeline_name>': 300,
}

FEED_FORMAT = 'csv'
FEED_URI = 'output.csv'
