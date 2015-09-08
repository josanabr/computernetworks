#!/usr/bin/python
#
# This program asks a NTP server for the current hour and prints it
#
import ntplib
from time import ctime

ntp_client = ntplib.NTPClient()
response = ntp_client.request("pool.ntp.org")
print ctime(response.tx_time)
