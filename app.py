# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import time

from flask import Flask, Response, request

from selenium.webdriver import PhantomJS

app = Flask(__name__)


class StderrLog(object):
    def close(self):
        pass

    def __getattr__(self, name):
        return getattr(sys.stderr, name)


class Driver(PhantomJS):
    def __init__(self, *args, **kwargs):
        super(Driver, self).__init__(*args, **kwargs)
        self._log = StderrLog()


@app.route("/")
def index():
    url = request.args.get("url", "")
    width = int(request.args.get("w", 1000))
    min_height = int(request.args.get("h", 400))
    wait_time = float(request.args.get("t", 20)) / 1000  # ms

    if not url:
        return "Example: <a href='http://scrn.herokuapp.com/?url=http://en.ig.ma/&w=1200'>" \
               "http://scrn.herokuapp.com/?url=http://en.ig.ma/</a>"

    driver = Driver()
    driver.set_window_position(0, 0)
    driver.set_window_size(width, min_height)

    driver.set_page_load_timeout(20)
    driver.implicitly_wait(20)
    driver.get(url)

    driver.set_window_size(width, min_height)
    time.sleep(wait_time)

    sys.stderr.write(driver.execute_script("return document.readyState") + "\n")

    png = driver.get_screenshot_as_png()
    driver.quit()

    return Response(png, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
