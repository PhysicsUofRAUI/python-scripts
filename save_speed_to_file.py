import speedtest
import time
from datetime import datetime
import csv

now = datetime.now()
formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

st = speedtest.Speedtest()

data = ["time", "Download", "upload"]

with open("data.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data)

while True :
    now = datetime.now()
    formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    down = st.download()/1000000
    up = st.upload()/1000000
    data = [formatted_timestamp, down, up]

    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
    
    time.sleep(900)
