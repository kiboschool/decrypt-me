# Program: Decrypt the messages
# Author: You (with some help from Kibo)
# This program decrypts secret messages.
# Follow the steps in the instructions to decrypt the messages!

# This line imports the base64 library
import base64

### Part 1
### Reversing the message
print("--- Part 1 ---")

backwards_message = "edoc ot nrael ot tnaw I"
print("The backwards message is:", backwards_message)
# TODO: Copy and paste the code to flip the message here


### Part 2
### Base64 decoding
print("\n--- Part 2 ---")

encoded_message = "SSB3YW50IHRvIHdvcmsgdG9nZXRoZXI="
print("The encoded message is", encoded_message)
# TODO: Copy and paste the code to decode the message here


### Part 3
### Decrypting with a key
print("\n--- Part 3 ---")

encrypted = "N%|fsy%yt%rfpj%sj|%kwnjsix"
print("The encrypted message is", encrypted)

# TODO: Find the key that correctly decrypts the message
key = 1
print("Trying key:", key)

decrypted = ""
for letter in encrypted:
  decrypted += chr(ord(letter) - key)

print("The decrypted message is:", decrypted)


### Part 4
### Putting it all together
print("\n--- Part 4 ---")

full_secret_message = 'N\\>nfZxl^r6ugLRlg8VliL:mi~GONH:\x7f_L:qf]OrNMiqgnGqf7KyNL>5NMWz^]hlXXFzhr[tiL[sg8Vlf8O{i~G{iHG5grK8NJplQr[pg7Rlg8VlgsOm_\\|lg8VliL:mi~GO'

print("The full secret message is", full_secret_message)

# TODO: Decrypt the message with the key


# TODO: Use base64 to decode the message


# TODO: Reverse the message

