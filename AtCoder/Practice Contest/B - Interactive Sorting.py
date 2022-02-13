from string import ascii_uppercase 
 
 
def compare(a, b): 
    print("? " + a, b) 
    return input() 
 
 
def sort5(let): 
    a, b, c, d, e = let 
    if compare(a, b) == ">": 
        a, b = b, a 
    if compare(c, d) == ">": 
        c, d = d, c 
    if compare(a, c) == ">": 
        a, b, c, d = c, d, a, b 
    if compare(c, e) == "<": 
        if compare(d, e) == ">": 
            d, e = e, d 
        if compare(b, d) == "<": 
            if compare(b, c) == "<": 
                let = [a, b, c, d, e] 
            else: 
                let = [a, c, b, d, e] 
        else: 
            if compare(b, e) == "<": 
                let = [a, c, d, b, e] 
            else: 
                let = [a, c, d, e, b] 
    else: 
        if compare(a, e) == "<": 
            if compare(b, c) == "<": 
                if compare(b, e) == "<": 
                    let = [a, b, e, c, d] 
                else: 
                    let = [a, e, b, c, d] 
            else: 
                if compare(b, d) == "<": 
                    let = [a, e, c, b, d] 
                else: 
                    let = [a, e, c, d, b] 
        else: 
            if compare(b, c) == "<": 
                let = [e, a, b, c, d] 
            else: 
                if compare(b, d) == "<": 
                    let = [e, a, c, b, d] 
                else: 
                    let = [e, a, c, d, b] 
    return let 
 
def merge_sort(let): 
    if len(let) <= 1: 
        return let 
 
    mid = len(let) // 2 
    left = let[:mid] 
    right = let[mid:] 
 
    left = merge_sort(left) 
    right = merge_sort(right) 
 
    return merge(left, right) 
def merge(left, right): 
    merged = [ ]
    left_i, right_i = 0, 0 
 
    while left_i < len(left) and right_i < len(right): 
 
        print("? "+left[left_i], right[right_i]) 
        if input() == "<": 
            merged.append(left[left_i]) 
            left_i += 1 
        else: 
            merged.append(right[right_i]) 
            right_i += 1 
 
    if left_i < len(left): 
        merged.extend(left[left_i:]) 
    if right_i < len(right): 
        merged.extend(right[right_i:]) 
    return merged 
p, q = map(int, input().split()) 
answer = list(ascii_uppercase[:p]) 
answer = merge_sort(answer) if p != 5 else sort5(answer) 
 
print("! "+"".join(answer), flush=True)