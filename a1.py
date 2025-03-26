import torch
print(torch.__version__)          # PyTorch版本
print(torch.version.cuda)         # PyTorch编译所用的CUDA版本
print(torch.cuda.is_available())  # 检查CUDA是否可用
print(torch.cuda.get_device_name(0))  # 显示GPU型号
print(torch.cuda.get_device_capability(0))  # 显示GPU计算能力（如8.6代表sm86）