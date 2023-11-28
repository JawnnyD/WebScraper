from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_XItzitHPaZDpsWJ9VvW9Q8oyOfNA5h2HQxDg")

# get input from user about what to search for
location = input("Enter location: \n")
limit = int(input("Enter limit of results you would like to receive: \n"))
sort = input("Enter how you want it sorted(relevance, change, newest, price_high, price_low, beds, baths, living_area, lot_area, year_built): \n")
search_type = input("Enter search type(sell, sold, rent): \n")

# Prepare the Actor input
run_input = {
    "location": [location],
    "limit": limit,
    "sort": sort,
    "search_type": search_type,
}

# Run the Actor and wait for it to finish
run = client.actor("7H3vXS9NiRVfdcMpI").call(run_input=run_input)

dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items

print(dataset_items)

# overwrites existing file, print formatting line
with open("Housing.txt", "w") as text_file:
    print("----------------------------------------------------------------------------------------------------------", file=text_file)

# iterate through collected data, set variables to wanted information
for item in dataset_items:
    if('address' in item):
        address = item['address']

        if('streetAddress' in address):
            streetAdress = address['streetAddress']
        else:
            streetAdress = "unknown"
        if('zipcode' in address):
            zipcode = address['zipcode']
        else:
            zipcode = "unknown"
        if('city' in address):
            city = address['city']
        else:
            city = "unknown"
        if('state' in address):
            state = address['state']
        else:
            state = "unknown"        
    else:
        streetAdress = "unknown"
        zipcode = "unknown"
        city = "unknown"
        state = "unknown"
    

    if('bathrooms' in item):
        bathrooms = item['bathrooms']
    else:
        bathrooms = "unknown"
    
    if('bedrooms' in item):
        bedrooms = item['bedrooms']
    else:
        bedrooms = "unknown"
    

    if('daysOnZillow' in item):
        daysOnZillow = item['daysOnZillow']
    else:
        daysOnZillow = "unknown"

    if('datePostedString' in item):
        datePosted = item['datePostedString']
    else:
        datePosted = "unknown"
    
    if('price' in item):
        price = item['price']
        if('value' in price):
            value = price['value']
        else:
            value = "unknown"
        if('pricePerSquareFoot' in price):
            pricePerSquareFt = price['pricePerSquareFoot']
        else:
            pricePerSquareFt = "unknown"
    else:
        value = "unknown"
        pricePerSquareFt = "unknown"

    if('affordabilityEstimate' in item):
        affordabilityEstimate = item['affordabilityEstimate']

        if('totalMonthlyCost' in affordabilityEstimate):
            totalMonthlyCost = affordabilityEstimate['totalMonthlyCost']
        else:
            totalMonthlyCost = "unknown"
    else:
        totalMonthlyCost = "unknown"

    if('url' in item):
        url = item['url']
    else:
        url = "unknown"

    # open file for appending, append information into text file with wanted formatting
    with open("Housing.txt", "a") as text_file:
        print(f"Street Address: {streetAdress}", file=text_file)
        print(f"Zipcode: {zipcode}", file=text_file)
        print(f"City: {city}", file=text_file)
        print(f"State: {state}\n", file=text_file)
        print(f"Number of bathrooms: {bathrooms}", file=text_file)
        print(f"Number of bedrooms: {bedrooms}\n", file=text_file)
        print(f"Date Posted: {datePosted}", file=text_file)
        print(f"Days on Zillow: {daysOnZillow}\n", file=text_file)
        print(f"Price: {value}", file=text_file)
        print(f"Price per sq ft: {pricePerSquareFt}", file=text_file)
        print(f"Total Monthly Cost: {totalMonthlyCost}\n", file=text_file)
        print(f"URL: {url}", file=text_file)
        print("----------------------------------------------------------------------------------------------------------", file=text_file)


