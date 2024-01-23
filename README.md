# generative-ai - "Fisica e Scuola" UniBo project

To setup the proper Python 3.10 environment and install all the needed dependecies on your Jetson Nano device, clone this repository and source the `setup.sh` script:
```
source generative-ai/setup.sh
```

Running all the commands may require several minutes.
Once the process is complete, you can test that everything is working fine activating the Python `llm` environment and running the `test.py` script:
```
source venvs/llm/bin/activate
cd generative-ai
python test.py
```
You should get back something like:
```
Query result: ...
```

***

WARNING: to run the examples in the different modules, you also need to create your account on [Replicate](https://replicate.com/), generate a **Replicate API Token**, and save it in the root directory of the repository with the name `replicate_api_token.txt`.