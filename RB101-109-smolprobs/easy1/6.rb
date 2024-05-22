def triangle(n)
  count = n
  (n+1).times do |i|
    puts "#{" " * count}#{"*" * i}"
    count -= 1
  end
end

triangle(5)
triangle(9)