import numpy as np #scientific library to work with array and matrixes
import zipfile #access and unzip files
import pandas as pd #library to access databases
import glob #read disk files
import json #read files in json format
import seaborn as sns #generate graphs
import spacy #natural language processing
import nltk #natural language processing
from IPython.core.display import HTML #build html pages
from matplotlib import pyplot as plt #generate graphs
import scispacy # library to handle with specific content
import en_core_sci_md
from os import listdir
from os import walk
# from google.colab import drive

# create dictionary
corona_features = {'paper_id': [], 'title': [], 'abstract': [], 'text': []}

# converting dictionary to Dataframe 
corona_dataframe = pd.DataFrame.from_dict(corona_features)

json_filenames = glob.glob(f'{"./"}//**/*.json', recursive=True);

print(json_filenames)