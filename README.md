Web Screenshots experiments
===========================

Sample Flask web app for taking web page screenshots using Selenium PhantomJS driver. Runs on Heroku.

Note: this is a very simple experiment. There are probably many better implementations out there.

See [scrn.herokuapp.com](http://scrn.herokuapp.com/) for example.

Heroku configs
--------------

This app uses [heroku-buildpack-multi](https://github.com/ddollar/heroku-buildpack-multi) buildpack.
Pass the buildpack as param during app creation or configure it later using `BUILDPACK_URL` var.

```
heroku apps:create app-name --buildpack https://github.com/ddollar/heroku-buildpack-multi.git
```

```
heroku config:set BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git
```

Inspect the `heroku config` and make sure that the following vars are set (and add them if missing):

```
LD_LIBRARY_PATH: /usr/local/lib:/usr/lib:/lib:/app/vendor/phantomjs/lib
PATH:            /usr/local/bin:/usr/bin:/bin:/app/vendor/phantomjs/bin
```
