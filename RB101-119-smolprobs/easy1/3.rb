def stringy(n)
  str = ''
  n.times do |i|
    if i % 2 == 0
      str.concat("1")
    else
      str.concat("0")
    end
  end
  str
end

puts stringy(6) == '101010'
puts stringy(9) == '101010101'
puts stringy(4) == '1010'
puts stringy(7) == '1010101'