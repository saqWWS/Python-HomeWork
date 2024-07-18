def is_palindrome(string):
        
    if len(string) <= 1:
        return True
            
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
                    
    else:
        return False


txt = input("Enter your word:\t").lower()

if is_palindrome(txt):
    print("YES!")
    
else:
    print("NO!")
