## Install Pip Packages
1. pip install --target ./package package-name

## Zip of package folder
cd package

zip -r ../lambda-kafka.zip .

## Add lambda_function file
cd ..

zip -g lambda-kafka.zip lambda_function.py


## Upload lambda-kafka.zip into AWS lambda function
