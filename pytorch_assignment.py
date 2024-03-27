import torch 
import torch.nn as nn
import pandas as pd

"""
Implement the neural network architecture from Problem 1 in the below funciton.
Return the instatiated class.
"""
def problem1(seed):
    torch.manual_seed(seed)

    return None

def problem2(nba_22_23_stats_filepath, batch_size, epochs, seed):
    model = problem1(seed)

    # Implement training loop here

    accuracy = None

    return model, accuracy

def problem3(nba_22_23_stats_filepath, 
             nba_23_24_all_stars, 
             batch_size, 
             epochs,
             seed):
    trained_model, train_accuarcy = problem2(nba_22_23_stats_filepath,
                             batch_size,
                             epochs, 
                             seed)

    # Import the allstar data and extract what you need to test the model here
    df = pd.read_csv(nba_23_24_all_stars)

    # Create dataset and dataloader objects here.

    # Implement predictions here using trained_model

    test_accuracy = None
    confusion_matrix = None

    return test_accuracy, confusion_matrix