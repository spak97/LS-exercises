a = "Xyzzy"

def my_value(b)
  b[2] = '-'
end

my_value(a)
puts a

# prints "Xy-zy". Strings are mutable while numbers aren't. And string[i] is a mutating method.