def reversed_number(n)
  num = n.to_s
  count = num.length 
  reversed = []
  (count + 1).times do |i|
    reversed << num[count]
    count -= 1
  end
  reversed.join.to_i
end

puts reversed_number(12345) 
puts reversed_number(12213) 
puts reversed_number(456) 
puts reversed_number(12000)  
puts reversed_number(12003) 
puts reversed_number(1)
