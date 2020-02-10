#!/usr/bin/env bash

# This simple database appends key-value pair to a log. To read, it searches
# the log from top-down and returns the most recent entry.
# Write time complexity: O(1)
# Read time complexity: O(n)

# Read is slow. Can improve using indexes, a separate data structure to
# improve lookup time. However, writes are slower with indexes because
# you need to write to the log and separate data structure.

# Issues real databases face: concurrency control, reclaiming disk space,
# partial records, error handling

db_set () {
    echo "$1,$2" >> database
}

db_get () {
    grep -e "^$1," database | sed "s/^$1,//" | tail -1
}

# Uncomment below to test
# db_set 117 '{"name":"Master Chief","type":"Spartan","location":"unknown"}'
# db_get 117
