name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Helo, {full_name.title()}!")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = "python "
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.strip()
print(favorite_language)
