from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_XItzitHPaZDpsWJ9VvW9Q8oyOfNA5h2HQxDg")

# Prepare the Actor input
run_input = {
    "location": ["New York"],
    "limit": 5,
    "sort": "newest",
    "search_type": "sell",
}
# Run the Actor and wait for it to finish
run = client.actor("7H3vXS9NiRVfdcMpI").call(run_input=run_input)

dataset_items = client.dataset(run['defaultDatasetId']).list_items().items

print(dataset_items)