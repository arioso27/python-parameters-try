##create new playlist by HTTP Control
#http://127.0.0.1:8888/ajquery/?cmd=CreatePlaylist&param1=New+Playlist&param3=NoResponse


import sys, os
import codecs
#import http
from http import client
#import urllib
import urllib.parse
import urllib.request


def httpGet( servName=None, urlPath=None, waitTime=5 ):
	if (urlPath == None) or (servName == None):
		return (-1, None)
	srv = None
	resp = None
	
	try:
		srv = client.HTTPConnection(servName, timeout=waitTime) # connect to http site/server
	except:
		print ("HTTP Connection Exception")
		return (-1, None)
		
	print("srv:",srv)
	if srv is None:
		print ("HTTP Connection Fail")
		return (-1, None)

	try:
		srv.request( "GET", urlPath )
	except:
		print ("HTTP request Exception")
		return (-1, None)
	resp = srv.getresponse()  # read reply info headers
	print( "httpGet:", resp.status, resp.reason )
	srv.close()
	
	return (1, resp)
#_ def httpGet


def main( argv=None ):
	sysCode = sys.getdefaultencoding()
	print( "defaultencoding=", sysCode )
	vsDEBUG = os.environ["VS_DEBUG"]
	print( "vsDEBUG:", vsDEBUG )
	print( "PYTHONDEBUG=", os.getenv( "PYTHONDEBUG" ) )
	if( (vsDEBUG != "TRUE") and (1) ):
		##vs2015 debug will raise exception in sys.stdout.detach(), but just run it not
		try:
			sys.stdout = codecs.getwriter("utf_8")(sys.stdout.detach()) ##important
			##sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf_8')
		except:
			print("except error stdout")		
		try:
			sys.stdin = codecs.getwriter("utf_8")(sys.stdin.detach()) ##important
		except:
			print("except error stdin")

	out = sys.stdout
	out.flush()

	if argv is None:
		argv = sys.argv
        # etc., replacing sys.argv with argv in the getopt() call.
    #_ if

	noArgv = len(argv)
	if noArgv <= 1:
		print( "No path string input ..!" )
		return( -1 )
	#_ if
	print( "noArgv=", noArgv )
	dirIN = argv[1]
	print( "dirIN=", dirIN )
	dirIN = dirIN.strip('"')
	print( "strip dirIN="+ dirIN )
	out.flush()

	servName = "192.168.1.2:8888"

	##create playlist
	newPlName = os.path.basename(dirIN) ## 傳回路徑的最後一個部分
	print( "newPlName=[", newPlName, "]" )
	#targetDir = os.path.dirname(dirIN) ## 傳回檔案名稱中屬於路徑的部分
	paraCmd = { "cmd":"CreatePlaylist", "param1":newPlName, "param2":"0", "param3":"NoResponse" }
	paraCmdee = urllib.parse.urlencode(paraCmd)
	urlPath = "/ajquery/?" + paraCmdee
	print( "urlPath=["+ urlPath +"]" )
	rc, rsp = httpGet( servName, urlPath )
	print( "rc=", rc )


	##switch playlist index 1
	toIdx = 1
	paraCmd = { "cmd":"SwitchPlaylist", "param1":1, "param3":"js/state.json" }
	paraCmdee = urllib.parse.urlencode(paraCmd)
	urlPath = "/ajquery/?" + paraCmdee
	print( "urlPath=["+ urlPath +"]" )
	rc, rsp = httpGet( servName, urlPath, 2 )
	print( "rc=", rc )

	
	##EnqueueDir items to playlist
	eqDir = dirIN + "\\"
	print( "eqDir=[", eqDir, "]" )
	paraCmd = { "cmd":"Browse", "param1":eqDir, "param2":"EnqueueDir", "param3":"js/state.json" }
	paraCmdee = urllib.parse.urlencode(paraCmd)
	urlPath = "/ajquery/?" + paraCmdee
	print( "urlPath=["+ urlPath +"]" )
	rc, rsp = httpGet( servName, urlPath, 5 )
	print( "rc=", rc )

	if (rc != 1) or (rsp.status != 200):
		print( "Error in foobar2000 Enqueue Dir")
	#_ if
	print( "----------\n" )


#_ def main

if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
