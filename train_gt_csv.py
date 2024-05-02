# -*- coding: utf-8 -*-
"""train-gt-csv.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pHFmNOjowYMl1IW-CPQQq6R4h-3vZBZu
"""

import numpy as np
import pandas as pd
import csv

columns = ['ID','File_Name','corX', 'corY']
traindf = pd.DataFrame(columns=columns)

traindf

with open("/content/drive/MyDrive/Comet Hunting/train-gt.txt", "r") as f:
    line = f.readline()
    split = line.strip().split(",")
    sequence_ID = split[0]
    all_triplets = split[1:-1]
    for i in range(0, len(all_triplets), 3):
        file_name, x, y = all_triplets[i:i + 3]
        new_row = [sequence_ID, file_name, float(x), float(y)]
    traindf.loc[len(traindf)] = new_row
traindf

with open("/content/drive/MyDrive/Comet Hunting/train-gt.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        split = line.strip().split(",")
        sequence_ID = split[0]
        all_triplets = split[1:-1]
        for i in range(0, len(all_triplets), 3):
            file_name, x, y = all_triplets[i:i + 3]
            new_row = [sequence_ID, file_name, float(x), float(y)]
            traindf.loc[len(traindf)] = new_row

traindf

traindf.info()

traindf.to_csv('/content/drive/MyDrive/Comet Hunting/train-gt.csv', index=False)