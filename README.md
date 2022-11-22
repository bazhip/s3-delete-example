# s3-delete-example

Just a quick script to delete the last X deployements. This is assuming a root directory containing folders with deployments, each with an index.html file.

Pass in `--bucket` to specify the s3 bucket `--x` as a parameter to keep the last x deployments. For example `s3-delete.py --x=5` to purge all but the last 5 deployments.
