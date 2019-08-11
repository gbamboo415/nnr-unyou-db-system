!/bin/bash
source "$(dirname $0)/conf"

readonly requested_type=$(
    echo "${PATH_INFO}" |
    sed  's!/!!'        |
    awk  'BEGIN{FS="/"}
          $1=="raw"{print "rawdata"}
          $1=="json"{print "json"}'
)

readonly requested_file=$(
    echo "${PATH_INFO}" |
    sed  's!/!!'        |
    awk  'BEGIN{FS="/"}
          {print "rawdata/" $2 ".yml"}'
)

readonly viewdate=$(
    echo "${PATH_INFO}" |
    sed  's!/raw/!!'    |
    tr -dc '0-9'
)

if [ $requested_type = "rawdata" ]; then
    echo -e "Content-Type: text/plain; charset: UTF-8"
    echo -e "Content-Language: ja\n"
    cat "${contentsdir}/$requested_file"
elif [ $requested_type = "json" ]; then
    echo -e "Content-Type: application/json; charset: UTF-8"
    echo -e "Content-Language: ja\n"
    cat "${contentsdir}/$requested_file" | ruby $(dirname $0)/yaml2json.rb
else
    echo -e "Content-Type: application/json; charset: UTF-8"
    echo -e '{"error":"未対応のリクエストの種類"}'
fi
