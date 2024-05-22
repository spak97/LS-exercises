def palindromic_number?(n)
  n.to_s == n.to_s.reverse
end

puts palindromic_number?(34543) 
puts palindromic_number?(123210)
puts palindromic_number?(22) 
puts palindromic_number?(5) 