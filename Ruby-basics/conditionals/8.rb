status = ['awake', 'tired'].sample

alert = if status == 'awake'
          'Be productive'
        else
          'Go sleep'
        end
        
puts alert