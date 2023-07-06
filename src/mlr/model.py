import torch.nn as nn

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.__model=nn.Sequential(
            nn.Linear(2, 1),
        )
    
    def forward(self, x):
        return self.__model(x)