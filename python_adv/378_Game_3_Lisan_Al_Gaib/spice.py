'''
Lab 7: ADVANCED PYTHON
Activity 1 : LISAN-AL-GAIB (Dune Reference)
Author : Sabyasachi Samantaray

Here we will be dealing only with 2D data to aid visualisation

In this activity, your aim will be the following.
1) Implement the kmeans algorithm completely and correctly.
2) Implement all TODOs without using any loops
'''

### TODO 1: Importing the necessary libraries - numpy, matplotlib and time
### This TODO is already done
import time # to time the execution
import numpy as np
import matplotlib.pyplot as plt
### TODO 1

### TODO 2
### Load data from data_path
### Check the input file spice_locations.txt to understand the Data Format
### Return : np array of size Nx2
def load_data(data_path):
    arr=np.loadtxt(data_path, delimiter=",")
    
    return arr

### TODO 3.1
### If init_centers is None, initialize the centers by selecting K data points at random without replacement
### Else, use the centers provided in init_centers
### Return : np array of size Kx2
def initialise_centers(data, K, init_centers=None):
    if init_centers is None:
        centers = data[np.random.choice(data.shape[0], K, replace=False)]
    else:
        centers=np.array(init_centers)
    return centers

### TODO 3.2
### Initialize the labels to all ones to size (N,) where N is the number of data points
### Return : np array of size N
def initialise_labels(data):
   return np.zeros(data.shape[0], dtype=float) 

### TODO 4.1 : E step
### For Each data point, find the distance to each center
### Return : np array of size NxK
def calculate_distances(data, centers):
    distances = np.linalg.norm(data[:, np.newaxis] - centers, axis=2)
    return distances

### TODO 4.2 : E step
### For Each data point, assign the label of the nearest center
### Return : np array of size N
def update_labels(distances):
    updatedlabels=np.argmin(distances, axis=1)
    return updatedlabels

### TODO 5 : M step
### Update the centers to the mean of the data points assigned to it
### Return : np array of size Kx2
def update_centers(data, labels, K):
    mask = np.eye(K)[labels] 
    sums = mask.T @ data  
    counts = mask.sum(axis=0, keepdims=True).T 
    new_centers = np.divide(sums, counts, where=counts != 0)
    return new_centers

### TODO 6 : Check convergence
### Check if the labels have changed from the previous iteration
### Return : True / False
def check_termination(labels1, labels2):
    return np.array_equal(labels1, labels2)

### DON'T CHANGE ANYTHING IN THE FOLLOWING FUNCTION
def kmeans(data_path:str, K:int, init_centers):
    '''
    Input :
        data (type str): path to the file containing the data
        K (type int): number of clusters
        init_centers (type numpy.ndarray): initial centers. shape = (K, 2) or None
    Output :
        centers (type numpy.ndarray): final centers. shape = (K, 2)
        labels (type numpy.ndarray): label of each data point. shape = (N,)
        time (type float): time taken by the algorithm to converge in seconds
    N is the number of data points each of shape (2,)
    '''
    data = load_data(data_path)    
    centers = initialise_centers(data, K, init_centers)
    labels = initialise_labels(data)

    start_time = time.time() # Time stamp 

    while True:
        distances = calculate_distances(data, centers)
        labels_new = update_labels(distances)
        centers = update_centers(data, labels_new, K)
        if check_termination(labels, labels_new): break
        else: labels = labels_new
 
    end_time = time.time() # Time stamp after the algorithm ends
    return centers, labels, end_time - start_time 

### FILL THE LINES BELOW THE TODO COMMENTS
def visualise(data_path, labels, centers):
    data = load_data(data_path)

    # Scatter plot of the data points
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

    ### TODO 7 : In conclusion
    ### Set title as 'K-means clustering'
    plt.title("K-means clustering")
    plt.xlabel("Longitude")
    ### Set xlabel as 'Longitude'
    plt.ylabel("Latitude")
    ### Set ylabel as 'Latitude'
    plt.savefig("kmeans.png")
    ### Save the plot as 'kmeans.png'


    ## DO NOT CHANGE THE FOLLOWING LINE
    return plt