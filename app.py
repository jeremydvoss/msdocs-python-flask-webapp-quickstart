from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)
import logging
import requests
import os


# Set up logger
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    logger.info("JEREMY: index info")
    logger.warning("JEREMY: warning: index info")
    print('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    logger.info("JEREMY: favicon info")
    logger.warning("JEREMY: warning: favicon info")
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    print('hello')
    print(logger)
    logger.info("JEREMY: hello info")
    logger.warning("JEREMY: warning: hello info")

    name = request.form.get('name')

    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name = name)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        properties = {'custom_dimensions': {'problemId': 'No Name', 'key_2': 'value_2'}}
        # properties = {'problem_id': 'No Name problem',
            # 'problemId': 'No name problem 2'}
        print(logger)
        print("JEREMYVOSS: before error")
        logger.error(Exception("JEREMY: EXCEPTION: NO NAME pre"))
        logger.setLevel(logging.ERROR)
        print(logger)
        print("JEREMYVOSS: after error")
        logger.error(Exception("JEREMY: ERROR: NO NAME post"))
        logger.setLevel(logging.INFO)
        logger.exception("JEREMY: EXCEPTION: NO NAME")
        return redirect(url_for('index'))


# Logs

@app.route('/logs/info')
def logs_info():
    logger.info('Test app info log')


@app.route('/logs/warning')
def logs_warning():
    logger.warning('Test app warning log')


@app.route('/logs/error')
def logs_error():
    logger.error('Test app error log')


@app.route('/logs/exception')
def logs_exception():
    logger.exception('Test app exception log')


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


# Traces

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
    traces_requests()
    traces_exception_requests()
    traces_dependencies()

# Metrics


# Django


# Psycopg2


# Auto + Manual


if __name__ == '__main__':
    logger.info("JEREMY: run info")
    app.run()