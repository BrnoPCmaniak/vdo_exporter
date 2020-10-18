#!/usr/bin/env python3

from vdo_exporter import VDOStats

stats = VDOStats()
stats.collect()
print(stats.formatted())
