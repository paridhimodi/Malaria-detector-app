# Malaria-detector-app

A deep learning model is build to detect malaria of the patients with the cell images of the patients.I used Vgg19 architecture to build this model to predict if an uploaded cell image is parasitized or uninfected. At first a Deep learning model was trained and tested in Google Colab based on the dataset obtained from kaggle, then in order to give it a user interface, Flask framework is used.
System will read the image uploaded by the user, augment it and will use the saved custom model to detect whether the disease is present or not in the patient and thus display the result in a user-friendly language.
