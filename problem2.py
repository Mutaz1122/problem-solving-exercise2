from typing import List
def oct_to_bin(octal: int) -> str:
    oct_bin={"0":"0","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
    octal1=str(octal)
    reslt=""
    for i in octal1:
        # print(oct_bin.get(i))
        reslt=reslt+oct_bin.get(i)
    for i in reslt:
        if reslt[0]=="0":
            reslt=reslt[1:]
    return reslt

print(oct_to_bin(123))