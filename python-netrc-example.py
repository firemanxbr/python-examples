#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netrc


"""
Set a path for your netrc file or ~/.netrc to default path
"""
get = netrc.netrc("netrc-file")

"""
Get login, account and password of netrc file
"""
print (get.authenticators('my-host'))

