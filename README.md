# Compliance LLM

An always-ready Compliance Officer at your service.

## Features

This application lets you test your website's compliance against a compliance policy using OpenAI's LLM model and delivers a report based on the same.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

An .env.example file is given as example.

## Run Locally

Clone the project

```bash
  git clone https://abhijeetps/ComplianceLLM
```

Go to the project directory

```bash
  cd ComplianceLLM
```

Install dependencies

```bash
  pip install -y requirements.txt
```

Start the server

```bash
  python server.py
```

Generate compliance report by sending POST request on `/` with `compliance_website` and `to_test_website` as in reqeust body.

```bash
curl -X POST "localhost:5000/" -d "compliance_website=https://stripe.com/docs/treasury/marketing-treasury" -d "to_test_website=https://www.joinguava.com/"
```

## Authors

- [@abhijeetps](https://www.github.com/abhijeetps)
