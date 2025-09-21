import requests
from queue import Queue
from threading import Thread
import time

que = Queue()
found = set()
threads = 1 #Change for your desired # of threads, usually won't need more than 1 or 2 with default timing
endtime = time.time() + 3600 #Run for 1hr
api = 'https://api.github.com/events'
file = open('gitbuckets.txt', 'w')

def gitnames():
    events = requests.get(api).json()
    for commit in events:
        repopath = commit["repo"]["name"]
        owner = repopath[:repopath.find("/")]
        repo = repopath[repopath.find("/")+1:]

        actor = commit["actor"]["login"]
        if (actor != "Copilot") and ("[bot]" not in actor) and (actor != owner):
            que.put('http://'+actor+'.s3.amazonaws.com')
        que.put('http://'+owner+'.s3.amazonaws.com')
        que.put('http://'+repo+'.s3.amazonaws.com')

def trybuckets():
    while True:
        item = que.get()
        print("trying: " + item)
        try:
            response = requests.get(item)
            if response.status_code == 200:
                if ("Content" in response.text) and (item not in found):
                    print("Item found: " + item)
                    found.add(item)
                    file.write(item + '\n'); file.flush()
        except:
            pass
        que.task_done()

def main():
    for _ in range(threads):
        t = Thread(target=trybuckets)
        t.daemon = True
        t.start()
    
    while time.time() < endtime:
        if que.qsize() < 5:
            gitnames()
        print(found)
        time.sleep(30) #New links every 30 seconds to avoid repeat scanning, change if needed.

if __name__ == "__main__":
    main()
