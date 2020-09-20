"""
Read more: https://www.investopedia.com/ask/answers/042415/what-difference-between-standard-error-means-and-standard-deviation.asp#:~:text=The%20standard%20deviation%20(SD)%20measures,from%20the%20true%20population%20mean.
"""

import argparse
from math import sqrt
from statistics import mean
from statistics import mode
from statistics import median
from statistics import StatisticsError

def std_dev(l):
    """
        prints out the std dev of a list of numbers
    """
    avg = mean(l)
    print("mean: {}".format(avg))
    print('median: {}'.format(median(l)))
    try:
        print('mode: {}'.format(mode(l)))
    except StatisticsError as se:
        print(se)
    sd = sqrt(sum([pow(avg-x,2) for x in l])/len(l))
    print('Standard deviation: {}'.format(round(sd,2)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('--values', help='Enter list of values')
    args = parser.parse_args()
    std_dev([int(x.strip()) for x in args.values.split(',')])