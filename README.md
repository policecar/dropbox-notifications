dropbox-pushover
================

Receive Pushover notifications to your Android or iPhone 
of any changes occurring in a chosen Dropbox folder.

Setup
-------

Install the Dropbox SDK: 

    unzip -x dropbox-python-sdk-1.5.1.zip
    cd dropbox-python-sdk-1.5.1
    python setup.py install 
    
In config.py specify the path to the Dropbox folder to keep track of as well as your Pushover
user token which can be retrieved from https://pushover.net/. Run
    
    ./dropbox-pushover.py
    
once to authorize access to your Dropbox. Then set up a cronjob ( crontab -e ) for dropbox-pushover.py, e.g. add a line like 
    
    00/5 * * * * <INSERT_FULL_PATH_TO_PYTHON>/python <INSERT_FULL_PATH_TO_REPOSITORY>/dropbox-pushover.py

to your crontab to run the script every 5 minutes, and you're set to receive Pushover notifications 
of any changes occurring in the specified Dropbox folder.

Author
-------
Priska Herger <priska@23bit.net>  
https://github.com/policecar/dropbox-pushover


Notes
-------
[1] Make your own Dropbox app at https://www.dropbox.com/developers/apps if you prefer or 
if the provided credentials don't work (which currently only work max 5 users)  and 
substitute your own tokens in config.py. 
