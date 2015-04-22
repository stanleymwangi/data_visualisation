# Parse sample SF crime data from a CSV file
import csv # obtain the csv module so that we can read csv files

MY_FILE="../data/sample_sfpd_incident_all.csv" # global variable MY_FILE holds data location


def parse(raw_file, delimeter):
    """Parses a raw CSV file to a JSON-like object."""
    
    # Open CSV file
    opened_file = open(raw_file)
    
    # Read CSV file
    csv_data = csv.reader(opened_file, delimeter=delimeter) # csv_data is a generator
    
    # Build a data structure to return parsed data
    parsed_data = [] # setup an empty list
    
    fields = csv_data.next() # get column headers on first row
    
    # loop over the rows in csv_data
    for row in csv_data:
        # append dictionary of each row after mapping corresponding header and value
        parsed_data.append(dict(zip(fields, row)))
      
    # Close CSV file
    opened_file.close()
    
    # Return parsed data    
    return parsed_data 

def main():
     # Call our parse function and give it required parameters
    new_data = parse(MY_FILE, "'")
     
     # View how the data looks like
    print new_data
     
if __name__ == "__main__": # only true when running parse.py from command line
    main() # main() will not be called when importing function parse() function