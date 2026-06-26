"""
CNN model for predicting Connect Four game outcomes.

Input: RGB image tensor of shape (batch_size, 3, H, W) where:
    - Red channel (index 0):   winner's chip positions (value 1.0 after normalization)
    - Green channel (index 1): loser's chip positions  (value 1.0 after normalization)
    - Blue channel (index 2):  always zero (empty cells are all-zeros)

This encoding matches the PNG format produced by DatasetSaver.

Output: tensor of shape (batch_size, 1) with values in [0, 1].
        Represents the probability that the board state belongs to the winning player's turn
        — i.e., the probability that the current player (whose turn it is) will eventually win.
"""

import torch
import torch.nn as nn


class ConnectFourCNN(nn.Module):
    """
    Convolutional neural network for Connect Four board evaluation.

    Architecture:
        - Three convolutional blocks, each with Conv2d -> BatchNorm2d -> ReLU
        - Global average pooling to collapse spatial dimensions regardless of board size
        - Two fully connected layers with ReLU and Dropout regularization
        - Sigmoid activation for binary probability output
    """

    def __init__(self) -> None:
        super().__init__()

        self.features = nn.Sequential(
            # Block 1: 3 -> 32 channels
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),

            # Block 2: 32 -> 64 channels
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),

            # Block 3: 64 -> 128 channels
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
        )

        self.classifier = nn.Sequential(
            # Collapse spatial dimensions to (batch, 128, 1, 1)
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),

            # Fully connected layers
            nn.Linear(128, 64),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),

            nn.Linear(64, 1),
            nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: float tensor of shape (batch_size, 3, H, W) with values in [0, 1].
               For a standard Connect Four board H=6, W=7.
        Returns:
            float tensor of shape (batch_size, 1) with probabilities in [0, 1].
        """
        x = self.features(x)
        return self.classifier(x)
