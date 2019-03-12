# IPhelper

A helper which can help get you IPs from file or convert CIDR,IP range to IPs.

 _____ ______  _            _
|_   _|| ___ \| |          | |
  | |  | |_/ /| |__    ___ | | _ __    ___  _ __
  | |  |  __/ | r'_ \  / _ \| || '_ \  / _ \| '__|
 _| |_ | |    | | | ||  __/| || |_) ||  __/| |
 \___/ \_|    |_| |_| \___||_|| .__/  \___||_|
                              | |
                              |_|

usage: python IPhelper.py <-F input_file> <-T input_text> <-O output_file_name>


Supported special formats:
1.(CIDR)          127.0.0.1/24
2.(IP range)      127.0.0.1-256
3.(','format IPs) 127.0.0.1,2,3,4……
