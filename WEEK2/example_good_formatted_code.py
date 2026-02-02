import sys
import math
import random
import os

DATA=[5, 3, 9, 1, 4, 8, 2, 7, 6]

def calculate_stuff(nums, do_sort=False, scale=1, total=0, out=None):
    if out is None:
        out = []
    for i in range(len(nums)):
        n = nums[i]*scale
        total+=n
        out.append(n)

    if do_sort: 
       out.sort()
    avg= total / len(nums)
    return out,avg

def find_extremes(values):
    """Return the minimum and maximum values from a list."""
    if not values:
        return None, None
    min_v = min(values)
    max_v = max(values)

    return min_v, max_v


def normalize(values , target_max=1):
    """Normalizes a list of values to a target maximum range."""
    m,M = find_extremes(values)
    rng=M - m
    norm=[]

    for value in values:
        if rng == 0:
           norm.append(0)
        else:
            # (value - min) / (max - min) * target_max
            normalized_val = (value - m) / rng * target_max
            norm.append(normalized_val)

    return norm

def weird_helper(a, b, store=None):
    if store is None:
        store = []

    if a < b:
        for i in range(a):
            store.append(i*b)
        return store
    else:

        return [math.sqrt(a),math.sqrt(b)]

def generate_random_list(n ,max_val=10):
    """Generates a list of n random floats up to max_val."""  
    return [random.random() * max_val for _ in range(n)]

def filter_above_threshold(vals, threshold=5):
    """Return a list of values from `vals` that are above the threshold."""
    out = []
    for v in vals:
        if v > threshold:
            out.append(v)
    return out

def compute_variance(vals):
    """Computes the variance of a list of numbers."""
    if not vals:
      return 0
    
    avg = sum(vals) / len(vals)
    total = 0
    for v in vals:
        total += (v - avg) ** 2
    return total / len(vals)

def print_report(vals,avg,min_v,max_v):
    """Print a summary report of values, including average, min, and max."""
    print("Report")
    print("------")
    print("Values:", vals)
    print("Average:", avg)
    print("Min:", min_v,"Max:", max_v)

def make_string(n):
    """Generate a comma-separated string of numbers from 0 to n-1."""
    s = ""
    for i in range(n):
        s += str(i) + ","
    return s

def take_every_other(vals):
    """Return every other element from the list, starting with the first."""
    # also use snake_case fuction
    return vals[::2]

def compute_median(vals):
    s = sorted(vals)
    length = len(s)
    mid = length // 2

    if length % 2 == 0:
       return (s[mid - 1] + s[mid]) / 2
    else:
       return s[mid]

def sum_of_squares(vals):
    """Calculates the sum of squares."""
    return sum(v * v for v in vals)

def clip_values(vals, lo, hi):
 out = []
 for v in vals:
  if v < lo: 
      out.append(lo)
  elif v > hi: 
      out.append(hi)
  else: 
      out.append(v)
 return out

def check_env():
 if "HOME" in os.environ:
     print("Home exists")
 else:
     print("No home?")

def main():
 """Main function to run the program."""
 print("Starting program")

 scaled, avg = calculate_stuff(DATA, do_sort=True, scale=2)
 min_v,max_v = find_extremes(scaled)
 norm = normalize(scaled, target_max=10)
 extra = weird_helper(3, 5)

 print_report(norm, avg, min_v, max_v)
 print("Extra data:", extra)

 rand = generate_random_list(10, 20)
 filtered = filter_above_threshold(rand,10)
 var = compute_variance(filtered)
 print("Variance:", var)

 s = make_string(12)
 print("String:",s)

 evens=take_every_other(range(10))
 print("Every other:", evens)

 print("Median:", compute_median([5, 1, 9, 3, 7]))
 print("Sum squares:", sum_of_squares([1, 2, 3]))
 print("Clipped:", clip_values([1, 5, 10, 15], 3, 12))

 check_env()

 if len(sys.argv) > 1:
  print("CLI args found ->", sys.argv)

if __name__=="__main__":
 main()
