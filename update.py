import os
import os.path as osp
import re
import urllib2

# generate Dockerfiles based on latest artifacts
# TODO: rewrite in rust?

rec_re = re.compile(r'<tr>.*?</tr>', re.DOTALL)
rec_ver_re = re.compile(r'href="/dist/rust-(nightly|beta|[\d.]+)-x86_64-unknown-linux-gnu.tar.gz"')
rec_mod_re = re.compile(r'modification">(\d{4}-\d{2}-\d{2} \d{2}:\d{2})<')

with open('versions.txt') as f:
    lines = f.readlines()
data = dict([line.strip().split(': ') for line in lines])

dist_html = urllib2.urlopen('http://static.rust-lang.org/dist/').read()
records = rec_re.findall(dist_html)
new_release = False
for rec in records:
    version = rec_ver_re.search(rec)
    modified = rec_mod_re.search(rec)

    if version and modified:
        version = version.group(1)
        modified = modified.group(1)
        if version not in data or data[version] < modified:
            data[version] = modified
            print 'NEW RELEASE: rust %s modified at %s' % (version, modified)
            new_release = True

if new_release:
    with open('versions.txt', 'w') as f:
        for k in sorted(data.keys(), reverse=True):
            print k
            f.write('%s: %s' % (k, data[k]))

    # generate Dockerfiles
    versions = sorted(data.keys(), reverse=True)[0:3]
    template = open('Dockerfile.template').read()
    for version in versions:
        if not osp.isdir(version):
            os.mkdir(version)
        with open('%s/Dockerfile' % version, 'w') as f:
            f.write(template.format(rust_version=version, modified=data[version]))
