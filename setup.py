from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()



setup(
    name="triple-encoders",
    version="0.0.1",
    author="Justus-Jonas Erker",
    author_email="justus-jonas.erker@tu-darmstadt.de",
    download_url="https://github.com/UKPLab/arxiv2024-triple-encoders",
    description="Distributed Sentence Transformer Representations with Triple Encoders ",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    packages=find_packages(),
    python_requires=">=3.8.0",
    install_requires=[
        'datasets>=2.17.0,<2.18.0',
        'transformers>=4.35.0,<4.36.0',
        'sentence-transformers>=2.2.2',
        'torch==2.0.1',
        'numpy==1.22.4',
        'pandas==2.2.2',
        'tqdm==4.64.1',
        'huggingface_hub>=0.16.4'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
    ],
    keywords="PyTorch NLP deep learning Sentence Transformer Triple Encoders Dialog Systems",
)
