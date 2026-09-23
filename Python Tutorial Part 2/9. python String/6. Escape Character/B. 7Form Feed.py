# Example of using the Form Feed (\f) escape character
text = "Page One\fPage Two"

print("--- Printing Raw String Representation ---")
print(repr(text))  # Displays the actual control character escape sequence

print("\n--- Printing Form Feed Output ---")
print(text)
