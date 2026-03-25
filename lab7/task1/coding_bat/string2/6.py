def xyz_there(s):
    if s[:3] == "xyz":
        return True
    
    for i in range(1, len(s) - 2):
        if s[i : i+3] == "xyz" and s[i-1] != ".":
            return True
            
    return False