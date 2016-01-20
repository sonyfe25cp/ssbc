#coding=utf-8
import urllib

def getHtml(url):
	html = ''
	try:
		page = urllib.urlopen(url)
		html = page.read()
	except:
		html = ''
	return html

def getTorrent(hashinfo):
	url = "http://bt.box.n0808.com/"+hashinfo[0:2]+"/"+hashinfo[-2:]+"/"+hashinfo+".torrent"
	print url
	return getHtml(url)

def getTorrentFromTor(hashinfo):
	url = 'http://torcache.net/torrent/'+ hashinfo + ".torrent"
	print url
	return getHtml(url)

import re

def download(filepath):
	print 'begin to download', options.filename
	#HASH.LOG
	infos = open(filepath)
	_c = 0
	for _info in infos:
		_info = _info.strip('\n')
	  	# print _info
	  	_info = _info.split(" ")[7]
		# continue
		_torrent = getTorrentFromTor(_info)

		if len(_torrent) == 0 or re.search(r'404', _torrent):
			print _info + " not found"
		else:
			_f = "torrent/" + _info + '.torrent'
			_op = open(_f, 'w')
			_op.write(_torrent)
			_op.close()
			_c += 1
			print _info, 'download over'


def testDownload():

	op = open('1.torrent', 'w')

	t1 = getTorrent("DB7FC8336AB1E28DA2308D0002334EF69170E7BF")

	# print t1

	op.write(t1)

	op.close()
	print 'test download over'

# html = getHtml("http://bttohash.ouoshop.com/hashtobt.php?hash=cace0fb4e5a12eba770cdce2f0b76dca558650ac")
# print html

from optparse import OptionParser

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("-f", "--file", dest= 'filename', help='download torrents from this file', metavar = 'FILE')
	parser.add_option("-t", "--test", dest= 'testDownload', action='store_true', help='test the link and function')
	
	(options, args) = parser.parse_args()
	print 'options:', options
	print 'args:', args
	print 'filename:', options.filename
	print 'testDownload:', options.testDownload

	if options.testDownload:
		testDownload()

	if options.filename and len(options.filename) > 0:
		
		download(options.filename)

	#download()