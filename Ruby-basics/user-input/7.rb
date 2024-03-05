username = "jp34"
pw = "rubysagem"

loop do
  puts "Please enter username:"
  username_try = gets.chomp
  puts "enter password:"
  pw_try = gets.chomp
  break if username_try == username && pw_try == pw
  puts "Authentication failed"
end

puts "Hello #{username}"

