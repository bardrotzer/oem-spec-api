# oem-spec-api
API that will get the specifications for a car model using OpenAI's API

## setup
Its quite simple. To make this run you first need a `OPEN AI API key` you can get one at [Open AI](https://openai.com)

Once you have the key you should configure your local repo (im using venv for this)

```bash
   # create the virtaual environment with python 
   # at the time of writing this was 3.11.x
  python -m venv env

  # switch to the new environment
  source env/bin/activate

  # install all dependencies in this environment (none at the moment)
  pip install -r requirements.txt
```

## start the app

```bash
  # you can run it as pure python,
  # but using uvicorn is more stable
  uvicorn app:app --reload

```
