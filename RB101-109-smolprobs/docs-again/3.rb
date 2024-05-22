def my_method(a, b = 2, c = 3, d)
  p [a, b, c, d]
end

my_method(4, 5, 6)

# assigns non-default args first then goes in order to assign default args
# so returns [4, 5, 3, 6]