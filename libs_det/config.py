""" 
    To check if a GPU is available
    we import torch for torch.device()
"""
import torch
from datetime import datetime

""" 
    Parameters for stage 1
"""
seed = 42
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
lr = 0.0001
epochs = 30
batch_size = 2
weight_decay = 3e-4
base_dir = "TO_BE_CONFIGURED"
run_id = datetime.now().strftime("%H%M%S")

"""
    Available Options:
    Encoder: ResNet-50, ResNet-101, ConvNext-tiny, ConvNext-small, ConvNext-base, ConvNext-large
             EfficientNet-B0, EfficientNet-B1, EfficientNet-B2, EfficientNet-B3, EfficientNet-B4
    Decoder: CNDecoder, RNDecoder, ENDecoder
    Loss: BCELoss, DiceLoss, JaccardLoss
"""
encoder = "ConvNext-small"
decoder = "CNDecoder"
loss = "DiceLoss"

"""
    Base Directory to locate images/masks
"""
data_dir = f"{base_dir}/datasets/ctdar/train/locate.csv"
