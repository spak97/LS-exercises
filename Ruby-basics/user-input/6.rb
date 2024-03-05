pw = "rubysagem"

loop do
  puts "Please enter the password:"
  ans = gets.chomp
  break if ans == pw
  puts "Invalid password!"
end

puts "Hello"