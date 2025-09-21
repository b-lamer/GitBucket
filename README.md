## GitBucket
While there's plenty of bucket scanning apps available, I figured I'd make one with my own small twist on it. Since many of the current ones are just databases or dictionary scans, I figured I'd make one that takes human tendency to re-use names and utilize that for the list.<br>

This uses GitHub's public changes to enumerate public S3 buckets. Outputs any public buckets into a .txt file in the same directory. This can then be used for manual searching or with tools such as [AWSBucketDump](https://github.com/jordanpotti/AWSBucketDump) for more effective automated searching.

#### Bonus info
Variables such as thread count, total runtime, and name scan frequency can all be changed easily in the code<br>
I believe in my first trial run, it found ~24 public buckets in an hour (with the default settings)

## Credits
Many inspiration derived from: https://github.com/jordanpotti/AWSBucketDump<br>
Definitely check out this repo if you haven't yet

## To Do:
- Allow extension of wordlist by adding current words to set
- Include different permutations of files of the same name
- Option to output links or just bucket names
- Potentially expand to other feeds as Apple/Android apps, Stackoverflow users, etc.

## Disclaimer
For those naughty individuals: This is for bringing attention to the security risks often neglected by cloud users. If you find any sensitive information, please disclose it to the proper parties. 