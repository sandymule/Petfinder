import sys
import os
import pandas as pd

os.chdir('PictureData')

#dog_type = ['Labrador Retriever', 'German Shepherd', 'Poodle', 'Chihuahua', 'Golden Retriever', 'Yorkshire Terrier', 'Dachshund', 'Beagle', 'Boxer', 'Miniature Schnauzer', 'Shih Tzu', 'Bulldog', 'German Spitz', 'English Cocker Spaniel', 'Cavalier King Charles Spaniel', 'French Bulldog', 'Pug', 'Rottweiler', 'English Setter', 'Maltese', 'English Springer Spaniel', 'German Shorthaired Pointer', 'Staffordshire Bull Terrier', 'Border Collie', 'Shetland Sheepdog', 'Dobermann', 'West Highland White Terrier', 'Bernese Mountain Dog', 'Great Dane', 'Brittany Spaniel']

dog = sys.argv[1]
df = pd.read_json(dog)
for x in range(len(df)):
    print df.iloc[:,0][x]
