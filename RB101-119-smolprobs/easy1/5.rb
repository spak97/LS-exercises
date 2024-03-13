def print_in_box(str)
  horiz_line = "+#{"-"*(str.length + 2)}+"
  empty_line = "|#{' '*(str.length + 2)}|"
  str_line = "| #{str} |"
  puts horiz_line
  puts empty_line
  puts str_line
  puts empty_line
  puts horiz_line
end

print_in_box('To boldly go where no one has gone before.')
