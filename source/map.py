# Plot sample data on a map with GeoJSON

from geojson import dumps

from parse import parse, MY_FILE

def create_map(parsed_data):
   """Create a GeoJSON file"""
   
   # Define type of GeoJSON we are creating
   
   
   # Define empty list to collect graph points
   
   
   # Iterate to create GeoJSON dobcument
   
   
       # Skip any zero coordinates (these are problematic)
       
       
       # Setup a new dictionary for each iteration
       
       
       # Assign line items to appropriate GeoJSON fields
       
       
       # Add data dictionary to our item_list
       
   # Add each point in our item_list to our dictionary
   
   # Write GeoJSON to a file for upload to gist.github.com

def main():
    data_file = parse(MY_FILE, ",")
if __name__ == "__main__":
    main()