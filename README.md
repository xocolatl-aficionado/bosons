# Bosons
Watch time lapses of bosons interacting on a line

# Description of approach
The approach taken involves taking a look at every char in the given string to determine where the particle will be later and to make the necessary update according to what was at that location before. The update() helper method does the update based on existing conditions. 
The intermediary stages/strings will reflect 4 different states- "R","L", "B" and "." for particles at a location heading right, left, 2 going both ways and being non-existent. 
The colorX() helper finally colors all particles 'X' after the final array is established.
The strings will stop being processed as soon as all particles disappear from the window given or if none were present in the first place.

# How to run
1. cd into project folder.
2. Enter ```python labelinsight_2.py```

# What to Expect
The output will be the result of unittests. Hence an 'OK' means all is good.
