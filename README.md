# avgen

Calculate the average entropy of all n-dimensional probability distributions with respect to n

## Results

| dimension | value |
|-----------|-------|
|         1 | $ 0 $ |
|         2 | $ \frac{1}{2} $ |
|         3 | $ \frac{5}{6} $ |
|         4 | $ \frac{13}{12} $ |
|         5 | $ \frac{77}{60} $ |

## Conjecture

$$ E(d)=\sum_{i=1}^d{\frac1{i+1}} = H_d-1 $$

Where $ E(d) $ is the expected entropy of a $ d $-dimensional probability distribution with respect to $d$, $H_n$ is a [harmonic number](https://en.wikipedia.org/wiki/Harmonic_number), a partial sum of a harmonic sequence.

## Proof

None so far, however something tells me it could be done using mathematical induction.

# Script usage

```
usage: avgen.py [-h] -d DIM [-s SAMPLES] [-j JOBS]

options:
  -h, --help            show this help message and exit
  -d DIM, --dim DIM     The dimension of the probability distribution. >= 1
  -s SAMPLES, --samples SAMPLES
                        the number of the distributions sampled in a job
  -j JOBS, --jobs JOBS  the number of jobs to paralelize the sampling
```
