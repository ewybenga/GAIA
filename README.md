# GAIA
Growing Automatically Is Awesome :D

This will be the central repository holding all of the code produced for my
project descibed in [my blog](https://ericwybenga.com/home/blog/).  


## File Structure
```
GAIA
|   config.yaml
│   README.md
|   requirements.txt
|   run.py     
│
└───arduino
│   │   SoilMoistureSensor.ino
│   
└───src
    │   arduino_comm.py
    │   
    │   
```


>#### `config.yaml`
>>Replace the value for `"port":` with whatever port your raspberry pi and
>>arduino are communicating on.
>#### `README.md` (this file)
>#### `requirements.txt`
>>Contains the python dependencies. Install using `pip install -r
>>requirements.txt`
>#### `run.py`
>>The python file that acts as the controller for the plant monitor. To use it,
>>use the following command: 
>>```
>>python run.py <commands separated by a space>
>>```
>>The translation of command numbers to commands can be found in `config.yaml`.  
>### arduino
>The code in this folder was made to be uploaded to an Arduino board. It was
developed on the ELEGOO UNO R3 from [this
kit](https://www.elegoo.com/collections/arduino-learning-sets/products/elegoo-uno-most-complete-starter-kit).
To upload, copy the file ending in `.ino` into the Arduino IDE window, verify
that the code compiles, and hit the "Upload" button.  
>
>### src
>This folder was made to hold Python and YAML files that enables different
actions with the plant monitor. It should be copied to the raspberry pi where it can be
called from `run.py`. 
>>>