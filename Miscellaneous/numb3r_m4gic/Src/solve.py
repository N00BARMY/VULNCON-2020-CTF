#!/usr/bin/env python
import sys

def create_pattern(start, end):
    try:
        r=[i**2 for i in range(int(start), int(end)+1)]
        print(f"R1:{r}")
        for n in range(1, int(end)-int(start)+1):
            r=[sum(map(int, str(r[i]))) +  sum(map(int, str(r[i+1]))) for i in range(len(r)-1)]
            print(f"R{n+1}:{r}")
    except:
            print("Invalid input")
            sys.exit(1)
create_pattern(sys.argv[1], sys.argv[2])
