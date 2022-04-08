# Vipra Data Unity

## Feature: Show full work day for everyone for the speficific time range in days
This is defined as the sum of all the time entries + gaps between entries, which are smaller than 30 minutes (as 30 minutes or less is considered to be a resonable break in work and still counts as part of your workday)

When breaks higher than 30 minutes are found, they are added. Out of the entire sum 30 minutes are subtracted and the reminder is removed out of the persons entire workday.

###Commands:

```
poetry run python -m toggl_extractor workdays --range 1
or
poetry run python -m toggl_extractor workdays --r 1

workdays         : represents the feature
--r / --range    : is the option for past days for which you
                   want to see the report 
"1" / int        : the no. of days for the report (starting the day before), so if you give it a 1, it will give you the report for yesterday, if you give it a 2, it will return the report for yesterday and the day before, 3, yesterday, the day before yesterday and the day before the day berfore yesterday. It will return data for those date only if there are entries for those dates. Example Sundays usually don't have entries, but they count in the number of days, even if there is nothing to dispaly.


exemple output (cmd given on 2022-03-18):
'''python
poetry run python -m toggl_extractor workdays --r 1

2022-03-17:

Shoisob: 9.6 h
Andrei: 7.3 h
Fatema: 8.2 h
Davide Vitelaru: 7.6 h
Vivek: 6.8 h
Adrian: 6.1 h
Laurie: 4.4 h
Emmanuel: 6.5 h
Catalin Suceveanu: 3.9 h
Jitesh: 10.0 h
```

Option:
--slack     : the output is sent to slack
             poetry run python -m toggl_extractor workdays --range 1 --slack
             poetry run python -m toggl_extractor workdays --r 1 --slack


##Feature: Show the efficiency of the person
It compares the sum of all the entries with the workday total (see the first feature).
But, given that to properly be efficient you might need micro-breaks during the day,
in the formula small breaks of 10 minutes every 50 minutes were accounted for.

###Commands:
poetry run python -m toggl_extractor efficiency --r 3

efficiency      : represents the feature
--r / --range   : is the option for past days for which you
                 want to see the report 
"1" / int       : the no. of days for the report (starting the day before), so if you give it a 1, it will give you the report for yesterday, if you give it a 2, it will return the report for yesterday and the day before, 3, yesterday, the day before yesterday and the day before the day berfore yesterday. It will return data for those date only if there are entries for those dates. Example Sundays usually don't have entries, but they count in the number of days, even if there is nothing to dispaly.

Sample output(cmd given on April 8 2022):
'''python
poetry run python -m toggl_extractor efficiency --r 1 

2022-04-07:
Kevin: 100 %
Laurie: 100 %
Andrei: 98 %
Catalin Suceveanu: 85 %
Fatema: 101 %
Vivek: 110 %
Adrian: 100 %
Jitesh: 108 %
Emmanuel: 93 %
Davide Vitelaru: 108 %
James: 116 %
Shoisob: 103 %
'''

Options:
--slack     : the output is sent to slack
             poetry run python -m toggl_extractor workdays --range 1 --slack
             poetry run python -m toggl_extractor workdays --r 1 --slack