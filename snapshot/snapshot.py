#!/usr/bin/env python
import psutil as pu
import time
import argparse as ap
import json


class Monitoring:
    def get_time(self):
        cur_time = time.time()
        local_time = time.ctime(cur_time)
        return local_time

    def get_cpu(self):
        return '\nOverall CPU load: {0}\n'.format(pu.cpu_percent())

    def get_mem(self):
        return 'Overall memory usage: {0}\n'.format(pu.disk_usage('/').percent)

    def get_vmem(self):
        return 'Overall virtual memory usage: {0}\n'.format(pu.virtual_memory().percent)

    def get_disk_io(self):
        return 'IO information: read_bytes {0} / write_bytes ' \
            '{1}\n'.format(pu.disk_io_counters().read_bytes, pu.disk_io_counters().write_bytes)

    def get_net_io(self):
        return 'Network information: bytes sent {0} / bytes recieved ' \
            '{1}\n'.format(pu.net_io_counters().bytes_sent, pu.net_io_counters().bytes_recv)

    def get_header(self, count):
        return 'SNAPSHOT {0}: TIMESTAMP: {1}:'.format(count, self.get_time())

    def arguments_parser(self):
        parser = ap.ArgumentParser()
        parser.add_argument('timestamp', type=int, default=5, help='Enter timestamp(in minutes)',
                            nargs='?')
        parser.add_argument('output', type=str, default='txt',
                            help='Enter output type(json or txt)', nargs='?')
        return parser.parse_args()

    def write_to_file(self, count):
        arg = self.arguments_parser()
        if 'json' in arg.output:
            with open('monitoring.json', 'a') as outfile:
                json.dump(self.get_header(count), outfile)
                json.dump(self.get_cpu(), outfile)
                json.dump(self.get_mem(), outfile)
                json.dump(self.get_vmem(), outfile)
                json.dump(self.get_disk_io(), outfile)
                json.dump(self.get_net_io(), outfile)
            outfile.close()
        elif 'txt' in arg.output:
            with open('monitoring.txt', 'a') as outfile:
                outfile.write(self.get_header(count))
                outfile.write(self.get_cpu())
                outfile.write(self.get_mem())
                outfile.write(self.get_vmem())
                outfile.write(self.get_disk_io())
                outfile.write(self.get_net_io())
            outfile.close()

    def start_monitoring(self):
        count = 0
        arg = self.arguments_parser()
        while True:
            self.write_to_file(count)
            time.sleep(arg.timestamp * 60)
            count += 1


def main():
    t = Monitoring()
    t.start_monitoring()


if __name__ == "__main__":
    main()
