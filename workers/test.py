import libtorrent as lt
import time
 
def magnet2t(link,tfile):
    sess = lt.session()
    params = {
             "save_path": './tfile/',
             "storage_mode":lt.storage_mode_t.storage_mode_sparse,
             "paused": True,
             "auto_managed": True,
             "duplicate_is_error": True
           }
 
    handle = lt.add_magnet_uri(sess, link, params)
 
    while (not handle.has_metadata()):
        time.sleep(5)
        print handle.has_metadata()
  
    torinfo = handle.get_torrent_info()
  
    fs = lt.file_storage()
    for f in torinfo.files():
        fs.add_file(f)
 
    torfile = lt.create_torrent(fs)
    torfile.set_comment(torinfo.comment())
    torfile.set_creator(torinfo.creator())
     
    #for i in xrange(0, torinfo.num_pieces()):
    #    hashes = torinfo.hash_for_piece(i)
    #    torfile.set_hash(i, hashes)
 
    for url_seed in torinfo.url_seeds():
        torfile.add_url_seed(url_seed)
 
    for http_seed in torinfo.http_seeds():
        torfile.add_http_seed(http_seed)
 
    for node in torinfo.nodes():
        torfile.add_node(node)
 
    for tracker in torinfo.trackers():
        torfile.add_tracker(tracker)
 
    torfile.set_priv(torinfo.priv())
  
    t = open(tfile, "wb")
    t.write(lt.bencode(torfile.generate()))
    t.close()
    print '%s  generated!'% tfile
 
def main():
    f= open('it.txt','r')
    magnet_list = f.read().split('\n')
    f.close()
    for i in range(len(magnet_list)):
        if magnet_list[i] != '':
            magnet2t(magnet_list[i],'%s.torrent'% str(i))
     
 
if __name__ == '__main__':
    main()