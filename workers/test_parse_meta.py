#coding: utf8
import re
import codecs

from metadata import parse_metadata
if __name__ == "__main__":
#需要读取的文件名称放到这里

	data = open("/home/work/data/dht/torrent-test/A1DEC5568905B8A1C67B0E4C5BA4A26B8B1FD50C.torrent", "rb").read()
	print data
	info = parse_metadata(data)
	print info