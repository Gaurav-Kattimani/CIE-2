import sys

if len(sys.argv) < 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("Usage : python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)
else:
    principal=10000
    rate=8
    time=2
    si = (principal * rate * time) / 100
    print("The Simple Interest is:", si)
