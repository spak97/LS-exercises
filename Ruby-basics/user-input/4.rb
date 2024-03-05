
ans = nil

loop do 
  puts "do you want me to print something? (y/n)"
  ans = gets.chomp.downcase
  break if %w(y n).include?(ans)
  puts "invalid input! please type y or n"
end
puts "something" if ans == 'y'


