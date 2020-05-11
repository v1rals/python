import re
from collections import Counter

class LogParser:
    def __init__(self, log_name):
        self.r_file = log_name

    def get_most_common(self, top):
        pattern = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - -')
        cnt = Counter()
        with open(self.r_file) as infile:
            for line in infile:
                m = pattern.match(line)
                if m is not None:
                    ip = m.groupdict()['ip']
                    cnt[ip] += 1
        return cnt.most_common(top)

    def log_by_http_code(self, output_file, code):
        pattern = re.compile(r'^[^"]*"[^"]*\sHTTP\/[\d.]+"\s+' + str(code))
        with open(self.r_file) as infile:
            with open(output_file, "w") as outfile:
                for line in infile:
                    m = pattern.match(line)
                    if m is not None:
                        outfile.write(line)
