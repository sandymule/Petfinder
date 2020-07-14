# Title: Petfinder App

## Project Summary
Although there are many dog-owning households in America, there are still many dogs up for adoption (higher than the adoption rate), resulting in many being forcibly put down. One road block preventing potentital adopters from selecting this option is the lack of a uniform system to locate adoptable dogs in the area. In fact, because many of these dogs are mixbreeds, it is difficult for an owner to place his or her preferences into a search. My Petfinder app uses deep learning and computer vision in order to understand the different features of these adoptable dogs, and based on a users preferences, can recommend dogs and where to adopt them. In addition, if an owner loses their dog, they can upload a picture of it, and the app can search dog adoption shelters to see if it has been rescued at a local shelter.

## Data Sources 
PetFinder.com, Bing API

## iPython Notebooks: 
model-src/AdoptionCenterScrape.ipynb - initial attempt to web scrape dog pictures from individual dog adoption centers (this ended up not being used)

model-src/BingAPI.ipynb - used the Bing API to save images of 30 breeds of dogs

model-src/Selenium.ipynb - tutorial on Selenium (used to scrape web images)

model-src/PetFinder.ipynb - web scrape adoptable dogs off of the Petfinder website

model-src/.sh files - Bash script run to obtain actual images from urls

model-src/Train_Test_Split.ipynb - split data into training set and test set

model-src/Creating_Theano_for_Flask.ipynb - deep learning using Theano backend (this ended up not being used)

model-src/NeuralNet.ipynb - deep learning using VGG Base Model and training top model using Tensorflow backend

model-src/Vectorizing_Images.ipynb - change images into a vector set in order to use Nearest Neighbor methodology to find similar dogs

## Final Presentation
Dog_Adoption.pdf - KeyNote Presentation