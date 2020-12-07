# Data aggregation for Cosmic Shambles Live show (Dec 2020)

1) Use this branch of the aggregation repo: https://github.com/zooniverse/aggregation-for-caesar/tree/users-in-question-reducer

2) Make a new folder for the data export and put Zooniverse classification dump in it

3) Edit `aggregation_script.sh` line 3 with this folder

3) Edit `aggregation_script.sh` line 4 with name of csv export 

4) Optionally edit the last number on `aggregation_script.sh` line 10 with vote count threshold for saving to the output file (useful for saving time on API calls to panoptes).  Set to `0` to keep all subjects in the output file.

5) Run `./aggregation_script.sh` and the output file will be named `candidates.csv` and be placed in the folder made in step 2.
