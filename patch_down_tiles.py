import urllib2
import os, os.path
import time

url ='http://c.tile.openstreetmap.org'
output_dir = 'tiles'

#z/x/y
s1="http://a.tile.openstreetmap.org/16/54870/26762.png"
s2="http://a.tile.openstreetmap.org/16/54884/26779.png"

# lv 13
# zoom =13
# min_y = 3345
# max_y = 3349

# min_x = 6858
# max_x = 6860

# lv 14
# zoom = 14
# min_y = 6689
# max_y = 6696

# min_x = 13717
# max_x = 13722

# zoom = 15
# min_y = 13380
# max_y = 13390

# min_x = 27434
# max_x = 27443

#lv 16
# zoom = 16
# min_y = 26762
# max_y = 26779

# min_x = 54870
# max_x = 54884

#lv 17
"http://c.tile.openstreetmap.org/17/109741/53530.png"
'http://a.tile.openstreetmap.org/17/109769/53550.png'

zoom =17
min_x = 109741
max_x = 109769

min_y = 53530
max_y = 53550


for y_index in range(min_y, max_y+1):
	for x_index in range(min_x, max_x+1):
		tile_url = url + "/%d/%d/%d.png" % (zoom, x_index,y_index )
		print "<h5>"+tile_url+"</h5>"
		print "<img src='"+tile_url+"'>"
		
		path = "%s/%d/%d" % (output_dir, zoom, x_index)
		filename = path + "/%d.png" % y_index
		if not os.path.exists(path):
			os.makedirs(path)

		data = None
		if not os.path.exists(filename) :
#					need_retry = False
			webFile = None
			
		
			download_succeeded = False
			#for try_nr in range(1, max_retries+2): # +1 for starting with 1, +1 bcs range goes to n-1 and we want min 1 retry
			for try_nr in range(1, 2):
				try:
					#print "trying %s" % tile_url

					req = urllib2.Request(tile_url, headers={'User-Agent' : "Magic Browser"}) 
					webFile = urllib2.urlopen( req )

					data = webFile.read()
					download_succeeded = True
					break
				except Exception, e:
					print e
					print "%s failed on try nr %d" % (tile_url, try_nr)
#							need_retry = True
					# give the server some time, maybe that helps
					time.sleep(50)
			
			if not download_succeeded:
				time.sleep(10)
				continue;

			localFile = open(filename, 'wb')
			localFile.write(data)
			webFile.close()
			localFile.close()
