#Task 1: Flight Route Comparison
#Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Define the sets of flight destinations for both airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Find destinations that both airlines fly to
common_destinations = our_routes & competitor_routes

# Find destinations unique to your airline
unique_our_routes = our_routes - competitor_routes

# Find destinations unique to the competitor airline
unique_competitor_routes = competitor_routes - our_routes

# Find destinations that neither airline shares
all_destinations = our_routes | competitor_routes
neither_shared = all_destinations - (our_routes & competitor_routes)

# Print the results
print("Destinations both airlines fly to:", common_destinations)
print("Destinations unique to our airline:", unique_our_routes)
print("Destinations unique to competitor airline:", unique_competitor_routes)
print("Destinations neither airline shares:", neither_shared)


#Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.


def remove_duplicates(customer_ids):
    # Convert the list to a set to remove duplicates
    unique_customer_ids = set(customer_ids)
    return unique_customer_ids