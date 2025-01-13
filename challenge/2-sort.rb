#!/usr/bin/env ruby
# Sort integer arguments (ascending)

result = []
ARGV.each do |arg|
  # Skip non-integer arguments
  next if arg !~ /^-?[0-9]+$/

  # Convert to integer
  i_arg = arg.to_i

  # Insert into the correct position in the sorted array
  inserted = false
  result.each_with_index do |num, index|
    if i_arg < num
      result.insert(index, i_arg)
      inserted = true
      break
    end
  end

  # Append to the end if not inserted
  result << i_arg unless inserted
end

puts result
