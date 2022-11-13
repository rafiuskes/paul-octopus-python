# paul-octopus-python

You can use this Python code to construct your solution to predict the results of the 2022 World Cup.

This is a Python webapp, and you will need to deploy it in a cloud provider.
In this example we will use the Azure Container Instances to run the webapp and generate the predictions.

## Requirements
- Docker
- Python

## Google Artifact Registry
In this example we will use the Google Artifact Registry to push our Docker image containing the webapp.

To start using the GCP to push images from your local environment, you will first need to authenticate

```
gcloud auth login
gcloud config set project phoenix-cit
gcloud auth application-default login
```

Create an artifact repository for you

```
gcloud artifacts repositories create paul-2022-<login> --repository-format=docker \
--location=us-central1 --description="Paul 2022 - <Name>"
```

With docker running on your machine, configure docker to be able to connect to your artifact repository

```
gcloud auth configure-docker us-central1-docker.pkg.dev
```

## Implementing your code to predict matches
Feel free to change or adapt anything in this solution.

If you just want to write a function to predict a match, based on the teams that are playing, you just need to create a new python file inside `predictor` folder, and extend the `AbstractPredictor` class.

One dummy predictor called `OneZeroPredictor` is included as an example.

Remember that you will need to use at lease one of the dataset files provided inside the Storage Account.


## Building and pushing your docker image
When you have your predictor implemented, you can build the docker image using the provided Dockerfile.

Include your login in the image, to avoid conflicts with others that are sharing the same environment.
```
docker build -t us-central1-docker.pkg.dev/phoenix-cit/paul-2022-<login>/<login>-predictor .
docker push us-central1-docker.pkg.dev/phoenix-cit/paul-2022-<login>/<login>-predictor
```

This will push your predictor WebApp to Artifact Registry, and it will be available to deploy using Cloud Run.

## Deploy in Cloud Run
Cloud Run is an easy way to deploy your WebApp in the GCP.

```
gcloud run deploy <login>-predictor --image=us-central1-docker.pkg.dev/phoenix-cit/paul-2022-<login>/<login>-predictor --region=us-central1
```

## Accessing your App and generating the Predictions
After the deployment of your app, gcloud will output the service url that you can use to access your predictor.

You can now access the app from your browser.

### Running a predictor class
The way that this solution is implemented, you can pass the name of your predictor in the URL like the following example:
```
https://eduardohf-predictor-wuydz5dt4a-uc.a.run.app/predict/OneZeroPredictor
```

In this example, it will instantiate the `OneZeroPredictor` class and call the method to make predictions.
The browser will download the CSV file called `predictions.csv`.

This file that you just download contains the predictions from your algorith and should be ready to submit.