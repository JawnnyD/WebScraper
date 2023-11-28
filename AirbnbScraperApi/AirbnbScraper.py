from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_XItzitHPaZDpsWJ9VvW9Q8oyOfNA5h2HQxDg")

# get input from user about what to search for
location = input("Enter location: \n")
limit = int(input("How many would you like to see: "))
check_in = input("Enter check-in date(Ex: 2024-01-01): \n")
check_out = input("Enter check-out date(Ex: 2024-01-01): \n")
numBedrooms = int(input("Enter number of bedrooms: \n"))
numBeds = int(input("Enter number of beds: \n"))
numBathrooms =int(input("Enter number of bathrooms: \n"))
numReviews = int(input("Enter number of reviews you want: \n"))

# Prepare the Actor input
run_input = {
    "location": location,
    "limit" : limit,
    "check_in": check_in,
    "check_out": check_out,
    "bedrooms": numBedrooms,
    "beds" : numBeds,
    "bathrooms" : numBathrooms,
    "reviews" : numReviews
}

# Run the Actor and wait for it to finish
run = client.actor("viXne7lpALg8viFdh").call(run_input=run_input)

dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items

# overwrites existing file, print formatting line
with open("Airbnb.txt", "w") as text_file:
    print("----------------------------------------------------------------------------------------------------------p", file=text_file)

# iterate through collected data, set variables to wanted information
for item in dataset_items:
    if('name' in item):
        name = item['name']
    else:
        name = "unknown"

    if('location' in item):
        location = item['location']

        if('country' in location):
            country = location['country']
        else:
            country = "unknown"
        if('city' in location):
            city = location['city']
        else:
            city = "unknown"
        if('state' in location):
            state = location['state']
        else:
            state = "unknown"        
    else:
        country = "unknown"
        city = "unknown"
        state = "unknown"
    
    if('capacity' in item):
        capacity = item['capacity']
        if('bathrooms' in capacity):
            bathrooms = capacity['bathrooms']
        else:
            bathrooms = "unknown"
        
        if('bedrooms' in capacity):
            bedrooms = capacity['bedrooms']
        else:
            bedrooms = "unknown"
    else:
        bathrooms = "unknown"
        bedrooms = "unknown"

    if('context' in item):
        context = item['context']

        if('checkin' in context):
            checkin = context['checkin']
        else:
            checkin = "unknown"
        if('checkout' in context):
            checkout = context['checkout']
        else:
            checkout = "unknown"
    else:
        checkin = "unknown"
        checkout = "unknown"

    if('pricing_quote' in item):
        pricing = item['pricing_quote']
        if('primary' in pricing):
            primary = pricing['primary']

            if('price' in primary):
                price = primary['price']
            else:
                price = "unknown"      
        else:
            price = "unknown"
    else:
            price = "unknown"
    
    if('reviews' in item):
        reviews = item['reviews']
        comments = ""

        if('items' in reviews):
            items = reviews['items']

            for review in items:
                if('comments' in review):
                    comments += review['comments'] + "\n"
    else:
        comments = ""

    if('url' in item):
        url = item['url']
    else:
        url = "unknown"

    # open file for appending, append information into text file with wanted formatting
    with open("Airbnb.txt", "a") as text_file:
        print(f"Name: {name}", file=text_file)
        print(f"Country: {country}", file=text_file)
        print(f"City: {city}", file=text_file)
        print(f"State: {state}\n", file=text_file)
        print(f"Number of bathrooms: {bathrooms}", file=text_file)
        print(f"Number of bedrooms: {bedrooms}\n", file=text_file)
        print(f"Check-in: {checkin}", file=text_file)
        print(f"Check-out: {checkout}\n", file=text_file)
        print(f"Price: {price}\n", file=text_file)
        print(f"Comments:\n{comments}", file=text_file)
        print(f"URL: {url}", file=text_file)
        print("----------------------------------------------------------------------------------------------------------", file=text_file)
