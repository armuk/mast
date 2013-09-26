mast
====

Python Based Mass Texting

## Getting Started

> pip install twilio

### Set Environment Variables
* TWILIO_SID
* TWILIO_TOKEN
* TWILIO_NUMBER

On OSX you can do this using: ```export TWILIO_SID=111222333444```

### Using mast!

> python mast.py test.txt test.csv

Pretty simple.
* test.txt is a text file with the message to send.
* test.csv is a csv file with the data to call with the format:
  * <name>,<+10000000>
  
Pretty simple right?
