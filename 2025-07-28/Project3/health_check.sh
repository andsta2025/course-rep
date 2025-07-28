#!/bin/bash
URL="http://localhost"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS" -ne 200 ]; then
    echo "ERROR: Service down" >> /var/log/app_health.log
    exit 1
fi

echo "Service OK - $(date)" >> /var/log/app_health.log
