def caesar_cipher(text, shift, mode):

  result = ""
  # traverse text
  for char in text:
    # Encrypt uppercase characters
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    # Encrypt lowercase characters
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    # Leave spaces and other characters intact
    else:
      result += char
  
  if mode == 'decrypt':
    # Decrypt by shifting in the opposite direction
    shift = -shift
    result = caesar_cipher(result, shift, 'encrypt')

  return result

def main():
  text = input("Enter your message: ")
  shift = int(input("Enter the shift value: "))
  mode = input("Enter mode (encrypt/decrypt): ")

  result = caesar_cipher(text, shift, mode)
  print("The", mode, "ed text is:", result)

if __name__ == "__main__":
  main()
