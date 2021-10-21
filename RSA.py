def main():
    # 1
    #RSA(p=3, q=17, e=5)
    #print()
    # 2
    #RSA(p=5, q=17, e=7)
    #print()
    # 3
    #RSA(p=7, q=17, e=29)
    RSA(11, 31, 7)

def RSA(p, q, e, m=None, encrypt=False, decrypt=False):
    
    n = p * q 
    print("n: " + str(n))

    oN = (p-1)*(q-1) 
    print("ø(n): " + str(oN))

    # Find d
    d = None 
    x = oN 
    step = 1
    while(step < oN): 
        print(f"Step {step} with x: {x}")
        if(x + 1) % e == 0:
            d = (x + 1) // e 
            break
        else:
            step += 1 
            x = oN * step 

    print("d: " + str(d))
    print("Total steps: " + str(step))
    
    return None 

if __name__ == "__main__":
    main() 