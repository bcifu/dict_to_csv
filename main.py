import argparse
import os
import sys
import pickle

parser = argparse.ArgumentParser(description="Take a pickled python dictionary and make it into a csv file", prog="Pickle to CSV")
parser.add_argument('Input_file', help="Input pickle file (path)")
parser.add_argument('Output_file', help="The file that will be created to write the data to", required=False, default='out.csv')
args = parser.parse_args()

if not os.path.isfile(args.Input_file):
    raise Exception('The path provided for the input file does not point to a file')

try:
    with open(args.Input_file, 'rb') as dataFile:
        dataDict = pickle.load(dataFile)
except FileNotFoundError:
    print("The file was not found")
    sys.exit()
except:
    print('Other error, possibly in pickling')
    sys.exit()