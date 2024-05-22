puts "Please write word or multiple words: "
ans = gets.chomp
chars = ans.split(' ').join

puts "There are #{chars.length} characters in #{ans}"