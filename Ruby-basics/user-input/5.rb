puts "How many output lines do you want? Enter a number >= 3:"

ans = gets.chomp.to_i
count = 0

loop do
  count += 1
  puts "Launch School is the best!"
  break if count == ans
end