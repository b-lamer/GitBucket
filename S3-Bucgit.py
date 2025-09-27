import requests
from queue import Queue
from threading import Thread
import time

with open("permutations.txt") as file:
    perms = [line.rstrip() for line in file]

que = Queue()
found = set()
threads = 4 #Usually get rate limited hard with more than 4
endtime = time.time() + 3600 #Run for 1hr
api = 'https://api.github.com/events'
file = open('buckets.txt', 'a+')

def gitnames():
    events = requests.get(api).json()
    for commit in events:
        repopath = commit["repo"]["name"]
        owner = repopath[:repopath.find("/")]
        repo = repopath[repopath.find("/")+1:]

        actor = commit["actor"]["login"]
        if (actor != "Copilot") and ("[bot]" not in actor) and (actor != owner):
            que.put(actor)
            permutations(actor)
        if (owner != repo):
            que.put(owner)
            permutations(owner)
        que.put(repo)
        permutations(repo)
    
def trybuckets():
    while True:
        item = que.get()
        print("trying: http://" + item + '.s3.amazonaws.com')
        try:
            response = requests.get('http://'+item+'.s3.amazonaws.com')
            if response.status_code == 200:
                if ("Content" in response.text) and (item not in found):
                    print("Item found: " + item)
                    found.add(item)
                    file.write(item + '\n'); file.flush()
        except:
            pass
        que.task_done()

def permutations(orig):
    for perm in perms:
        que.put(orig + perm)

def main():
    file.seek(0)
    for line in file:
        found.add(line.strip())
    for _ in range(threads):
        t = Thread(target=trybuckets)
        t.daemon = True
        t.start()
    while time.time() < endtime:
        if que.qsize() < 5:
            gitnames()
        time.sleep(60) #New links every 60s to allow program to catch up. Can lower if permutations are off.

if __name__ == "__main__":
    main()