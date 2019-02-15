
# Author: Trevor Leake
# Note: This was developed iteratively in the accompanying Jupyter notebook

# We intend to parse the accompanying file "data.xml" and create a CSV
# which holds fields occured, value, and usage point. Please see the
# companion notebook for details. There we get to understand the document
# a bit more fully.

# Libraries and modules
import xml.etree.ElementTree as ET
import pandas as pd

# Let's go ahead and load the document with a parser like ElementTree.
tree = ET.parse('./data.xml')

# This map allows us to search the XML elements with less ugly queries.
namespaces = {
    'Atom' : 'http://www.w3.org/2005/Atom',
    'NAESB': 'http://naesb.org/espi'
}

# Find all "value" objects in the NAESB namespace
values = [element.text for element in tree.findall('.//NAESB:value', namespaces)]

# Find the first "published" object in the Atom namespace
published = tree.find('.//Atom:published', namespaces).text

# Find the first "kind" object in the NAESB namespace
kind = tree.find('.//NAESB:kind', namespaces).text

# Create a pandas dataframe using column headers as given in the email.
df = pd.DataFrame.from_dict({
        "usage point": kind,
        "occured": published,
        "value": values
})
df.to_csv('data.csv', index=False)
