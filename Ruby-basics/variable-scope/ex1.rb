# 17.. i am wrong. It prints 7. Reassignment doesn't mutate a variable. 

a = 7

def my_value(b) 
  b += 10
end

puts my_value(a)
puts a
