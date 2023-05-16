from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)
import logging
import requests
from os.path import exists, isdir
from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor()

# Set up logger
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return 'Test app'


# Logs -> traces

@app.route('/logs/info')
def logs_info():
    message = 'Test app info log'
    logger.info(message)
    return message


@app.route('/logs/warning')
def logs_warning():
    message = 'Test app warning log'
    logger.warning(message)
    return message


@app.route('/logs/error')
def logs_error():
    message = 'Test app error log'
    logger.error(message)
    return message


@app.route('/logs/exception')
def logs_exception():
    message = 'Test app exception log'
    logger.exception(message)
    return message


# @app.route('/logs/correlated_info')
# def logs_correlated_info():
#     with tracer.start_as_current_span("hello"):
#         logger.info('Test app info log')


# @app.route('/logs/correlated_warning')
# def logs_correlated_warning():
#     with tracer.start_as_current_span("hello"):
#         logger.warning('Test app warning log')


# @app.route('/logs/correlated_error')
# def logs_correlated_error():
#     with tracer.start_as_current_span("hello"):
#         logger.error('Test app error log')


# @app.route('/logs/correlated_exception')
# def logs_correlated_exception():
#     with tracer.start_as_current_span("hello"):
#         logger.exception('Test app exception log')


@app.route('/logs')
def logs():
    logs_info()
    logs_warning()
    logs_error()
    logs_exception()
    # for endpoint in ('logs_info', 'logs_warning', 'logs_error', 'logs_exception'):
    #     requests.get(url_for(endpoint))
    return "Test app logs"


# Traces -> requests

@app.route('/traces/requests')
def traces_requests():
    return "Test app request"


@app.route('/traces/exception_requests')
def traces_exception_requests():
    return "Test app exception request", 500


@app.route('/traces/dependencies')
def traces_dependencies():
    requests.get('https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python')
    return "Test app dependency"

@app.route('/traces')
def traces():
    # traces_requests()
    # traces_exception_requests()
    # traces_dependencies()
    for endpoint in ('traces_requests', 'traces_exception_requests', 'traces_dependencies'):
        try:
            requests.get(url_for(endpoint))
        except:
            pass
    if exists('/agents/python'):
        return "EXISTS"
    return 'Test app traces'

# Metrics


# Django


# Psycopg2


# Auto + Manual


if __name__ == '__main__':
    logger.info("JEREMY: run info")
    if exists('/agents/python/'):
        print("/agents/python EXISTS")
    else:
        print("/agents/python does not EXIST")
    
    if exists('~/workplace/'):
        print("~/workplace EXISTS")
    else:
        print("~/workplace does not EXIST")
    app.run()