# -*- coding: utf-8 -*-

import requests
import humanize


class Pkg(object):

    def __str__(self):
        return self.name+' '+self.latest_version+' '+self.summary+' '


class Release(object):
    pass


def info(pkg_name):
    pkg_url = 'https://pypi.python.org/pypi/{}/json'.format(pkg_name)
    if exists(pkg_name):
        response = requests.get(pkg_url).json()
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
        for item in response['releases'].iterkeys():
            if response['releases'][item]:
                r = response['releases'][item][0]
                release = Release()
                release.url = r['url']
                release.downloads = r['downloads']
                release.upload_time = r['upload_time']
                release.size = humanize.naturalsize(r['size'])
                releases.append(release)
        pkg.releases = releases
    else:
        return None
    return pkg


def exists(pkg_name):
    pkg_url = 'https://pypi.python.org/pypi/{}/json'.format(pkg_name)
    try:
        r = requests.head(pkg_url)
        r.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        return False
