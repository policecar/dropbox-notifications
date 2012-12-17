# Dropbox config
# ( create a free Dropbox app at https://www.dropbox.com/developers/apps 
#   to obtain the following tokens )

APP_KEY     = ''
APP_SECRET  = ''
ACCESS_TYPE = 'dropbox' # either 'dropbox' or 'app_folder' depending on app config

# Pushover config
# ( retrieve your user token from https://pushover.net/ )
APP_TOKEN   = 'EpMD3BrlmxioeKvGujVccccPqHeUxd'
USER_TOKEN  = ''


# Dropbox folder to be notified about ( / is the Dropbox root )
folder_to_watch = '/'

# Note: specify full path names in the following for this to work with crontab
# filename to store Dropbox access token in
auth_filename   = '<INSERT_FULL_PATH_HERE>/db_oauth'
# filename for storing state of updates pulled ( aka cursor )
# ( cf. https://www.dropbox.com/developers/reference/api#delta )
cursor_filename = '<INSERT_FULL_PATH_HERE>/last_cursor'
