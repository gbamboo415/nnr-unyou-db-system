#!/bin/bash -euvx
source "$(dirname $0)/conf"
export PATH="$PATH:/usr/local/bin"
trap 'rm -f $tmp-*' EXIT

# VARIABELS
tmp=/tmp/$$
order_date=$(tr -dc '0-9' <<< ${QUERY_STRING})

if [ "$order_date" = "" ] ; then
  order_date=$(date '+%Y%m%d')
fi

datafilename="$contentsdir/rawdata/${order_date}.yml"

# HTTP HEADER
echo "Content-Type: text/html"
echo

# GENERATE METADATA
op_date=$(date -d $order_date '+%Y-%m-%d')
op_prev_date=$(date -d "$order_date 1 day ago" '+%Y%m%d')
op_next_date=$(date -d "$order_date 1 day" '+%Y%m%d')
count=$(cat $datafilename | wc -l)

# OUTPUT
cat << DAT > $tmp-meta.yml
---
date: $op_date
prev_date: $op_prev_date
next_date: $op_next_date
count: $count
information:
$(cat $datafilename | sed 's/\(.*\): \(.*\)/- tnum: \1\n  formation: \2/')
---
DAT

pandoc --template=view/template.htm \
       -f markdown_github+yaml_metadata_block "$tmp-meta.yml"
