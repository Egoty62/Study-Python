import pickle

with open("pickle_test.pickle", "rb") as f :
    result = pickle.load(f)

print(result)