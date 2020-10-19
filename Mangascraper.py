import re
import sys
from extra_functions import fuckit

print(f"Getting {sys.argv[1]}'s Chapter {sys.argv[2]} to Chapter {int(sys.argv[2]) + int(sys.argv[3])}")

for _ in range(int(sys.argv[2]),int(sys.argv[2])+int(sys.argv[3])+1):
    print(f"\n Fetching Chapter {_}")
    fuckit(sys.argv[1],_)
    print("\n###### Downloading Next Chapter ########\n")