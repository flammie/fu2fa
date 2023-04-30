#!/usr/bin/env python3
'''fu2fa is a cli app for printing out TOTP 2fa secrets.

Flammie's ubiquitous 2-factor authentication was designed with a dmenu + pass
application in mind. Use at your own risk, since the primary use case is
circumventing an extra factor that is basically reducing the security level and
probably not a smart thing to do.
'''

from argparse import ArgumentParser

import sys

import pyotp


def main():
    '''Command-line interface to Flammie's ubiquituous 2fa tool.'''
    a = ArgumentParser()
    a.add_argument('-v', '--verbose', action='store_true',
                   help='print verbosely while processing')
    a.add_argument('-U', '--url', metavar='URL',
                   help='use URL as source for otp data')
    options = a.parse_args()
    if options.verbose:
        print('Printing verbosely')
    if options.url:
        if options.verbose:
            print('using url from options')
        otp = pyotp.parse_uri(options.url)
    else:
        if options.verbose:
            print('expecting url from stdin')
        otp = pyotp.parse_uri(sys.stdin.readline().strip())
    if isinstance(otp, pyotp.TOTP):
        print(otp.now())
    else:
        print('cannot do HOTP yet', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
