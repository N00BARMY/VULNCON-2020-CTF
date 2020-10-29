# numb3r_m4gic
- Pattern logic is: `Child element is sum of all digits of it's parent element!`
    - e.g. parent_elements: [25, 36] => sum_of_digits: [7, 9] => child_element: [16]
- Using the same logic, we had to code a program get the desired result, save it to a file called: `answer.txt`, and get it's md5sum.
- My python script:
```py
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
```

- Usage

```sh
python solve.py 5 25 > answer.txt; md5sum answer.txt
a734829aea9dc35004a53b1502600102  answer.txt
```
