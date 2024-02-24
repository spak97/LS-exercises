a = 7
array = [1, 2, 3]

array.each do |i|
  i += 1
end

puts a
p array

# a is untouched by the block operation. The array also is not modified because .each doesn't mutate the array.