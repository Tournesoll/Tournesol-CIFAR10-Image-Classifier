#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('src/config/config.py', 'w', encoding='utf-8') as f:
    f.write('''"""
配置文件
包含所有超参数、路径配置等
"""

import os
from pathlib import Path

class Config:
    """配置类"""

    # 项目根目录
    PROJECT_ROOT = Path(__file__).parent.parent.parent

    # 随机种子（使用学号）
    RANDOM_SEED = 123456  # 请替换为实际学号

    # 数据集配置
    DATA_DIR = PROJECT_ROOT / "data"
    CIFAR10_MEAN = [0.4914, 0.4822, 0.4465]
    CIFAR10_STD = [0.2023, 0.1994, 0.2010]
    IMAGE_SIZE = 32
    NUM_CLASSES = 10
    CLASS_NAMES = ['plane', 'car', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']

    # 模型配置
    MODELS_DIR = PROJECT_ROOT / "models"

    # PyTorch模型配置
    PYTORCH_MODEL_CONFIG = {
        'batch_size': 128,
        'learning_rate': 0.001,
        'epochs': 50,
        'weight_decay': 1e-4,
        'momentum': 0.9,
        'dropout_rate': 0.5
    }

    # sklearn模型配置
    SKLEARN_MODEL_CONFIG = {
        'svm': {
            'C': [0.1, 1, 10, 100],
            'kernel': ['rbf', 'linear']
        },
        'rf': {
            'n_estimators': [100, 200, 300],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5, 10]
        },
        'lr': {
            'C': [0.01, 0.1, 1, 10, 100],
            'penalty': ['l1', 'l2'],
            'solver': ['liblinear', 'saga']
        }
    }

    # 训练配置
    LOGS_DIR = PROJECT_ROOT / "logs"
    CHECKPOINT_DIR = MODELS_DIR / "checkpoints"

    # 推理配置
    INFERENCE_CONFIG = {
        'batch_size': 32,
        'device': 'cuda' if os.environ.get('CUDA_AVAILABLE', 'true').lower() == 'true' else 'cpu'
    }

    # Web应用配置
    WEB_CONFIG = {
        'title': 'CIFAR-10 图像分类器',
        'description': '基于机器学习技术的CIFAR-10图像分类Web应用',
        'max_file_size': 5 * 1024 * 1024,  # 5MB
        'supported_formats': ['jpg', 'jpeg', 'png']
    }

    @classmethod
    def get_model_path(cls, model_name: str, extension: str = '.pth') -> Path:
        """获取模型保存路径"""
        return cls.MODELS_DIR / f"{model_name}{extension}"

    @classmethod
    def get_log_path(cls, log_name: str) -> Path:
        """获取日志文件路径"""
        return cls.LOGS_DIR / f"{log_name}.log"

    @classmethod
    def get_checkpoint_path(cls, model_name: str, epoch: int = None) -> Path:
        """获取checkpoint路径"""
        if epoch is not None:
            return cls.CHECKPOINT_DIR / f"{model_name}_epoch_{epoch}.pth"
        else:
            return cls.CHECKPOINT_DIR / f"{model_name}_best.pth"
''')

print("Config file created successfully!")
