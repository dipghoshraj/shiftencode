# SHIFT-ENCODER
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

shift-encode is a encoding and decoding libery for file or message encoding with salt value and verifying the message and file for original sources with a decoding feature.

  - Encode a message with a salt value
  - Decode that same message
  - And verifying the message sources


#### Building for source
First install all requirement file:
```sh
>>> pip install shiftencode
```
 

### Run the drawing code:

Step 1 :  Encode a message with shiftencoder
```
>>> from shiftencode import encrypt
>>> encrypt(message="hello-world", salt="test")
'sftend216se213se220se220se223se157se231se223se226se220se212se'
```
Step 2 :  Decode the message using shiftencoder
```
>>> from shiftencode import decrypt
>>> decrypt(message="sftend216se213se220se220se223se157se231se223se226se220se212se", salt="test")
```
Step 3 : verify the sources of the message
```
>>> from shiftencode import validator
>>> validator(message="sftend216se213se220se220se223se157se231se223se226se220se212se", salt="test", verifier="hello-world")
True
>>> validator(message="sftend216se213se220se220se223se157se231se223se226se220se212se", salt="twts", verifier="hello-world")
False
```

License
----
MIT

### NOTE :
```
Author: Dip Ghosh
email: dipghoshraj@gmail.com
IOT and robotics developer with a handson experience in Software development and DevOps.
```


<!-- **Free Software, Yeah it's fucking truth!** -->