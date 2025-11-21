import sys

sys.argv = ["simple_interest.py", "10000", "5", "2"]

if len(sys.argv) != 4:
    print("Usage : python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

else:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    si=(principal * time * rate)/100
    print("Simple Interest : ",si)
