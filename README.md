# Assignment Pytorch

This assignment is written in Python using Pytorch. It is tested with Pytest.

## The assignment

For this assignment you will again work with with regular season NBA player
statistics. Similar to the previous assignment you will predict whether a player
in the 2023-2024 was selected as an Allstar. You will use the 2 datasets:

- NBA 2022-2023 regular season stats with Allstars,
- NBA 2023-2024 regular season stats with Allstars.

However, this time you will build a neural network as your classifier model.
The features to train on are: Points, Assists, Rebounds, Steals, Blocks, and Turnovers.
The problems to answer are listed below.

1. Write a function that builds a neural network with the following
    archictecture
    - Input layer: input dimension equal to the number of input features with ouput
    dimension equal to 10.
    - Hidden layer 1: input dimension equal to 10 and output dimension equal to 10
    - Hidden layer 2: input dimenion equal to 10 and output dimension equal to 5
    - Output layer: input dimension equal to 5 and output dimension equal to 1
    - Use relu activation functions for each hidden layer.

    The output of this function is your configured neural network (nn.Module) class.

2. Write a function that trains the model on the 2022-2023 dataset. The loss
    function should be appropriate for binary classification. The optimizer
    should be the Adams optimizer with a learning rate of 0.01. Use the variable batch_size to set the batch size in the dataloader object. Set the number of epochs to train your model
    using the epochs input variable. You will need to extract the features and target variables from the dataset.Be sure to scale the dataset using the StandarScaler.

    Return the trained model and the final training accuracy.

3. Write a function that tests the model using the 2023-2024 data. Use the input variable batch_size to set the batch size in the dataloader. Return the
    model accuracy and the confusion matrix.

## Run command

On the SCC:

```bash
module load miniconda
module load academic-ml/spring-2024
conda activate spring-2024-pyt
cd /path/that/contains/this/repo
pytest
```
