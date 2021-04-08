#!/usr/bin/env python
# coding: utf-8

import re

# function search for skill
def skill_search(regex, txt):
    pattern = re.compile(regex)
    matches = pattern.search(txt)

    if matches is not None:
        return 1
    else:
        return 0

# regexes
# search for R
reg_r = re.compile(r'(\,|\s)(R|Rstudio|rstudio)(\,|\s|\.)')

# search for Python
reg_python = re.compile(r'Python', re.IGNORECASE)

# search for SAS
reg_sas = re.compile(r'SAS', re.IGNORECASE)

# search for Excel 
reg_excel = re.compile(r'Excel', re.IGNORECASE)

# search for PowerPoint
reg_pp = re.compile(r'(PowerPoint|Power\sPoint)', re.IGNORECASE)

# search for SQL
reg_sql = re.compile(r'(SQL|PostgreSQL|MySQL)', re.IGNORECASE)

# search for Spark
reg_spark = re.compile(r'Spark', re.IGNORECASE)

# search for aws
reg_aws = re.compile(r'AWS', re.IGNORECASE)


