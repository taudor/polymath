"""
This file is a benchmark comparison between numpy and polymath.
It also serves as correctness proof for polymath
"""
import argparse
import sys
import time
import numpy as np
import polymath as pm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="Name of the function to benchmark.", choices=["mult", "mod_pad"])
    parser.add_argument("bits", help="Bit length of the polynomials.", type=int, choices=[8, 16, 24, 32, 48, 64])
    parser.add_argument("samples", help="Number of samples to compute.", type=int)
    parser.add_argument("iterations", help="Number of iterations", type=int)
    args = parser.parse_args()

    if args.samples <= 0:
        sys.exit("Error: Negative number of samples")
    if args.iterations <= 0:
        sys.exit("Error: Negative number of iterations")

    samples1 = np.random.RandomState().random_integers(0, 1, (args.samples, args.bits))
    samples2 = np.random.RandomState().random_integers(0, 1, (args.samples, args.bits))

    if args.bits == 64:
        f = np.array([1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 1])
    elif args.bits == 48:
        f = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1,
                   0, 0, 1])
    elif args.bits == 32:
        f = np.array([1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    elif args.bits == 24:
        f = np.array([1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    elif args.bits == 16:
        f = np.array([1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1])
    elif args.bits == 8:
        f = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1])

    # list with individual times
    time_np = []
    time_pm = []

    if args.function == "mult":
        print("Multiplying", args.samples, "samples with", args.samples,
              "samples using", args.bits, "bit polynomials:")

        for i in range(args.iterations):
            print("Iteration {:5d} / {}".format(i, args.iterations), end='\r')
            start_np = time.time()
            res_np = [np.polymul(p1, p2) % 2 for p1, p2 in zip(samples1, samples2)]
            time_np.append(time.time() - start_np)

            start_pm = time.time()
            res_pm = [pm.polymul(p1, p2) for p1, p2 in zip(samples1, samples2)]
            time_pm.append(time.time() - start_pm)

            for p1, p2 in zip(res_np, res_pm):
                np.testing.assert_array_equal(p1, p2)

    elif args.function == "mod_pad":
        print("Computing remainder for", args.samples, "samples using", args.bits,
              "*", args.bits ,"bit polynomials:")

        # computing bigger polynomials
        mult_samples = [pm.polymul(p1, p2) for p1, p2 in zip(samples1, samples2)]

        for i in range(args.iterations):
            print("Iteration {:5d} / {}".format(i, args.iterations), end='\r')
            start_np = time.time()
            res_np = [np.polydiv(p1, f)[1].astype(int) % 2 for p1 in mult_samples]
            time_np.append(time.time() - start_np)

            start_pm = time.time()
            res_pm = [pm.polymodpad(p1, f) for p1 in mult_samples]
            time_pm.append(time.time() - start_pm)

    print("               {:>8} / {:>8} / {:>8}".format("min", "max", "avrg"))
    print("numpy time   : {:8.4f} / {:8.4f} / {:8.4f} ms".format(
        min(time_np) * 1000,
        max(time_np) * 1000,
        sum(time_np) / len(time_np) * 1000
    ))
    print("polymath time: {:8.4f} / {:8.4f} / {:8.4f} ms".format(
        min(time_pm) * 1000,
        max(time_pm) * 1000,
        sum(time_pm) / len(time_pm) * 1000
    ))


if __name__ == '__main__':
    main()
