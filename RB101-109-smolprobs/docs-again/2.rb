require 'date'

puts Date.civil
puts Date.civil(2016)
puts Date.civil(2016, 5)
puts Date.civil(2016, 5, 13)

# first line puts default date value
# subsquent lines puts the dates in the parenthesis. If not provided, puts default for date and month.