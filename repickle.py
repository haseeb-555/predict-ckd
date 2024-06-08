import pickle

# Load the model from the existing pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Re-pickle the model with the current version of scikit-learn
with open('model_updated.pkl', 'wb') as file:
    pickle.dump(model, file)
