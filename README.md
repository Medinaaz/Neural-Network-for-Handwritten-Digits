# Neural-Network-for-Handwritten-Digits
A neural network to recognize handwritten digits with TensorFlow

# Configure  the project
Create a Python3 virtual environment in order to use correctly independencies 

# Import MNIST Dataset
Images of handwritten digits 28x28 pixels in size 

# Define Neural Network Architecture
Each neural network consists of numbers of layers, units per each layer and the way how they are connected to each other. Unit concept consits of a brain neuron. 

# Build a TensorFlow Graph
We define three tensors as placeholders which we will be feeding values into later. During the training process the network will be updating parameters as:
_weight_ and _bias_ . These 2 parameters are used in activation functions of neurons representing the strength of the connection between units. After this we define the layers of the network that will manipulate the tensors.
**_Very important_** Each hidden layer will execute matrix multiplication on the previous layer's outputs and the current layer's weights and add the bias to these values. In the last hidden layer we will apply dropout operation. Last step is defining loss function.

# Training and Testing
Feed the training dataset thought the graph and optimize the loss function. We run the testing dataset using the trained graph and checking which image will be predicted correctly.  

# Predicted and True Labels
Minimize the difference between these 2 groups of labels of the images. 

# How to run

python main.py


**_If you are using Python2 and Python3 you should specify it in the command line as "python"  for Python2 and "python3" for Python3. But however TensorFlow libraires will not be working in a Python2 environment. _**

©All rights reserved for: Python Machine Learning Projects
Written by Lisa Tagliaferri, Michelle Morales, Ellie Birbeck, and
Alvin Wan, with editing by Brian Hogan and Mark Drake
