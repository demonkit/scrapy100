#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gurl


def urlWithScheme(url):
    if not gurl.Url(url).scheme:
        return "http://" + url
    return url


def urlToDomain(url):
    return gurl.Url(urlWithScheme(url)).hostname

