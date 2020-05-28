import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dev", action="store_true", help="Dev mode")
    parser.add_argument("-t", "--test", action="store_true", help="Test mode")
    parser.add_argument("-l", "--lang", help="Your lang")

    return parser

def get():
    return args().parse_args()
