

upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alpha = "abcdefghijklmnopqrstuvwxyz"

def hack(encrypted_msg):
    
    key = 1
    result = ""
    
    while key <= 26:
        
        i = 0
        while i < len(encrypted_msg):
            if encrypted_msg[i] >= 'A' and encrypted_msg[i] <= 'Z':
                    index_count = upper_alpha.index(encrypted_msg[i]) - key
            
                    if index_count < 0:
                        index_count += 26
                    result += upper_alpha[index_count]
                    
            elif encrypted_msg[i] >= 'a' and encrypted_msg[i] <= 'z':
                
                index_count = lower_alpha.index(encrypted_msg[i]) - key
                
                if index_count < 0:
                    index_count += 26
                result += lower_alpha[index_count]
            
            else:
                result += encrypted_msg[i]
            
            i += 1
        print(f" Key #{key}: {result}")
        
        result = ""
        key += 1
        
encrypted_code = input('enter encrypted message:\n > ')

hack(encrypted_code)