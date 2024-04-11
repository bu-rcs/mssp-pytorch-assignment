import pytorch_assignment as pta
import torch 
import pytest
import numpy as np

def test_problem1():
    nn = pta.problem1(42)

    assert(isinstance(nn, torch.nn.Module))
    parameter_list = list(nn.parameters())
    assert(parameter_list[0].size() == torch.Size([10, 6]))
    assert(parameter_list[2].size() == torch.Size([10, 10]))
    assert(parameter_list[4].size() == torch.Size([5, 10]))
    assert(parameter_list[6].size() == torch.Size([1, 5]))

def test_problem2():
    model, accuracy = pta.problem2("dataset/2022-2023_NBA_Player_Stats_Regular_Allstar.csv", 4, 5, 42)
    expected_accuracy = 0.95

    assert(isinstance(model, torch.nn.Module))
    assert(expected_accuracy == pytest.approx(accuracy, abs=0.05))


def test_problem3():
    accuracy, cm = pta.problem3("dataset/2022-2023_NBA_Player_Stats_Regular_Allstar.csv",
                                "dataset/2023_2024_Allstars.csv",
                                4,
                                5,
                                42)
    expected_cm = np.array([[499,   0],[ 23,   0]])

    assert(accuracy == pytest.approx(0.95, abs=0.05))
    assert(cm[0, 0] == expected_cm[0, 0])
    assert(cm[0, 1] == expected_cm[0, 1])
    assert(cm[1, 0] == expected_cm[1, 0])
    assert(cm[1, 1] ==expected_cm[1, 1])
