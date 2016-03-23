#!/usr/local/bin/python

# do $ pip install selenium
# if you don't already have selenium python drivers

from selenium import webdriver
import SimpleHTTPServer
import SocketServer
from threading import Thread
from time import sleep
import sys

def run_server(httpd):
  httpd.serve_forever()

if __name__=="__main__":
  PORT = 8080
  Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
  httpd = SocketServer.TCPServer(("", PORT), Handler)
  sys.stderr.write("serving at port %d\n" % (PORT))
  thread = Thread(target = run_server, args = (httpd, ))
  thread.start()
  sleep(1)
  sys.stderr.write("web server running in background\n")

  driver = webdriver.Chrome()
  try:
    driver.get("http://localhost:%d/index.html" % (PORT))
    #sleep(5) # wait for javascript XHR requests to finish... ouch!
    elem = driver.find_element_by_tag_name("svg")
    # import ipdb; ipdb.set_trace()
    html = elem.get_attribute('innerHTML')
    print html

    pass
  finally:
    driver.close()
    sys.stderr.write("requesting shutdown of web server ...\n")
    httpd.shutdown()
    thread.join()
    sys.stderr.write("requesting shutdown of web server ... OK\n")

