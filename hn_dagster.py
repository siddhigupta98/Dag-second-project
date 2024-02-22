from one import extract, transform, load
from dagster import asset

@asset
def hackernews_wordcloud():
    input = extract()
    output = transform(input)
    load(output)
    
    
from dagster import RetryPolicy


# @asset(retry_policy=RetryPolicy(max_retries=5, delay=5))
# def hackernews_wordcloud():
#     input = extract()
#     output = transform(input)
#     load(output)