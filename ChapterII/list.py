bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# 3.1. Names:
names = ['Alice', 'Bob', 'Charlie', 'David']
print(f"All names are :{names[0]}, {names[1]}, {names[2]}, {names[3]}")

# 3.2. Greetings:
print(f"Hello, {names[0].title()}!")
print(f"Hello, {names[1].title()}!")
print(f"Hello, {names[2].title()}!")
print(f"Hello, {names[3].title()}!")

# 3.3. Your own list:
vehicles = ['car', 'motorcycle', 'bicycle', 'truck']
print(f"I would like to own a {vehicles[2].title()}!")

# Changing, Adding, and Removing Elements:
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)

motocycles.append('ducati')
print(motocycles)

# We can easily build list dynamically:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# inserting elements into a list:
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list:
del motocycles[0]
print(motocycles)

popped_motorcycle = motocycles.pop()
print(f"I just popped {popped_motorcycle} from the list of {motocycles}.")
