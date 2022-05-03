from concurrent.futures import ThreadPoolExecutor
from requests import get, head
import time
import os


class Downloader:
    def __init__(self, url, name):
        self.url = url
        self.num = min(32, (os.cpu_count() or 1) + 4)
        self.name = name
        self.getsize = 0
        r = head(self.url, allow_redirects=True)
        self.size = int(r.headers['Content-Length'])

    def down(self, start, end, chunk_size=10240):
        headers = {'range': f'bytes={start}-{end}'}
        r = get(self.url, headers=headers, stream=True)
        with open(self.name, "rb+") as f:
            f.seek(start)
            for chunk in r.iter_content(chunk_size):
                f.write(chunk)
                self.getsize += chunk_size

    def main(self):
        start_time = time.time()
        f = open(self.name, 'wb')
        f.truncate(self.size)
        f.close()
        tp = ThreadPoolExecutor(self.num)
        futures = []
        start = 0
        for i in range(self.num):
            end = int((i+1)/self.num*self.size)
            future = tp.submit(self.down, start, end)
            futures.append(future)
            start = end+1
        while True:
            process = self.getsize/self.size*100
            last = self.getsize
            time.sleep(1)
            curr = self.getsize
            down = (curr-last)/1024
            if down > 1024:
                speed = f'{down/1024:6.2f}MB/s'
            else:
                speed = f'{down:6.2f}KB/s'
            print(f'Process: {process:6.2f}% | Speed: {speed}', end='\r')
            if process >= 100:
                print(f'Process: {100.00:6}% | Speed:  00.00KB/s', end=' | ')
                break
        tp.shutdown()
        end_time = time.time()
        total_time = end_time-start_time
        average_speed = self.size/total_time/1024/1024
        print(f'Total-time: {total_time:.0f}s | Average-speed: {average_speed:.2f}MB/s')


if __name__ == '__main__':
    Downloader('https://1251316161.vod2.myqcloud.com/007a649dvodcq1251316161/2074194f5285890808508755340/Q5TVeeaCdf0A.mp4', 'test.mp4').main()
