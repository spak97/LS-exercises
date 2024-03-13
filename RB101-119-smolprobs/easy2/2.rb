puts "Enter the length of the room in meters:"
length = gets.chomp.to_i
puts "Enter the width of the room in meters:"
width = gets.chomp.to_i

area_m = width * length
area_ft = area_m * 10.7639

puts "The area of the room is #{area_m} square meters (#{area_ft} square feet)."