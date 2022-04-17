def e06_05():
    str = 'X-DSPAM-Confidence:0.8475'
    first_slice=str.find(":")
    fnumber=float(str[first_slice+1:])
    print(fnumber)
e06_05()
