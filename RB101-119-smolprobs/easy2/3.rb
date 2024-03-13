puts "What is the bill?"
bill = gets.to_f
puts "What is the tip percentage?"
tip_percent = gets.to_f
tip = bill * (tip_percent * 0.01)

puts "The tips is $#{tip.round(2)}"
puts "The total is $#{(bill + tip).round(2)}"