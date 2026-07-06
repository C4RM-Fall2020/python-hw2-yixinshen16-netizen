import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    nums_obj = nums.astype(object)

    v = np.where(nums % 15 == 0, 'fizzbuzz',
        np.where(nums % 3 == 0, 'fizz',
        np.where(nums % 5 == 0, 'buzz', nums_obj))).tolist()
    return(v)
