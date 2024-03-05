input = nil
no_of_lines = nil

loop do
  puts 'How many output lines do you want? Enter a number >= 3 (Q to quit):'
  input = gets.chomp
  no_of_lines = input.to_i

  break if input.downcase == 'q'

  if no_of_lines < 3
    puts "That's not enough lines."
  elsif no_of_lines >= 3
    while no_of_lines > 0
      puts "Launch School is the best!"
      no_of_lines -= 1
    end
  end
end



