# Take parsed data and visualize using popular Python math libraries
from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

import parse as prs 

data_file = prs.parse(prs.MY_FILE, ",")

def visualize_days(parsed_data):
    """Visualize data by day of week"""
    
    # Count how many incidents occur per day, store result in counter 
    counter = Counter(item["DayOfWeek"] for item in parsed_data) # counter is a dictionary object
    
    # Separate days of the week (x-axis) from number of incidents per day (y-axis)
    # plt.xticks() ony accepts tuples for x-axis labelling
    week_days = tuple(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]) 
    # obtain the frequency of incidents for each day of the week
    incident_count = [counter["Monday"], 
                      counter["Tuesday"],
                      counter["Wednesday"],
                      counter["Thursday"], 
                      counter["Friday"],
                      counter["Saturday"],
                      counter["Sunday"]]
    
    # Assign number of incidents per day to a matplotlib plot instance
    plt.plot(incident_count)

    # Create x-axis ticks, assign the labels
    # range(len()) tells matplotlib how many ticks to place
    plt.xticks(range(len(week_days)), week_days) 
    
    # Save the plot
    plt.savefig("Days.png")
    
    # Close the plot file
    plt.clf()
    
def visualize_type(parsed_data):
    """"Visualize data by category in a bar graph"""
    
    # Count how many incidents occur by category
    counter = Counter(item["Category"] for item in parsed_data)
    
    # Obtain category labels
    labels = tuple(counter.keys())
    
    # Set label locations (for helping with tick placement)
    xlocations = np.arange(len(labels)) + 0.5
    
    # Set width of each bar
    width = 0.5
    
    # Assign (y-axis) data to a bar chart
    plt.bar(xlocations, counter.values(), width=width)
    
    # Assign (x-axis) labels and tick locations
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    
    # Increase room for labels to avoid cut off
    plt.subplots_adjust(bottom=0.4)
    
    # Make the graph larger
    plt.rcParams["figure.figsize"] = 12, 8
    
    # Save the graph
    plt.savefig("Type.png")
    
    # Close plot file
    plt.clf()
    
def main():
    visualize_days(data_file)
    visualize_type(data_file)
    
if __name__ == "__main__":
    main()