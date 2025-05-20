import torch
device = torch.device("cuda")
a = torch.randn(3, 3)
b = torch.randn(3, 3)

a = a.to(device)
b = b.to(device)

c = torch.matmul(a, b)
print(c)