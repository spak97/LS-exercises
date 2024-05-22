puts "What is your age?"
age = gets.to_i
puts "At what age would you like to retire?"
retire_age = gets.to_i

current_year = Time.now.year
retire_year = current_year + (retire_age - age)

puts "It's #{current_year}. You will retire in #{retire_year} " + \
"You have only #{retire_year - current_year} years of work to go!"