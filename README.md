# CS488-cloud-project
Project code for CS488/588 cloud computing. Converts data from the DBLP data set into a format usable by MongoDB and queries said data.
# Dataset
The data is detailed and can be downloaded by following this link: https://web.archive.org/web/20170721110641/https://kdl.cs.umass.edu/display/public/DBLP
# Converter.py
Python program for converting the XML file to a JSON file for mongoImport().\
RUNNING: run python3 converter.py in the same directory as the data, labelled "dblp-data.xml".\
OUTPUT: A JSON file "dblp-data.json" that can be run through mongoImport()
# Importing data to MongoDB
The documentation for mongoImport can be found here: https://docs.mongodb.com/manual/reference/program/mongoimport/
The JSON file outputted above is too large to be run through mongoImport. To fix this, run the linux command:\
"split -b 1000000 dblp-data.json data-slice-"\
To split the data into smaller files. Run mongoImport on each of the outputted files (e.g. data-slice-aa)
# Queries:
Queries to run on the data. Only one exists currently
