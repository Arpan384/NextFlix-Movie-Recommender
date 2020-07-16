import pandas as pd
import numpy as np
from statistics import mean
from math import *

dataset = pd.read_csv("data/movies.dat", error_bad_lines=False, header=None, sep="::")
ratingsData = pd.read_csv("data/ratings.dat", header=None, sep="::")
dataset.columns = ["id", "name", "genre"]
ratingsData.columns = ["user", "mid", "rat", "num"]

movie_id = list(dataset["id"].values)
movie_name = list(dataset["name"].values)
movie_cats = [[] for i in range(len(movie_id))]

for i in range(len(dataset)):
    movie_cats[i] = dataset["genre"][i].split("|")


uniqueCats = []

for i in range(len(movie_cats)):
    for j in range(len(movie_cats[i])):
        try:
            uniqueCats.index(movie_cats[i][j])
        except ValueError:
            uniqueCats.append(movie_cats[i][j])


moviecatsdict = [{} for i in range(len(movie_cats))]

for i  in range(len(movie_cats)):
    for j in range(len(uniqueCats)):
        if uniqueCats[j] not in movie_cats[i]:
            moviecatsdict[i][uniqueCats[j]] = 0
        else :
            moviecatsdict[i][uniqueCats[j]] = 1


movRat = [[] for i in range(len(dataset))]
for i in range(len(ratingsData)):
    index = movie_id.index(ratingsData["mid"][i])
    movRat[index].append(ratingsData["rat"][i])


for i in range(len(movRat)):
    try:
        movRat[i] = mean(movRat[i])
    except :
        movRat[i] = -1

def square_rooted(x):
 
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    try:
        sim = round(numerator/float(denominator),3)
        return sim
    except ZeroDivisionError:
        return "*** Similarity Unavailable ***" 


def recommender(mov):
    # mov = input("Enter a movie name: ")
    recom_sims =[]
    recom = []
    movIndex = None
    for i in range(len(movie_name)):
        if movie_name[i][:-7].lower() == mov.lower():
            movIndex = i
    if movIndex == None:
        return "Movie not found in db"
    else:
        for i in range(len(movie_id)):
            sim = cosine_similarity(moviecatsdict[movIndex].values(), moviecatsdict[i].values())
            recom_sims.append(sim)
        indices = list(np.argsort(np.array(recom_sims)))
        recom_sims = list(np.sort(np.array(recom_sims)))
        ind = indices.index(movIndex) 
        indices.pop(ind)
        recom_sims.pop(ind)
        indices.reverse()
        recom_sims.reverse()
        # print(indices)
        # print(recom_sims)
        for i in range(len(indices)):
            # print(movRat[int(indices[i])])
            if (recom_sims[i] > 0.6) and (movRat[indices[i]] >= 3 or movRat[indices[i]] == -1) :
                recom.append(movie_name[indices[i]])
            if (len(recom) >= 5):
                break
        return recom