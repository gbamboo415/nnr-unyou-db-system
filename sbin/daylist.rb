#!/usr/local/bin/ruby2.0

# daylist.rb
# 指定された期間の日付を出力する

require 'date'

begin_day = Date.parse("20190625")
end_day = Date.parse("20190705")

begin_day.upto(end_day) do |day|
  puts day.strftime('%Y%m%d')
end
