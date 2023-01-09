#!/usr/bin/env python3
import os, subprocess, sys, tempfile
from datetime import date

home_dir = os.path.dirname(os.path.abspath(__file__))
bin_dir = os.path.join(home_dir, 'bin')
bin_path = os.path.join(bin_dir, 'scanline')
working_dir = tempfile.mkdtemp()

def scan_path(filename):
  return os.path.join(working_dir, '{}.pdf'.format(filename))

# Scan Command
scan_cmd_tmpl = '{} -dir {} -name {{}}'.format(bin_path, working_dir)

# Input
input("Press Enter to start scanning odd pages...")
print("Scanning odd pages...")
subprocess.run(scan_cmd_tmpl.format('odd'), shell=True)

input("Press Enter to start scanning even pages...")
print("Scanning even pages...")
subprocess.run(scan_cmd_tmpl.format('even'), shell=True)

# Merge
print("Merging files...")
name = sys.argv[1]
merge_cmd_tmpl = 'pdftk A={} B={} shuffle A Bend-1 output {}.pdf'.format(scan_path('odd'), scan_path('even'), name)
subprocess.run(merge_cmd_tmpl, shell=True)

print("Done! File saved as {}.pdf".format(name))