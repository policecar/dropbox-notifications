#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'policecar'

from config import *

from dropbox import client, rest, session
import sys, re, logging, pickle
import httplib, urllib

# Pushover specifications
PUSHOVER_URL = "api.pushover.net"
PUSHOVER_PATH = "/1/messages.json"

# display progress logs on stdout
# set level to logging.INFO for verbosity
logging.basicConfig( level=logging.ERROR,
					 format='%(asctime)s %(levelname)s %(message)s' )
log = logging.getLogger(__name__)

# set up session
if not APP_KEY or not APP_SECRET:
    print "You have to configure your Dropbox application tokens in config.py for this to work."
    sys.exit()
sess = session.DropboxSession( APP_KEY, APP_SECRET, ACCESS_TYPE )

log.info( 'read Dropbox access token from file' )
try:
    with open( auth_filename, 'rb' ) as f:
        sess.token = pickle.load( f )
except IOError as e:
    log.info( 'no access tokens stored; authorize dropbox-pushover app' )
    request_token = sess.obtain_request_token()
    url = sess.build_authorize_url( request_token )
    print "For this to work, please grant your app access to your Dropbox at", url, "then hit 'Enter' here to continue." 
    raw_input()
    print "proceeding to fetch all available deltas now"
    print "once done, set up a cronjob on this script to receive notifications upon further changes"
    # consider fixing the akward construction above
    access_token = sess.obtain_access_token( request_token )
    # save access token for future requests
    try:
        with open( auth_filename, 'wb' ) as f:
            pickle.dump( access_token, f, pickle.HIGHEST_PROTOCOL )
    except IOERROR as ioerr:
        print "Check your path configurations in config.py - the specified auth path doesn't seem to exist."

# get client
client = client.DropboxClient( sess )

log.info( 'read pull state from file' )
try:
    with open( cursor_filename, 'rb' ) as f:
        cursor = pickle.load( f )
except IOError as e:
    cursor = None
    pass

log.info( 'fetch available deltas' )
# ( cf. https://www.dropbox.com/developers/reference/api#delta )
more = True
notify = False
while more: 
    delta = client.delta( cursor=cursor )
    cursor = delta[ 'cursor' ]
    more = delta[ 'has_more' ]
    folder_to_watch = unicode( folder_to_watch.decode( 'utf-8', 'replace' ))
    # check if delta includes any entries from desired folder
    for entry in delta[ 'entries' ]:
        if re.match( folder_to_watch, entry[0] ):
            notify = True
            break

log.info( 'write pull state to file' )
try:
    with open( cursor_filename, 'wb' ) as f:
        pickle.dump( cursor, f, pickle.HIGHEST_PROTOCOL )
except IOError as ioerr:
    print "Check your path configurations in config.py - the specified cursor path doesn't seem to exist."

if notify:
    if not USER_TOKEN:
        print "You have to configure your Pushover user token in config.py for this to work."
        sys.exit()
    log.info( 'send message to Pushover' )
    conn = httplib.HTTPSConnection( PUSHOVER_URL )
    conn.request( 'POST', PUSHOVER_PATH,
        urllib.urlencode({ 
            'title'  : '( : db ',
            'token'  : APP_TOKEN,
            'user'   : USER_TOKEN,
            'message': ')',
        }), { 'Content-type': 'application/x-www-form-urlencoded' })

    # for debugging
    res = conn.getresponse()
    log.info( 'response: ' + str( res.status ) + ' ' + res.reason )
    conn.close()
else:
    log.info( "things didn't change" )
    
