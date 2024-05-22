# return true only if exactly one of the args is truthy
def xor?(arg1, arg2)
  if (arg1 || arg2) 
    if arg1 && arg2
      false
    else
      true
    end
  else
    false
  end
end


# overcomplicates a fairly easy problem to solve
# interesting that I couldn't figure out the simple solution
  
puts xor?(5.even?, 4.even?) 
puts xor?(5.odd?, 4.odd?) 
puts xor?(5.odd?, 4.even?)
puts xor?(5.even?, 4.odd?)