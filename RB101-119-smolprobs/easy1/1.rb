def repeat(str, int)
  count = 0
  loop do
    puts str
    count += 1
    break if count == int
  end
end

repeat("hello", 3)