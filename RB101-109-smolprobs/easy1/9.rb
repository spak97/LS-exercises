def center_of(str)
  if str.length % 2 != 0
    str[(str.length / 2)]
  else 
    str[(str.length / 2) - 1] + str[(str.length / 2)]
  end
end
  
puts center_of('I love ruby') 
puts center_of('Launch School')
puts center_of('Launch') 
puts center_of('Launchschool') 
puts center_of('x') 