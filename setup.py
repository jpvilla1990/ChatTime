from setuptools import setup, find_packages

setup(
    name="chat_time",
    version="0.3.0",  # Dynamic versioning handled separately
    description="ChatTime: A Multimodal Time Series Foundation Model",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Chengsen Wang, Qi Qi, Jingyu Wang, Haifeng Sun, Zirui Zhuang, Jinming Wu, Lei Zhang, Jianxin Liao",
    author_email="cswang@bupt.edu.cn",
    maintainer="cswang",
    maintainer_email="cswang@bupt.edu.cn",
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.1,<2.5",
        "transformers>=4.47.1",
        "lightning>=2.0",
        "numpy~=1.26.0",
        "scikit-learn>=1.6.0",
        "scipy~=1.11.3",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "Time Series Forecasting",
        "Transformer",
        "Deep Learning",
        "PyTorch",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
