#!/usr/bin/env python
# (c) 2015 Michał Górny
# 2-clause BSD license

import sys

from gentoopm import get_package_manager

def find_packages(repo, flags):
	flags = frozenset(flags)
	pset = set()

	for p in repo:
		try:
			u = p.use
		except:
			pass
		else:
			for f in flags:
				if f in u:
					pset.add(p.key)
					break

	return pset


if __name__ == '__main__':
	if len(sys.argv) > 2:
		print('Usage: %s [<repo-name>]' % sys.argv[0])
		sys.exit(1)

	if len(sys.argv) == 2:
		repo_name = sys.argv[1]
	else:
		repo_name = 'gentoo'

	flags = '''
		3dnow
		3dnowext
		aes
		aes-ni
		avx
		avx2
		fma
		fma3
		fma4
		mmx
		mmxext
		padlock
		popcnt
		sse
		sse2
		sse3
		sse4
		sse4_1
		sse4_2
		sse4a
		ssse3
		xop
	'''.split()

	pm = get_package_manager()

	if repo_name == 'ALL':
		repos = pm.repositories
	else:
		repos = (pm.repositories[repo_name],)

	for r in repos:
		pset = find_packages(r, flags)
		if pset:
			print('== %s ==' % r.name)
			for p in sorted(pset):
				print(p)
