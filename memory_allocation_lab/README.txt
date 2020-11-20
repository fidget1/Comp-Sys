Macallister Armstrong

References:
    The book, class videos, exercises.

Environment information:
    PyCharm IDE running vanilla Python 3.8. Tested with Python 3.8 using the python3 command on my machine. I have still
    never heard back from the CS system administrators. You may be aware that I am unable to write to my home folder on
    the CS servers due to mal-configured permissions. I have documented this twice now, starting in September, in emails
    to the admins and Dr. Yang.

Usage:
    python3 ./memory_allocation_lab.py -H implicit -A first-fit -F input.txt
    python3 ./memory_allocation_lab.py -H explicit -A best-fit -F input.txt
    python3 ./memory_allocation_lab.py --heap-type implicit --algorithm first-fit --file input.txt
    python3 ./memory_allocation_lab.py -h
    python3 ./memory_allocation_lab.py --help

Notes:
    I have tested the implicit list quite a bit, and I'm confident that the validation for unacceptable inputs is more
or less full featured. I have tested all four commands for the implicit list, and it appears to be working as intended.
Given that we are not writing any payloads for pointers, I was unsure about whether to overwrite headers and footers
from past allocations. From what I learned in Systems Programming Concepts, I have no reason to believe that any of the
calls would actually overwrite memory, and so I have elected to leave all garbage data as is, after all, the header
always gives sufficient information to arrive at the next block, and so on. I have not sufficiently tested the explicit
list. Only about an hour before turning in the assignment did I pass my first significant test, and so I simply haven't
had time to look for patterns and edge cases, and code coverage.
