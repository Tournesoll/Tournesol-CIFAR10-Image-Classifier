"""
验证项目结构设置
"""

import sys
import os
from pathlib import Path

def main():
    print("验证Tournesol CIFAR-10项目结构设置")
    print("=" * 50)

    # 检查当前目录
    current_dir = Path.cwd()
    print(f"当前目录: {current_dir}")

    # 检查src目录
    src_dir = current_dir / "src"
    if src_dir.exists():
        print("✅ src目录存在")
    else:
        print("❌ src目录不存在")
        return False

    # 检查主要模块文件
    required_files = [
        "src/__init__.py",
        "src/config/__init__.py",
        "src/config/config.py",
        "src/data/__init__.py",
        "src/data/dataset.py",
        "src/data/preprocessing.py",
        "src/models/__init__.py",
        "src/models/base_model.py",
        "src/models/sklearn_models.py",
        "src/models/pytorch_models.py",
        "src/training/__init__.py",
        "src/training/trainer.py",
        "src/training/evaluator.py",
        "src/inference/__init__.py",
        "src/inference/predictor.py",
        "src/utils/__init__.py",
        "src/utils/logger.py",
        "src/utils/visualization.py",
        "src/web/__init__.py",
        "src/web/app.py",
        "src/train.py",
        "src/evaluate.py",
        "src/test_structure.py",
        "src/README.md"
    ]

    missing_files = []
    for file_path in required_files:
        if not (current_dir / file_path).exists():
            missing_files.append(file_path)

    if missing_files:
        print("❌ 缺少以下文件:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    else:
        print("✅ 所有必需文件都存在")

    # 检查配置文件存在性
    config_file = src_dir / "config" / "config.py"
    if config_file.exists() and config_file.stat().st_size > 0:
        print("✅ 配置文件存在且不为空")
    else:
        print(f"❌ 配置文件不存在或为空: {config_file}")
        return False

    # 简单的语法检查
    try:
        import ast
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.strip():
            print("❌ 配置文件为空")
            return False

        ast.parse(content)
        print("✅ 配置文件语法正确")

        if 'class Config' in content:
            print("✅ Config类定义存在")
        else:
            print("❌ Config类定义不存在")
            return False

    except SyntaxError as e:
        print(f"❌ 配置文件语法错误: {e}")
        return False
    except UnicodeDecodeError as e:
        print(f"❌ 文件编码错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 配置文件检查失败: {e}")
        return False

    # 检查目录结构
    required_dirs = ["data", "models", "logs"]
    for dir_name in required_dirs:
        dir_path = current_dir / dir_name
        if not dir_path.exists():
            print(f"❌ 目录 {dir_name} 不存在")
            return False
    print("✅ 所有必需目录都存在")

    print("\n" + "=" * 50)
    print("🎉 项目结构设置验证通过！")
    print("\n接下来你可以：")
    print("1. 运行训练: python src/train.py")
    print("2. 运行评估: python src/evaluate.py")
    print("3. 启动Web应用: streamlit run test_streamlit.py")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
