#===========#
# Functions #
#===========#
def caesar(original_text, shift_amount, encode_or_decode, alphabet):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+= letter
        else:
            shifted = alphabet.index(letter) + shift_amount
            shifted %= len(alphabet)  # 0-25
            output_text += alphabet[shifted]
    return output_text

#===========#
#  App Run  #
#===========#
def run():
    import art
    import string
    #===========#
    # Variables #
    #===========#
    print(art.logo)
    alphabet = [char for char in string.ascii_lowercase] # get all english alphabets in lowercase and put them in a list
    
    #===========#
    # Main Loop #
    #===========#
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n--> ").lower()
        if direction == "encode" or direction == "decode": # if something else restart the loop
            text = input("Type your message:\n--> ").lower() # just to look more cool added an arrow :)
            try: # check if the user entered a text in shift num instead of a number
                shift = int(input("Type the shift number:\n--> "))
            except ValueError:
                print("Shift number is not a text!\n")
                continue # if ValueError restart the loop from the beginning
            caesar_result = caesar(text, shift, direction, alphabet) # get the result
            print(f"Here is the {direction}d result: {caesar_result}") # print it
            
            if input("Enter anything if you wanna go again. otherwise, type 'no'. \n--> ").lower() == "no": # if 'no' then Goodbye otherwise app works!
                print("Goodbye")
                break
            print("") # A line break for readability
if __name__ == '__main__': # run
    run()
