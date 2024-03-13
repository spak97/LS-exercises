a = %w(a b c d e)
puts a.fetch(7)
puts a.fetch(7, 'beats me')
puts a.fetch(7) { |index| index**2 }

# error bc index 7 doesn't exist
# 'beats me' bc 7 doesn't exist
# 49 bc 7 doesn't exist