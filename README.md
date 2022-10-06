# Decrypt Me 

Encryption and decryption play an important role in information security and computer science. It’s used everywhere to secure the transmitted data between two entities. 

In this exercise, you'll put together a program that decrypts secret messages.

By investigating previously encrypted and decrypted messages, we believe the people who encrypt these messages use the following algorithm to encrypt them:

1. Reverse the message
2. Encode the message using a base64 encoder
3. Encrypt the message by shifting the letters

To decrypt the messages, you'll need to undo each of those layers of encryption. We'll show you how, step by step.

## Instructions

To crack the code, you'll learn a little about how each of these work, and how to break the encryption using Python.

### 1. Reversing the message

We intercepted a message that was nearly decrypted already. It was just backwards! Here's the message:
`"edoc ot nrael ot tnaw I"`

Run the code to see the backwards message printed out.

To flip the backwards message around and show the answer, you can use these two lines of code:

```python
flipped_message = backwards_message[::-1]
print("The flipped message is:", flipped_message)
```

Copy and paste that where the comment tells you to, then run the code. You should see a line that says "The flipped message is:", followed by the flipped message.

> `backwards_message[::-1]` is how to reverse a string in python.

### 2. Base64 decoding

We intercepted another partially-decrypted message. This time, it's been base64-encoded. 

> Base64 is a limited alphabet, using only 64 letters and symbols. Encoding translates each letter into several different letters or symbols.

The intercepted message is `"SSB3YW50IHRvIHdvcmsgdG9nZXRoZXI="`.

To decode the message, copy and paste this code:

```python
decoded_message = base64.b64decode(  encoded_message.encode('ascii')).decode('ascii')
print("The decoded message is: ", decoded_message)
```

Run the code, and you should see the decoded message.

> We use python's built-in `base64` library to do most of the work. It knows how to translate to and from base64.
> The other part of this snippet turns the _string_ into _bytes_ and back. It uses ASCII to turn each letter into a number.

### 3. Decrypting with a key

Another encrypted message. This one looks pretty strange!

```
N%|fsy%yt%rfpj%sj|%kwnjsix
```

It's been letter-shifted. Letter-shifting means that each letter has been moved some number of letters forward in the alphabet. Letter shifting "Hello" by 1 letter makes the "H" into an "I", the "e" into an "f", etc. Shifting by 2 letters makes "H" into "J", "e" into "g", etc.

```
0: "Hello"
1: "Ifmmp"
2: "Jgnnq"
```

The number of letters to shift by is called the **key**.

The problem is, we don't know the key that was used to decrypt the message! In `main.py`, there's already code that will try decrypting the message using the key.

Your task is to find the key that decrypts the message. We know it's a number less than 20, so try changing the `key` variable and running the code.

### 4. Putting it all together

Now we'll put all the pieces together to break every layer of encryption at the same time.

The secret message is: 

```
N\>nfZxl^r6ugLRlg8VliL:mi~GONH:_L:qf]OrNMiqgnGqf7KyNL>5NMWz^]hlXXFzhr[tiL[sg8Vlf8O{i~G{iHG5grK8NJplQr[pg7Rlg8VlgsOm_\|lg8VliL:mi~GO
```

To decrypt it, we'll need to use all our tricks in reverse. Copy and paste each of the three snippets of code.

First, we'll decrypt it using the key.

```
decrypted = ""
for letter in full_secret_message:
  decrypted += chr(ord(letter) - key)
```

Next, we'll decode it using base64:

```
decoded = base64.b64decode(decrypted.encode('ascii')).decode('ascii')
```

Finally, we'll reverse it:

```python
fully_decrypted_message = decoded[::-1]
print("The full decrypted message is:", fully_decrypted_message)
```

Run the code a final time to see the message.

*Congratulations!* You decrypted the message.
