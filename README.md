open terminal and navigate to the dockerfile folder that contains the project. After that run the command 
```docker build -t python-barcode .```
This command will build the docker image on the system.
Once this is done, the next step is to run the docker image. To run the docker image type the following command 
```docker run -it python-barcode```
This will run the program and ask for input from the user for plain text to be encrypted.
For example we can type "I love internet"
The second message from the program asks for the keyword that will be used to decrypt this message.
We can enter "NYITV".
The program will then show the decrypted message "ottiinveXerXlne".
To check the run : https://github.com/kamranuddin1300670/NYITfiles.git
Then the program would ask for the message that needs to be decrypted. So we will type the decrypted message from the last output and then it asks for the keyword. The keyword is the same as used before "NYITV".
Finally it will show the decrypted message, the cipher text and the keyword in the output.
