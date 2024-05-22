def real_palindrome?(str)
  str = str.upcase.delete('^A-Z0-9')
  str == str.reverse
end

puts real_palindrome?('madam') 
puts real_palindrome?('Madam')           # (case does not matter)
puts real_palindrome?("Madam, I'm Adam")  # (only alphanumerics matter)
puts real_palindrome?('356653') 
puts real_palindrome?('356a653') 
puts real_palindrome?('123ab321') 