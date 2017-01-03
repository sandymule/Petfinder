#!/bin/bash

export dog=$1
mkdir -p ./AdoptionPictures/$1

export i=1
while read url; do
    wget --read-timeout=120 --tries=1 $url -O ./AdoptionPictures/${dog}/${i}
    let i++
done

