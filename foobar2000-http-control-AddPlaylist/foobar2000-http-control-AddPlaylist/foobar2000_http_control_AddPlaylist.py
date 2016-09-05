##create new playlist by HTTP Control
#http://127.0.0.1:8888/ajquery/?cmd=CreatePlaylist&param1=New+Playlist&param3=NoResponse


import sys, os
import codecs
#import http
from http import client
#import urllib
import urllib.parse
import urllib.request

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

#_ def main

if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
