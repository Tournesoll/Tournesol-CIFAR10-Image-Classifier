import torch
import torchvision
import numpy as np
import matplotlib
import pandas as pd
import streamlit
import PIL
import sklearn

print("=== 环境验证 ===")
print(f"PyTorch版本: {torch.__version__}")
print(f"TorchVision版本: {torchvision.__version__}")
print(f"NumPy版本: {np.__version__}")
print(f"Matplotlib版本: {matplotlib.__version__}")
print(f"Pandas版本: {pd.__version__}")
print(f"Streamlit版本: {streamlit.__version__}")
print(f"PIL版本: {PIL.__version__}")
print(f"scikit-learn版本: {sklearn.__version__}")

# 检查CUDA支持
if torch.cuda.is_available():
    print(f"\nCUDA可用: {torch.cuda.is_available()}")
    print(f"CUDA版本: {torch.version.cuda}")
    print(f"GPU设备: {torch.cuda.get_device_name(0)}")
else:
    print(f"\nCUDA不可用，使用CPU")

print("\n=== 环境验证完成 ===")