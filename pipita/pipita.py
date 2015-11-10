# -*- coding: utf-8 -*-

import requests


class Pkg(object):
    pass


class Release(object):
    pass


def info(pkg_name):
    pkg_url = 'https://pypi.python.org/pypi/{}/json'.format(pkg_name)
    response = requests.get(pkg_url).json()
    data = response['info']
    pkg = Pkg()
    pkg.author = data['author']
    pkg.author_email = data['author_email']
    pkg.license = data['license']
    pkg.summary = data['summary']
    pkg.latest_version = data['version']
    return pkg
