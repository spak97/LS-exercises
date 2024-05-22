def palindrome?(str)
  length = str.length
  half = str.length / 2
  
  if length % 2 != 0 
    if str[0, half] == str[half + 1, length].reverse
      true
    else
      false
    end
  elsif length % 2 == 0
    if str[0, half] == str[half, length].reverse
      true 
    else
      false
    end
  end
end

# this is overcomplicating a very simple problem just like the last one.
# interesting that I missed the obvious answer struggled so much with this.

puts palindrome?('madam') 
puts palindrome?('Madam')       # (case matters)
puts palindrome?("madam i'm adam")  # (all characters matter)
puts palindrome?('356653') 

