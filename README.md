# continuous_find
A simple program to continuously find counterexamples.

This repo expects to try all numbers for a conjecture like the 3n+1 problem and many more.

When it stops, it saves the current state in `start.txt`.
And when it resumes, it reads the same file as a new starting point.
This means, it can record all the previously calculated results without redoing it again.

Just run `find_next.py` when you have time. This is the leisure way of calculating.
Have fun.
