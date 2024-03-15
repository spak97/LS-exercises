# return true if all alphabetic chars are upper
# else return false
def uppercase?(str)
  if str == str.upcase
    return true
  else 
    return false
  end
end

puts uppercase?('t')
puts uppercase?('T')
puts uppercase?('Four Score') 
puts uppercase?('FOUR SCORE') 
puts uppercase?('4SCORE!') 
puts uppercase?('') 