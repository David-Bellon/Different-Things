import torch
import torch.nn as nn

class Model(nn.Module):
  def __init__(self):
    super().__init__()
    self.features = nn.Sequential(
      nn.Conv2d(3, 64, 3, 1, 1),
      nn.BatchNorm2d(64),
      nn.ReLU(),
      
      nn.Dropout(p=0.3),

      nn.Conv2d(64, 128, 3, 1, 1),
      nn.BatchNorm2d(128),
      nn.ReLU(),

      nn.MaxPool2d(2, 2),

      nn.Conv2d(128, 256, 3, 1, 1),
      nn.BatchNorm2d(256),
      nn.ReLU(),

      nn.Dropout(p = 0.4),

      nn.Conv2d(256, 512, 3, 1, 1),
      nn.BatchNorm2d(512),
      nn.ReLU(),

      nn.MaxPool2d(2, 2),

      nn.Conv2d(512, 512, 3, 1, 1),
      nn.BatchNorm2d(512),
      nn.ReLU(),

      nn.Dropout(p = 0.4),

      nn.Conv2d(512, 512, 3, 1, 1),
      nn.BatchNorm2d(512),
      nn.ReLU(),

      nn.MaxPool2d(2, 2),

      nn.Conv2d(512, 512, 3, 1, 1),
      nn.BatchNorm2d(512),
      nn.ReLU(),

      nn.Dropout(p = 0.4),

      nn.Conv2d(512, 512, 3, 1, 1),
      nn.BatchNorm2d(512),
      nn.ReLU(),

      nn.MaxPool2d(2, 2),
      
    )


    self.output = nn.Sequential(
      nn.Linear(2048, 512),
      nn.BatchNorm1d(512),
      nn.ReLU(),

      nn.Dropout(p = 0.3),

      nn.Linear(512, 256),
      nn.BatchNorm1d(256),
      nn.ReLU(),

      nn.Dropout(p = 0.3),

      nn.Linear(256, 4)
    )

  def forward(self, x):
    x = self.features(x)
    x = x.view(x.size(0), 2048)
    x = self.output(x)
    return x


class Chess(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(704, 1024)
        self.linear2 = nn.Linear(1024, 512)
        self.linear3 = nn.Linear(512, 256)
        self.linear4 = nn.Linear(512, 128)
        self.linear5 = nn.Linear(128, 64)
        self.out = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        x = torch.relu(self.linear3(x))
        x = x.view(-1, 512)
        x = torch.relu(self.linear4(x))
        x = torch.relu(self.linear5(x))
        
        out = self.out(x)
        
        return out