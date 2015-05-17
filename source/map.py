# Plot sample data on a map with GeoJSON

from geojson import dumps

from parse import parse, MY_FILE

def create_map(parsed_data):
   """Create a GeoJSON file"""
   
   # Define type of GeoJSON we are creating
   geo_map = {"type": "FeatureCollection"}
   
   # Define empty list to collect graph points
   points_list = []
   
   # Iterate to create GeoJSON dobcument
   # enumerate() gives us the index as well which is the line number
   for index, line in enumerate(parsed_data): 
   
       # Skip any zero coordinates (these are problematic)
       if line['X'] == "0" or line['Y'] == "0":
           continue
       
       # Setup a new dictionary for each iteration
       data = {}
       
       # Assign line items to appropriate GeoJSON fields
       data["type"] = "Feature"
       data["id"] = index
       data["properties"] = {"title": line["Category"],
                             "description": line["Descript"],
                             "date": line["Date"]}
       
       data["geometry"] = {"type": "Point",
                           "coordinates":(line['X'], line['Y'])}
       
       # Add data dictionary to our points_list
       points_list.append(data)
       
   # Add each point in our points_list to our geomap dictionary
   for point in points_list:
       # setdefault() creates a key caled "features" whose default value is an empty list
       # we add each point to this list to get our list of features
       geo_map.setdefault("features", []).append(point)
       
   # Write GeoJSON to a file for upload to gist.github.com
   with open("file_sf.geojson", "w") as f: # with automatically closes f
       # dumps() prints the dictionary into a GeoJSON recognisable file
       f.write(dumps(geo_map)) 

def main():
    data_file = parse(MY_FILE, ",")
    return create_map(data_file)
    
if __name__ == "__main__":
    main()