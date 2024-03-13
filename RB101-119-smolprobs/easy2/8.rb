puts "Please enter an integer greater than 0:"
n = gets.to_i
puts "Enter 's' to compute the sum, 'p' to compute the product."
ans = gets.chomp
arr = Array(1..n)

sum = arr.sum
prod = (1..n).inject(:*)



if ans == 's'
  puts "The sum of the integers between 1 and #{n} is #{sum}"
else
  puts "The product of the integers between 1 and #{n} is #{prod}"
end