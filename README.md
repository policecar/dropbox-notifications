dropbox-pushover
================

Receive Pushover notifications to your Android or iPhone 
of changes that occurred in a chosen Dropbox folder since you last checked.

Setup
-------

Unarchive the Dropbox SDK and run python setup.py install on it.  
Create a Dropbox app at https://www.dropbox.com/developers/apps and put your key and secret into config.py 
( or trust me to access your Dropbox but don't ).  
Sign up with Pushover, retrieve your Pushover user token from https://pushover.net/, 
and add it to the config file.  
In the config file specify which folder in your Dropbox to track or else track 'em all.
Set up a cronjob ( crontab -e ) for dropbox-pushover.py and you're set to receive Pushover notifications 
of any changes occurring in the specified Dropbox folder;  
e.g. 
    
    00/5 * * * * <INSERT_FULL_PATH_TO_PYTHON>/python <INSERT_FULL_PATH_TO_REPOSITORY>/dropbox-pushover.py

to run the script every 5 minutes.

Author
-------
Priska Herger <priska@23bit.net>  
https://github.com/policecar/dropbox-pushover

