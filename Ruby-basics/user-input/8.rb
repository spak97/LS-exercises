# user enters two integers
# prints result of dividing first by the second
# second number must not be 0
# you must validate the input is an integer

def valid_number?(number_string)
  number_string.to_i.to_s == number_string
end

nume = nil
denom = nil

loop do
  puts "enter the numerator:"
  nume = gets.chomp
  
  break if valid_number?(nume) 
  puts "invalid input. integers only."
end

loop do
  puts "enter the denominator:"
  denom = gets.chomp

  if denom == '0'
    puts "denom can't be 0"
  else
    break if valid_number?(denom)
    puts "invalid input. integers only."
  end
end

result = nume.to_i / denom.to_i

puts "#{nume} / #{denom} = #{result}"



