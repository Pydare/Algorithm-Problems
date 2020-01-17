import requests
eeg405_url = 'https://schoolextras.wordpress.com/eeg-405.pdf/'
r = requests.get(eeg405_url, stream=True)

with open("405Note",'wb') as pdf:
    for chunk in r.iter_content(chunk_size=1024): 
        # writing one chunk at a time to pdf file 
        if chunk: 
            pdf.write(chunk)