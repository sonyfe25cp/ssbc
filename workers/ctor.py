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

#HASH.LOG
infos = open('hashinfos/HASH.log')
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


op = open('1.torrent', 'w')

t1 = getTorrent("DB7FC8336AB1E28DA2308D0002334EF69170E7BF")

# print t1

op.write(t1)

op.close()

# html = getHtml("http://bttohash.ouoshop.com/hashtobt.php?hash=cace0fb4e5a12eba770cdce2f0b76dca558650ac")
# print html
