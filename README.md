## Install Pip Packages
1. pip install --target ./package package-name

## Zip of package folder
1. cd package
2. zip -r ../lambda-kafka.zip .


## Add lambda_function 
1. cd ..
2. zip -g lambda-kafka.zip lambda_function.py
3. zip -g lambda-kafka.zip scrap.py

## Run Kafka Pipeline
1. Upload lambda-kafka.zip into aws lambda function
2. Run producer.py file from localhost to publish msg
