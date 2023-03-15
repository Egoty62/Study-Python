import pickle

list_a = [1, 2, 3, 4, 5]
with open("pickle_test.pickle", "wb") as f :
    pickle.dump(list_a, f)