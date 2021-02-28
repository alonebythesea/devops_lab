# snapshot module

Module that have some basic monitoring features:

- get_cpu() - Shows current CPU usage (in percentage)
- get_mem() - Shows used space in '/' directory(in percentage)
- get_vmem() - Shows current RAM usage(in percentage)
- get_disk_io() - Shows disk IO info
- get_net_io() - Shows network IO info
- get_time() - Shows current time(extra)
- write_to_file() - Write all above to file in '.' directory (json or txt supported only). File name is monitoring.json/txt

### Installation

To import this module just cd into directory and
`pip install -U .`


To make distro:
`python setup.py sdist`

### Usage

Script may take two arguments. The first one will indicate after how much time write_to_file() will executed.(in minutes)
Second one is file type(txt or json)

Example:
`snapshot 1 txt` after this command script will write to txt file every 1 min.
