def kTuples(k, n):
    # accepted = [] CAN ALSO ADD THIS IF WE NEED TO STORE THEM AND RETURN INSTEAD OF PRINTING

    def myHelper(min, n, k, history):
        if len(history) == k:
            if False: #actually check 'if history not in accepted'
                # accepted.append(history) CAN ALSO ADD THIS IF WE NEED TO STORE THEM AND RETURN INSTEAD OF PRINTING
                print history
                return
        if min > n:
            return
        else:
            myHelper(min+1, n, k, history + [min])
            myHelper(min+1, n, k, history[:])

    myHelper(1,n,k,[])

kTuples(2, 4)
