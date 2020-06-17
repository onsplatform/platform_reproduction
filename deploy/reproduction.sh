#!/usr/bin/env bash
timestamp=`date +%Y/%m/%d-%H:%M:%S`
echo "System path is $PATH at $timestamp"

export SCHEMA_URI=http://schema/api/v1/
export EVENT_MANAGER_URI=http://event_manager:8081/
export RABBIT_MQ=rabbitmq

cd /var/cron/reproduction

/usr/local/bin/pipenv run python reproduction/reproduction_executor.py