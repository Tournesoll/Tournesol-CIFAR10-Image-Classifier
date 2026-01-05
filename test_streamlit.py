"""
Tournesol CIFAR-10 图像分类器 - Streamlit Web应用

这是使用新的模块化架构的Streamlit应用入口文件。
"""

from src.web.app import create_streamlit_app

# 创建并运行Web应用
if __name__ == "__main__":
    app = create_streamlit_app()
    app.run()
