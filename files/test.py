import pyotp
import pandas as pd
from pathlib import Path
from datetime import datetime
import csv, re, os, argparse, configparser
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true')
    parser.add_argument('--bar', action='store_true')
    args = parser.parse_args()

    if args.foo:
        print("foo")
    if args.bar:
        print("bar")

    