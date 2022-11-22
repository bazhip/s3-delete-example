# s3-delete-example

Just a quick script to delete the last X deployements. This is assuming a root directory containing folders with deployments, each with an index.html file.

Pass in `--x` as a parameter to keep the last x deployemnts. For example `s3-delete.py --x=5` to purge all but the last 5 deployments.
