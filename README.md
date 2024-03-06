# End-to-end NLP project with Hugging Face, FastAPI and Docker
This is the GitHub repository for the blog post [End-to-end NLP project with Hugging Face, FastAPI and Docker](INSERT URL).

Here's how to use this repo. 

First, build a Docker image by running this:
```bash
docker build -t sentiment-app .
```

Then, run a Docker container from the image:
```bash
docker run -d -p 8000:8000 sentiment-app:latest
```

This will expose an API endpoint on `http://your_address:8000/analyze`

Here's how to call the API endpoint using curl:

Call API: 
```bash
curl -X 'POST' \ 'http://localhost:8000/analyze' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "input_string": "This tutorial is very useful" }'
```

For an example of how to call the API endpoint through a Python script, see `call_api.py`