import h5py

import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

class CACDDataset(Dataset):
    "This is a wrapper for the CACD dataset"
    def __init__(self, dataset_path):
        super(CACDDataset, self).__init__()
        self.dataset_path = dataset_path
        with h5py.File(dataset_path, 'r') as file:
            self.length = len(file['img'])

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        with h5py.File(self.dataset_path, "r") as file:
            img = file['img'][idx]
            landmark = file['lmk_2D'][idx]
        return img, landmark