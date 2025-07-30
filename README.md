<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">AWS Lambda Python - Docker Selenium CDK Template App</h3>

  <p align="center">
	Use this code as a starting point for deploying your own AWS Lambda functions that utilize Selenium. Useful for web-automation, serverless web-scraping.
	Instructions below are provided for running this application via AWS SSO (IAM Identity Center), using the AWS Cloud Development Kit (CDK) and Python.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was created as I was searching for a method to deploy a serverless web-automation bot on AWS Lambda. After finding multiple useful repositories, I merged them together to create a template for CDK web deployment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][python-url]
* [![Docker][Docker.com]][Docker-url]
* [![AWS][aws.com]][aws-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This template requires a few system prequisites:
- Node.js and node package manager. (`npm`, in this exapmle installed via node version manager `nvm`)
- An AWS account, with IAM Identity Center configured.
- AWS Cloud Development Kit CLI (run using `cdk`)
- AWS Command Line Interface v2 (`aws`)
- Docker engine (`docker`)
- Python (`python`)

Configuration prequisites:
- Setup your aws CLI to run using SSO (previously IAM Identity Center)
- Ensure you can run `aws sso login --profile <your-profile>` to successfully login to AWS.
- Create a local `.env` file in the project folder, for the variables `ACCOUNT_ID` (your AWS account ID) and `REGION` (your AWS region). These are read by `app.py`


### Installation & Usage

1. Clone the repo to your local directory
```sh
$ git clone https://github.com/HoYoung1/aws-lambda-python313-selenium-cdk-template.git
```

2. Navigate to the new directory
```sh
$ cd aws-lambda-python313-selenium-cdk-template
```

3. Create a new virtual environemnt called `.venv` with python at the top level
```sh
$ python -m venv .venv
```

4. Activate the virtual environment
```sh
$ source .venv/bin/activate # Use this line for Linux/MacOS
source .venv/Scripates/activate.bat  # Use this line for Windows
```

5. Install the requirements file in the top level directory (required for CDK use in python)
```sh
$ pip install -r requirements.txt
```

6. Login via the AWS CLI (for non-IAM examples check out AWS documentation) using a profile
```sh
$ aws sso login --profile your-profile
```

7. Deploy the app using the CDK
```sh
$ cdk deploy --profile your-profile
```

8. Find the name of your newly deployed function (this will take the base name you define in `app.py` and function name from `scraper.py`)
```sh
$ aws lambda list-functions --profile your-profile
```

9. Invoke the function via AWS CLI, output the response as `response.json`, if successful, you should see a STATUS:200 response in your command line. Check the json output file for the return values.
```sh
$ aws lambda invoke --profile your-profile --function-name your-function-name-copied-from-step-8 response.json
```

The application stack should now be available in your AWS account if you visit AWS Lambda.

#### Testing locally with docker prior to deploying
If you would like to check the application locally, you can separately build a test of the docker container image and run / test it locally before deploying.

1. Navigate to the scraper directory to build the Dockerfile
```sh
$ cd lambda/scraper
```

2. Build the docker image locally
```sh
$ docker build -t my-image:test .
```

3. Since the root image is an AWS/Lambda/Python image, you can run it simply with:
```sh
$ docker run -p 9000:8080 my-image:test

```

4. Open a new shell (or pass -d flag in the previous command to run in background) and send a cURL request to the local container port you exposed:
```sh
$ curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"this is optional"}'
```

You should receive a response that matches the return of the `lambda_function.handler` function.

5. Shut down the container
```sh
$ docker kill my-image:test
```

This is useful to do _before_ pushing the container to AWS, as it will allow you to confirm your code is functioning as expected.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [mbruntink's lambda-scraper](https://github.com/mbruntink/lambda-scraper/)
* [umihico's docker selenium lambda](https://github.com/umihico/docker-selenium-lambda)
* [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-alt-test)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[python-url]: https://python.org
[Docker-url]: https://docker.com
[aws-url]:https://aws.amazon.com



<!-- ORIGINAL REPOSITORY  -->
https://github.com/rdarneal/aws-lambda-python-selenium-cdk-template.git