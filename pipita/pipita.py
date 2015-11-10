# -*- coding: utf-8 -*-

import requests
import humanize


class Pkg(object):
    pass


class Release(object):
    pass


def info(pkg_name):
    pkg_url = 'https://pypi.python.org/pypi/{}/json'.format(pkg_name)
    try:
        response = requests.get(pkg_url).json()
    except requests.exceptions.RequestException as e:
        print e
        return
    data = response['info']
    pkg = Pkg()
    pkg.name = data['name']
    pkg.author = data['author']
    pkg.author_email = data['author_email']
    pkg.license = data['license']
    pkg.summary = data['summary']
    pkg.latest_version = data['version']
    pkg.keywords = data['keywords']
    releases = []
    versions = response['releases'].keys()
    for item in versions:
        r = response['releases'][item][0]
        release = Release()
        release.url = r['url']
        release.downloads = r['downloads']
        release.upload_time = r['upload_time']
        release.size = humanize.naturalsize(r['size'])
        releases.append(release)
    pkg.releases = releases
    return pkg
