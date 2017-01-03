import sys
import os
import pandas as pd

os.chdir('AdoptionData')

dog = sys.argv[1]
df = pd.read_json(dog)
for x in range(len(df)):
    print df.iloc[:,0][x]
