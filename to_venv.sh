#!/bin/sh

echo "pandas" > requirements.txt
echo "numpy" >> requirements.txt
echo "ipykernel" >> requirements.txt
echo "matplotlib" >> requirements.txt
echo "scikit-learn" >> requirements.txt
echo "seaborn" >> requirements.txt


python3 -m venv envi

source envi/bin/activate

pip install -r requirements.txt

python3 -m ipykernel install --user --name=envi --display-name "envi"

rm requirements.txt