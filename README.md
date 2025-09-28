## S3-Bucgit
While there's plenty of bucket scanning apps available, I figured I'd make one with my own twist on it. Since many of the current ones are just databases or dictionary scans, this one instead takes human tendency to re-use names and utilize that for the list.<br>

This uses GitHub's public changes to enumerate public S3 buckets. Outputs any public buckets into a .txt file in the same directory. This can then be used for manual searching or with tools such as [AWSBucketDump](https://github.com/jordanpotti/AWSBucketDump) for more effective automated searching.<br>

While this may be less effective than a curated wordlist, it's more effective at finding edge cases that people often don't think to search for. 

## Usage
        python S3-Bucgit.py [-h] [-o OUTPUT] [-t THREADS] [-f FREQUENCY] [-r RUNTIME] [-p]

        Optional arguments:
                -h, --help: show help message
                -o OUTPUT.txt: Define name of output file
                -t THREADS: Specify number of threads
                -f FREQUENCY: Frequency of new search keywords from Github in seconds
                -r RUNTIME: How long the program runs for in seconds
                -p: Enable permutations

#### Bonus info
AWS will temporarily block IPs from bucket access if scanning is too aggressive<br>
I believe in my first trial run, it found ~35 public buckets in an hour (no permutations)

## See also
Many aspects inspired by: https://github.com/jordanpotti/AWSBucketDump<br>
Search-able web bucket DB: http://buckets.grayhatwarfare.com/<br>
Same idea but with Web Certificates: https://github.com/eth0izzle/bucket-stream

## Disclaimer
For those naughty individuals: This is intended to bring attention to the security risks often neglected by cloud users. If you find any sensitive information, please disclose it to the proper parties. 