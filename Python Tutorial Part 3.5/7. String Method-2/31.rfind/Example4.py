txt = "Hello, welcome to my world."

print(txt.find("q")) 

try:
    print(txt.index("q"))
except ValueError:
    print("Character not found")