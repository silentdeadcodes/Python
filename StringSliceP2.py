# Now we will be using the actual 'slice' function where we use commas ',' instead of the colons ':'
# but it works the same way.


# We can use negative index which is from right to left as most of the webs don't have the same 
# stopping index.
# And when you start from the right side the index will start from 1 and from the left 0.
# Very useful for getting the websites name and not having to do the same thing again and again.
url = 'https://google.com'
url2 = 'https://wikipedia.com'

slice = slice(8, -4)

print(url[slice])
print(url2[slice])
