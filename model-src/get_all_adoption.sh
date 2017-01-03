#!/bin/bash

export dog_type='Everything'

for dog in ${dog_type}; do
    python print_dog_urls_adoption.py ${dog} | ./get_dogs_adoption.sh ${dog} 
done

