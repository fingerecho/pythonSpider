import requests

#url = "https://zoink.ch/torrent/Jimmy.Kimmel.2017.05.11.Ewan.McGregor.WEB.x264-TBS[eztv].mkv.torrent"
def downTorrentFile(url,name):
    r = requests.get(url)
    with open("./../downresource/"+name+".torrent","ab+") as f:
        for chunck in r.iter_content(1024):
            f.write(r.content)
            f.flush()


