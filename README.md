## Install Pip Packages
1. pip install --target ./package package-name

## Zip of package folder
cd package

zip -r ../lambda-kafka.zip .

## Add lambda_function file
cd ..

zip -g lambda-kafka.zip lambda_function.py

zip -g lambda-kafka.zip scrap.py
