import requests
def download_file(url, name):
    local_filename = 'videos' + name + '.mp4'
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
url = 'https://www38.o0-1.com/token=wJCBhgaDBentUsr1TY1FLw/1596808097/1.53.0.0/109/8/f2/378e79422df723d81be77a6464316f28-720p.mp4'
download_file(url)
