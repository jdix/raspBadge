#!/bin/bash


cd $(dirname $0)
echo "" >> output.log
echo "Running at: `date`" >> output.log
python google_manager.py >>output.log
