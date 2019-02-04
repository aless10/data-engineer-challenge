# Data Engineer challenge

## Description
We receive 10 millions of events every day from our advertising platform. 
An example of event could be like this:
``
{
'clip': '1433',
'country': 'IT',
'event_id': '3cb10c45-4b92-496c-946d-b5dea993c8f9', 'publisher_id': '22',
'viewable_time': '15'
'timestamp': '552878700'
}
``

Where:
- clip is an id of 4 random numbers
- country is the country code
- event_id is an uuid of the event
- publisher_id is an id of 2 random numbers
- viewable_time is the time in seconds of the ad viewed (max 30) - timestamp is the unix timestamp of the event
 

We would like to have a schedulable job that takes as input:
- the number of events to generate 
- the datetime range

The job generates fake data and stores the events in a Redis database.
We would like to see a bunch of statistics saved and updated in Redis:
- total sum of viewable_time per publisher
- the top 10 publishers by events count
- the number of uniques clips per publisher
- total sum of clips per country viewed by day and by night (day = from 07:00 to 19:00, night = from 19:00 to 07:00)


## Installation and Requirements

Python 3.6:
```
pip install -r requirements.txt
```


### Install git client Hooks

1. Open with a terminal and execute
```bash
$ git config core.hooksPath git-hooks
```

The command above set git to use hooks saved in `git-hooks` instead of the default `.git/hooks/`.
This installation is required because [git doesn't track git client hooks.](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

