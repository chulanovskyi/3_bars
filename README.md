# 3_bars

Prerequisites:
Scripts need a list of bars in JSON format. Just copy the file 'Bars.json' to the directory with the script.
List of bars can be downloaded directly from http://data.mos.ru/opendata/export/1796/json/2/1

This script can help you to determine 3 things:

- Biggest bar
- Smallest bar
- Closest to you bar

How to use:

All functions take one argument (data) - a list of bars in JSON format and returns bar (name, address).

- get_biggest_bar(data) - bar with the biggest number of seats.
- get_smallest_bar(data) - bar with the smallest number of seats.
- get_closest_bar(data) -  bar which is closest to your location. Your location needs to be entered manually.