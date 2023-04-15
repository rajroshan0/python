from math import ceil,floor
import csv
import statistics as st
smpl_mode = st.mode(sample_sorted)
smpl_mean = st.mean(sample_sorted)
smpl_median = st.median(sample_sorted)

print()
print("parameter of center te")
print("mode:",smpl_mode)
print("mean",smpl_mean)
print("medain:",smpl_median)

