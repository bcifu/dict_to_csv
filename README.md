# Dictionary to CSV
### A quick library to turn a pickled python dictionary into a csv

I frequently write data from my files out as a pickled dictionary where keys map to a list of outputs. This program is a simple commdand line tool I built to make it easier for myself to turn these outputs into a CSV.
This tool is most useful where you have a dictionary which maps to lists because **dictionary items that are a list will each be put in their own cell.** This means that if a key maps to a single value, it gets its own cell, but if it maps to a list, the list is expanded out.

## Usage
Download the code and in the directory with the file run:
`python main.py (the path for your input pickle file) -o (the file that you want to write to, if nothing is provided, it will write to out.csv)`
The output file will be written to the directory that the main.py is in.
