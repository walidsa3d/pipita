#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pipita

for release in pipita.info('pipita').releases:
    print release.size