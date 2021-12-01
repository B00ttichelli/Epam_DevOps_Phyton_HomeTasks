#!/usr/local/bin/python3

import argparse
import logging
import random
import re
import string

parser = argparse.ArgumentParser(description='Strong Password Generator')

parser.add_argument("-l", "--length", help="Set length of password and generate random password", type=int)
parser.add_argument("-t", "--template", help=" Set template for generate passwords", type=str, )
parser.add_argument("-f", "--file", help="Getting list of patterns from file and generate for each random password")
parser.add_argument("-c ", "--count", help="Number of passwords", type=int)
parser.add_argument("-v", "--verbose", action='count', default=0)


def gen_by_token(token):
    split = list(token)
    symbol = split[0]
    try:
        quant = int(split[1])
    except Exception as err:
        quant = 1

    if symbol == 'a':
        return random.choices(string.ascii_lowercase, k=quant)
    elif symbol == 'A':
        return random.choices(string.ascii_uppercase, k=quant)
    elif symbol == 'd':
        return random.choices(string.digits, k=quant)
    elif symbol == 'p':
        return random.choices(string.punctuation, k=quant)
    else:
        return ''.ljust(quant, symbol)


def password_gen(template):
    if template.count()<5:
        logging.info("template is very short")
    tokens = str(template).split("%")
    password = ""
    for token in tokens:
        password = password + ''.join([str(elem) for elem in gen_by_token(token)])

    return password


args = parser.parse_args()
count = 1
log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
if args.verbose:
    level = log_levels[min(len(log_levels)-1, args.verbose)]
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")


logging.debug("Logging level debug")
logging.info("Logging Level Info")


if args.count:
    count = args.count
    logging.info("Password length is " + count)
    if count < 5:
        logging.debug("Password is too short")
if args.template:
    for x in range(count):
        print(password_gen(args.template))
if args.length:
    for x in range(count):
        print(re.sub(r'\s',
                     '',
                     ''.join([str(elem) for elem in random.choices(string.printable, k=args.length)]).replace(' ', '')))
if args.file:
    logging.info("Reading file with template")
    with open(args.file) as f:
        lines = f.readlines()

    for line in lines:
        logging.debug("Generating password for template " + line)
        print(password_gen(line))
