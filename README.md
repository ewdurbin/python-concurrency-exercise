python-concurrency-exercise
===========================

Concurrency is hard, let's let gunicorn take care of it while we go shopping

## Prerequisites

  - Python 3.4
  - `virtualenv` or `venv`
  - `nginx`

## Setup

```
git@github.com:ewdurbin/python-concurrency-exercise.git
cd python-concurrency-exercise
virtualenv venv -p python3.4
source venv/bin/activate
pip install -r requirements.txt
honcho start
```

We now have 3 app servers and an `nginx` frontend running! Head on over to
http://localhost:8080/ to check it out.

## Instructions

Over the last few days, our Ops team has been noticing terrible behavior and
performance out of this application.

In a fit of rage, we took on the super difficult task of porting `app.py` to
Python 3.4 in hopes of alleviating some of the issues with the lamb that is
`asyncio`.

Your goal is to help us figure out why the following routes are causing trouble
as they are currently configured and hopefully fix them!:

  - `/check_feed`: Route which calls out to a slow external service to
    determine if there is anything interesting happening on the internet. In
    general, we've been seeing a steady stream of ~10 requests a second to this
    route. Unfortunately a lot of users are ending up with `502` backend errors
  - `/stream_feed`: Route which begins polling the same slow external service
    and streams updates to the client. This has been a real bear. After launch
    we regularly saw 50-100 *attempted* connections to this endpoint, but they
    nearly all fail. Our entire application also becomes quickly unavilable.

Do some research and determine the cause of our issues with these two routes.
Discuss your findings!

The Operations team has setup two additional application servers to test
mitigation strategies for these routes.

  - `gunicorn` running with `gthread` workers.
    Creates a pool of Python threads for handling requests
  - `gunicorn` running with `gaiohttp` workers.
    A fully evented worker class.

Read up a bit more in the Gunicorn documentation and source code:

  - https://github.com/benoitc/gunicorn
  - http://docs.gunicorn.org/en/latest/index.html

You should now edit `nginx.conf` to reconfigure the `upstream` that each route
connects to. Again, please discuss your choices!
