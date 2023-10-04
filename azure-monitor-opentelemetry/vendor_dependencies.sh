#!/bin/bash
# Update repo
VERSION="0.40b0"
VERSION_MODULE="v0_40b0"
# cd ~/workplace/opentelemetry-python-contrib
# git fetch --all --tags
# git checkout tags/v$VERSION
# git reset --hard upstream/v$VERSION

mkdir ~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE
mkdir ~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE/opentelemetry
mkdir ~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE/opentelemetry/instrumentation

# instrumentation
# PACKAGE_DIR=~/workplace/opentelemetry-python-contrib/opentelemetry-instrumentation/src/opentelemetry/instrumentation
DEST_DIR=~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE/opentelemetry/
# cp -r $PACKAGE_DIR $DEST_DIR




# opentelemetry-instrumentation
pip install opentelemetry-instrumentation==$VERSION
#  PACKAGE_DIR=~/workplace/opentelemetry-python-contrib/instrumentation/opentelemetry-instrumentation-$PACKAGE/src/opentelemetry/instrumentation/$PACKAGE
PACKAGE_DIR=~/workplace/auto_instrumentation/Lib/site-packages/opentelemetry/instrumentation
DEST_DIR=~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE/opentelemetry
cp -r $PACKAGE_DIR $DEST_DIR


# Copy packages
declare -a INSTRUMENTATION_PACKAGES=(
    "asgi"
    "dbapi"
    "django"
    "fastapi"
    "flask"
    "psycopg2"
    "requests"
    "urllib"
    "urllib3"
    "wsgi"
)
for PACKAGE in ${INSTRUMENTATION_PACKAGES[@]}; do
 pip install opentelemetry-instrumentation-$PACKAGE==$VERSION
#  PACKAGE_DIR=~/workplace/opentelemetry-python-contrib/instrumentation/opentelemetry-instrumentation-$PACKAGE/src/opentelemetry/instrumentation/$PACKAGE
 PACKAGE_DIR=~/workplace/auto_instrumentation/Lib/site-packages/opentelemetry/instrumentation/$PACKAGE
 DEST_DIR=~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE/opentelemetry/instrumentation/
 cp -r $PACKAGE_DIR $DEST_DIR
done

# ppentelemetry-util-http
pip install opentelemetry-util-http
# PACKAGE_DIR=~/workplace/opentelemetry-python-contrib/util/opentelemetry-util-http/src/opentelemetry/util
PACKAGE_DIR=~/workplace/auto_instrumentation/Lib/site-packages/opentelemetry/util
DEST_DIR=~/workplace/azure-sdk-for-python/sdk/monitor/azure-monitor-opentelemetry/azure/monitor/opentelemetry/_vendor/$VERSION_MODULE/opentelemetry/
cp -r $PACKAGE_DIR $DEST_DIR


# Update imports for instrumentations
# find: from opentelemetry.instrumentation
# replace: from azure.monitor.opentelemetry._vendor.$VERSION_MODULE.opentelemetry.instrumentation
# files to include: azure-monitor-opentelemetry/azure/monitor/opentelemetry/

# Update imports for instrumentations
# find: import opentelemetry.instrumentation
# replace: import azure.monitor.opentelemetry._vendor.$VERSION_MODULE.opentelemetry.instrumentation
# files to include: azure-monitor-opentelemetry/azure/monitor/opentelemetry/

# Update imports for util-http
# find: from opentelemetry.util.http
# replace: from azure.monitor.opentelemetry._vendor.$VERSION_MODULE.opentelemetry.util.http
# files to include: azure-monitor-opentelemetry/azure/monitor/opentelemetry/

# Update imports for util-http
# find: import opentelemetry.util.http
# replace: import azure.monitor.opentelemetry._vendor.$VERSION_MODULE.opentelemetry.util.http
# files to include: azure-monitor-opentelemetry/azure/monitor/opentelemetry/

# Update version (this is an overreach)
# find: azure.monitor.opentelemetry._vendor.$OLD_VERSION_MODULE
# replace: azure.monitor.opentelemetry._vendor.$VERSION_MODULE
# files to include: azure-monitor-opentelemetry/

# Undo update version for old folder # huh?

# Update entry points

# Update package._instrument usage in dependency conflict flow

# remove docstrings

# make sure manual tracing sample was not changed

# Check all project toml for new dependencies