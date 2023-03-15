import pickle

with open("multiply_object.pickle", "rb") as f :
    a = pickle.load(f)
    print(a.multimutli(5))