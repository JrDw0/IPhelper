# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'JrD'
__creatimm__ = '2019.3.11'

import sys
import re
import argparse
from netaddr import IPNetwork


def args_parse():
    usage = 'python IPhelper.py [options]'
    description = 'A helper which can help get you IPs from file or convert CIDR,IP range to IPs.'
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument(
        '-T',
        '--text',
        nargs='+',
        dest='text',
        help='Input from file',
        action='store')
    parser.add_argument(
        '-F',
        '--file',
        nargs='+',
        dest='file',
        help='Input from file',
        action='store')
    parser.add_argument(
        '-O',
        '--output',
        dest='output',
        help='OutPut IPs in file',
        action='store')
    args = parser.parse_args()
    return args


def find_all_ip(args):
    pattern1 = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}-\d{1,3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\,\d{1,3})+')
    allip = re.findall(pattern1, args)
    return allip


def main():
    ips = []
    result = []
    args = args_parse()
    if args.text:
        for text in args.text:
            ips += find_all_ip(text)
    elif args.file:
        for file in args.file:
            with open(file=file) as o:
                text = o.read()
                ips += find_all_ip(text)
    for ip in ips:
        if re.search('-', ip):
            _spilt = ip.split('-')
            s = _spilt[0].split('.')
            for n in range(int(s[3]), int(_spilt[1]) + 1):
                result.append('%s.%s.%s.%s' % (s[0], s[1], s[2], n))
        elif re.search('/', ip):
            for i in IPNetwork(ip):
                result.append(str(i))
        elif re.search(',', ip):
            _spilt = ip.split(',')
            result.append(_spilt[0])
            s = _spilt[0].split('.')
            if _spilt[1]:
                for n in _spilt[1:]:
                    result.append('%s.%s.%s.%s' % (s[0], s[1], s[2], n))
        else:
            result.append(ip)
    result = list(set(result))
    if args.output:
        with open(file=args.output + '.txt', mode='w') as out:
            for i in result:
                out.write(i + '\n')
    print(*result)
    print('The numbers of IPs: %s' % len(result))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('''
 _____ ______  _            _
|_   _|| ___ \| |          | |
  | |  | |_/ /| |__    ___ | | _ __    ___  _ __
  | |  |  __/ | r'_ \  / _ \| || '_ \  / _ \| '__|
 _| |_ | |    | | | ||  __/| || |_) ||  __/| |
 \___/ \_|    |_| |_| \___||_|| .__/  \___||_|
                              | |
                              |_|

usage: python IPhelper.py <-F input_file> <-T input_text> <-O output_file_name>
        ''')
    else:
        try:
            main()
        except KeyError:
            sys.exit()
            pass
