import requests
from queue import Queue
from threading import Thread
from argparse import ArgumentParser
import time

with open("permutations.txt") as file:
    perms = [line.rstrip() for line in file]

que = Queue()
found = set()
api = 'https://api.github.com/events'
args = None
file = None

def gitnames():
    events = requests.get(api).json()
    for commit in events:
        repopath = commit["repo"]["name"]
        owner = repopath[:repopath.find("/")]
        repo = repopath[repopath.find("/")+1:]

        actor = commit["actor"]["login"]
        if (actor != "Copilot") and ("[bot]" not in actor) and (actor != owner):
            que.put(actor)
            if args.permutate:
                permutations(actor)
        if (owner != repo):
            que.put(owner)
            if args.permutate:
                permutations(owner)
        que.put(repo)
        if args.permutate:
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
    global args,file

    parser = ArgumentParser()
    parser.add_argument("-o", "--output", default='buckets.txt', required = False, help="Output file name")
    parser.add_argument("-t", "--threads", type=int, default=4, required = False, help="Number of threads. Higher speed is more likely to get blocked by AWS")
    parser.add_argument("-f", "--freq", type=int, default=60, required = False, help="How often in seconds new names are collected")
    parser.add_argument("-r", "--runtime", type=int, default=3600, required = False, help="How long the program will run for, in seconds. Default: 3600 (1 hour)")
    parser.add_argument("-p", "--permutate", action='store_true', help="Enable permutations")
    args = parser.parse_args()
    
    file = open(args.output, 'a+') ###
    file.seek(0)
    for line in file:
        found.add(line.strip())

    threads = args.threads ###
    for _ in range(threads):
        t = Thread(target=trybuckets)
        t.daemon = True
        t.start()
    
    endtime = time.time() + args.runtime ###
    while time.time() < endtime:
        if que.qsize() < 5:
            gitnames()
        time.sleep(args.freq)###

if __name__ == "__main__":
    main()