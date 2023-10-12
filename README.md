# github-training-fronza

[TESTED] 
Update on README.md file to check webhook sending `push` information to the listener.

# my_listener.py
This script will be listening the POST requests from the Githu webhook and sabe the JSON information on `webhook-data` folder.
  -  To make this "work" we used the Ngrok to create a URL mapping to our local host:
    - Download Ngrok and install it
    - Then, execute: `ngrok http 5000` (5000 which is the port that the listener is listening)
Run the script and see the magic happening.
