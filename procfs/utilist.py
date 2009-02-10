#! /usr/bin/python
# -*- python -*-
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

def hexbitmask(l, nr_entries):
	hexbitmask = []
	bit = 0
	mask = 0
	for entry in range(nr_entries):
		if entry in l:
			mask |= (1 << bit)
		bit += 1
		if bit == 32:
			bit = 0
			hexbitmask.insert(0, mask)
			mask = 0

	if bit < 32 and mask != 0:
		hexbitmask.insert(0, mask)

	return hexbitmask

def bitmasklist(line, nr_entries):
	fields = line.strip().split(",")
	bitmasklist = []
	entry = 0
	for i in range(len(fields) - 1, -1, -1):
		mask = int(fields[i], 16)
		while mask != 0:
			if mask & 1:
				bitmasklist.append(entry)
			mask >>= 1
			entry += 1
			if entry == nr_entries:
				break
		if entry == nr_entries:
			break
	return bitmasklist
