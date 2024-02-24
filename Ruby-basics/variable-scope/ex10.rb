a = 7
array = [1, 2, 3]

def my_value(ary)
  ary.each do |b|
    a += b
  end
end

my_value(array)
puts a

# since this is a method declaration, a is initialized but method doesn't have access to it.
# can't += to an un-initialized variable, so returns an error.