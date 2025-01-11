message = ("One of Python's strengths is its diverse community and"
           " extensive library.")

print(message)

# 2-3. Personal message:
name = "Eric"
message = f"{name}, would you like to learn some Python today?"
print(f"Hello, {message}")

# 2-4. Name cases:
print(name.title())  # Capitalize the first letter
print(name.lower())  # Convert all letters to lowercase
print(name.upper())  # Convert all letters to uppercase

# 2-5. Famous quote:
famous_quote = ("I have not failed. I've just found"
                " 10,000 ways that won't work.")
quote_author = "Mark Twain"
print(f"{quote_author} once said, '{famous_quote}'")

# 2-6. Famous quote 2:
famous_person = "Albert Einstein"
famous_quote = ("\"A person who never made a mitake"
                " never tried anything new\"")
print(f"{famous_person} once said, '{famous_quote}'")

# 2-7. Stripping Names:
another_name = "\tErik\n"
print(another_name.strip())  # Remove leading and trailing whitespace
print(another_name.lstrip())  # Remove leading whitespace
print(another_name.rstrip())  # Remove trailing whitespace
