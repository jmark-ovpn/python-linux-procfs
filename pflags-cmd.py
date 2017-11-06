#! /usr/bin/python
# -*- python -*-
# -*- coding: utf-8 -*-
#   print process flags
#   Copyright (C) 2015 Red Hat Inc.
#   Arnaldo Carvalho de Melo <acme@redhat.com>
#
#   This application is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; version 2.
#
#   This application is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.

from __future__ import print_function
import procfs, re, fnmatch, sys
from functools import reduce
from six.moves import map

ps = None

def thread_mapper(s):
	global ps

	try:
		return [ int(s), ]
	except:
		pass
	try:
		return ps.find_by_regex(re.compile(fnmatch.translate(s)))
	except:
		return ps.find_by_name(s)

def main(argv):

	global ps
	ps = procfs.pidstats()

	if (len(argv) > 1):
		pids = reduce(lambda i, j: i + j, list(map(thread_mapper, argv[1].split(","))))
	else:
		pids = list(ps.processes.keys())

	pids.sort()
	len_comms = [len(ps[pid]["stat"]["comm"]) for pid in pids]
	max_comm_len = max(len_comms)
	del(len_comms)

	for pid in pids:
		flags = ps[pid].stat.process_flags()
		# Remove flags that were superseeded
		if "PF_THREAD_BOUND" in flags and "PF_NO_SETAFFINITY" in flags:
			flags.remove("PF_THREAD_BOUND")
		if "PF_FLUSHER" in flags and "PF_NPROC_EXCEEDED" in flags:
			flags.remove("PF_FLUSHER")
		if "PF_SWAPOFF" in flags and "PF_MEMALLOC_NOIO" in flags:
			flags.remove("PF_SWAPOFF")
		if "PF_FREEZER_NOSIG" in flags and "PF_SUSPEND_TASK" in flags:
			flags.remove("PF_FREEZER_NOSIG")
		comm = ps[pid].stat["comm"]
		flags.sort()
		sflags = reduce(lambda i, j: "%s|%s" % (i, j), [a[3:] for a in flags])
		print("%6d %*s %s" %(pid, max_comm_len, comm, sflags))

if __name__ == '__main__':
	main(sys.argv)
