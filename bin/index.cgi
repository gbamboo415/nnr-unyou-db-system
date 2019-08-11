#!/bin/bash -euvx
source "$(dirname $0)/conf"
export PATH="$PATH:/usr/local/bin"
trap 'rm -f $tmp-*' EXIT

# VARIABELS
tmp=/tmp/$$
datafilename="$contentsdir/$(tr -dc '0-9'<<< ${QUERY_STRING}).yml"
[ -f $datafilename ]

# HTTP HEADER
echo "Content-Type: text/html"
echo

# GENERATE METADATA
op_date=$(date '+%Y-%m-%d')
count=$(cat $datafilename | wc -l)

# OUTPUT
cat << DAT > $tmp-meta.yml
---
date: $op_date
count: $count
information:
$(cat $datafilename | sed 's/\(.*\): \(.*\)/- tnum: \1\n  formation: \2/')
---
DAT

pandoc --template=view/template.htm \
       -f markdown_github+yaml_metadata_block "$tmp-meta.yml"
