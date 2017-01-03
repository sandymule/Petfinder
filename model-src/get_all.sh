#!/bin/bash

export dog_type='Pug Rottweiler English_Setter Maltese English_Springer_Spaniel German_Shorthaired_Pointer Staffordshire_Bull_Terrier Border_Collie Shetland_Sheepdog Dobermann West_Highland_White_Terrier Bernese_Mountain_Dog Great_Dane Brittany_Spaniel'


for dog in ${dog_type}; do
    python print_dog_urls.py ${dog} | ./get_dogs.sh ${dog} 
done

