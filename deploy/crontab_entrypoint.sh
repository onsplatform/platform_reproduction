#!/usr/bin/env bash

# Setup a cron schedule
echo "* * * * * /reproduction.sh >> /var/cron/reproduction/log/reproduction_cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt