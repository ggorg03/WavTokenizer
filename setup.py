from setuptools import setup, find_packages

# Função para ler o arquivo requirements.txt
def read_requirements():
    with open("requirements.txt") as req_file:
        return req_file.read().splitlines()

setup(
    name="WavTokenizer",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=read_requirements(),
)
