#! /bin/bash

## Extract
echo "Extracting..."
# Get temperature reading and append to log
python3 get_temp.py --lat=39.828118 --lon=-104.936449 >> temperature.log

# Buffer last N readings
# tail -5 temperature.log > temperature.log

## Transform
echo "Transforming..."
# Call get_stats.py to aggregate readings
python3 get_stats.py --log=temperature.log --output=temp_stats.json

## Load
echo "Loading..."
# Push stats to dashboard
# TODO