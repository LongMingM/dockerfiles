import os
import numpy as np
import torch

device = torch.device("cuda")

data_dir = './tcdata'
a = np.load(os.path.join(data_dir, "a.npy"))
b = np.load(os.path.join(data_dir, "b.npy"))
a = torch.from_numpy(a).to(device).float()
b = torch.from_numpy(b).to(device).float()
c = torch.matmul(a,b).cpu().numpy()

print(c)
np.save("result.npy", c)