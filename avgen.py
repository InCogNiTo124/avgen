import numpy as np
from numpy.random import default_rng
import concurrent.futures as cf
from functools import reduce
from tqdm import tqdm
from argparse import ArgumentParser

class GaussianReducer():
    def __init__(self):
        self.n = 1
        return

    def __call__(self, x, y):
        # adapted from https://stats.stackexchange.com/a/179215
        self.n += 1
        alpha_y = 1/self.n
        alpha_x = 1-alpha_y
        x_mean, x_var = x
        y_mean, y_var = y
        mean = (alpha_x*x_mean) + alpha_y*y_mean
        var = (alpha_x**2 * x_var) + alpha_y**2 * y_var
        return (mean, var)

SIZE = 1_000_000
DIM = 5
TOTAL = 1000

def avgen(dim, samples):
    rng = default_rng()
    X = rng.dirichlet(np.ones(dim), (samples,))
    assert X.shape == (samples, dim)
    E = -np.sum(X * np.log(X),axis=1)
    return E.mean(), E.var(ddof=1)/samples


def main(dim, samples, jobs):
    with cf.ProcessPoolExecutor() as executor:
        job_list = [executor.submit(avgen, dim, samples) for _ in range(jobs)]
        mean, var = reduce(GaussianReducer(), map(lambda f: f.result(), tqdm(cf.as_completed(job_list), total=TOTAL)))
        std = np.sqrt(var)
        print(mean-2.96*std, mean, mean + 2.96*std)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-d', '--dim', type=int, required=True, help="The dimension of the probability distribution. >= 1")
    parser.add_argument('-s', '--samples', type=int, default=1_000_000, help="the number of the distributions sampled in a job")
    parser.add_argument('-j', '--jobs', type=int, default=1000, help="the number of jobs to paralelize the sampling")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))
