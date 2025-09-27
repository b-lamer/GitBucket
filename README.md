## GitBucket
While there's plenty of bucket scanning apps available, I figured I'd make one with my own twist on it. Since many of the current ones are just databases or dictionary scans, I figured I'd make one that takes human tendency to re-use names and utilize that for the list.<br>

This uses GitHub's public changes to enumerate public S3 buckets. Outputs any public buckets into a .txt file in the same directory. This can then be used for manual searching or with tools such as [AWSBucketDump](https://github.com/jordanpotti/AWSBucketDump) for more effective automated searching.<br>

While this may be less effective than a curated wordlist, it's more effective at finding edge cases that people often don't think to search for. 

## Usage
        python gitbucket.py

        Optional arguments will be added in the future

#### Bonus info
Variables such as thread count, total runtime, and name scan frequency can all be changed easily in the code<br>
I believe in my first trial run, it found ~35 public buckets in an hour (with the default settings)

## See also
Many aspects inspired by: https://github.com/jordanpotti/AWSBucketDump<br>
Search-able web bucket DB: http://buckets.grayhatwarfare.com/<br>
Same idea but with Web Certificates: https://github.com/eth0izzle/bucket-stream

## To Do
- Remove more white noise
- Allow arguments (threads, name/link output, filename, timing, total runtime)
- Potentially expand to other feeds as Apple/Android apps, Stackoverflow users, etc.

## Disclaimer
For those naughty individuals: This is intended to bring attention to the security risks often neglected by cloud users. If you find any sensitive information, please disclose it to the proper parties. 