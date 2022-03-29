# Vipra Data Unity

## Feature: Show full work day for everyone for the speficific time range in days

```
poetry run python -m toggl_extractor workdays --range 1
or
poetry run python -m toggl_extractor workdays --r 1

workdays         : represents the feature
--r / --range    : is the option for past days for which you
                   want to see the report 
"1" / int        : the no. of days for the report (starting the day before), so if you give it a 1, it will give you the report for yesterday, if you give it a 2, it will return the report for yesterday and the day before, 3, yesterday, the day before yesterday and the day before the day berfore yesterday. It will return data for those date only if there are entries for those dates. Example Sundays usually don't have entries, but they count in the number of days, even if there is nothing to dispaly.



if the message should be posted on Slack, then:

poetry run python -m toggl_extractor workdays --range 1 --slack True
or
poetry run python -m toggl_extractor workdays --r 1 --slack True



exemple output (cmd given on 2022-03-18):  poetry run python -m toggl_extractor workdays --r 1

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
