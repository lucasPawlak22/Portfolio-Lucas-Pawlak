#!/bin/env python3

from __future__ import unicode_literals
import pandas as pd
import youtube_dl

ffmpeg = "/usr/bin/ffmpeg"


chewing_encoded = '/m/03cczk'
df = pd.read_csv('./unbalanced_train_segments.csv', delimiter=', ')

chewing = df[df['labels'].str.contains(chewing_encoded)]
print(chewing)

def create_yt_link(id, start, end):
    return 'youtu.be/' + id + '&start=' + start + '&end=' + end


for i, row in enumerate(chewing.values):
    outtmpl = str(i) + '.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    print("row number =",i, "row=", row[1])

    ytid = row[0]
    start = str(int(row[1]))
    end = str(int(row[2]))

    link = create_yt_link(ytid, start, end)
    print(link)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


