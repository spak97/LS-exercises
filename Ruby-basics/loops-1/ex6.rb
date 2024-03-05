numbers = Array(0..99)
keep_print = true
count = 0

while keep_print
  puts numbers.sample
  count += 1
  keep_print = false if count == 5
end