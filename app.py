# Add to test manual instrumentation or backoff scenarios
# # from azure.monitor.opentelemetry import configure_azure_monitor
# configure_azure_monitor()

from flask import Flask, url_for
app = Flask(__name__)
import logging
import requests


# Set up logger
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return 'Flask Test app\nVisit /logs and /traces.'


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


@app.route('/logs')
def logs():
    logs_info()
    logs_warning()
    logs_error()
    logs_exception()
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
    for endpoint in ('traces_requests', 'traces_exception_requests', 'traces_dependencies'):
        try:
            requests.get(url_for(endpoint))
        except:
            pass
    return 'Test app traces'


if __name__ == '__main__':
    logger.info("App Running")
    logger.warning("App Running Warning")
    requests.get('https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python')
    app.run(port=8082)