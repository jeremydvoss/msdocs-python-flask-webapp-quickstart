core_repo_name="opentelemetry-python"
contrib_repo_name="opentelemetry-python-contrib"

# declare -A core_packages
core_packages=(
    "opentelemetry-api"
    "opentelemetry-semantic-conventions"
    "opentelemetry-sdk"
    "opentelemetry-proto"
    # ["opentelemetry-test-utils"]="tests"
)
declare -A core_package_paths
core_package_paths=(
    ["opentelemetry-api"]=""
    ["opentelemetry-sdk"]=""
    ["opentelemetry-proto"]=""
    ["opentelemetry-semantic-conventions"]=""
    # ["opentelemetry-test-utils"]="tests"
)

# declare -A contrib_packages
contrib_packages=(
    "opentelemetry-instrumentation"
    # ["opentelemetry-distro"]=""

    "opentelemetry-instrumentation-django"
    "opentelemetry-instrumentation-fastapi"
    "opentelemetry-instrumentation-flask"
    "opentelemetry-instrumentation-requests"
    "opentelemetry-instrumentation-psycopg2"
    "opentelemetry-instrumentation-asgi"
    "opentelemetry-instrumentation-wsgi"
    "opentelemetry-instrumentation-dbapi"
    # ["opentelemetry-instrumentation-logging"]="instrumentation/"
    "opentelemetry-instrumentation-urllib"
    "opentelemetry-instrumentation-urllib3"
    "opentelemetry-resource-detector-azure"
)
declare -A contrib_packages_paths
contrib_packages_paths=(
    # ["opentelemetry-api"]=""
    # ["opentelemetry-sdk"]=""
    # ["opentelemetry-proto"]=""
    # ["opentelemetry-semantic-conventions"]=""
    # ["opentelemetry-test-utils"]="tests"

    ["opentelemetry-instrumentation"]=""
    # ["opentelemetry-distro"]=""

    ["opentelemetry-instrumentation-django"]="instrumentation/"
    ["opentelemetry-instrumentation-fastapi"]="instrumentation/"
    ["opentelemetry-instrumentation-flask"]="instrumentation/"
    ["opentelemetry-instrumentation-requests"]="instrumentation/"
    ["opentelemetry-instrumentation-psycopg2"]="instrumentation/"
    ["opentelemetry-instrumentation-asgi"]="instrumentation/"
    ["opentelemetry-instrumentation-wsgi"]="instrumentation/"
    ["opentelemetry-instrumentation-dbapi"]="instrumentation/"
    # ["opentelemetry-instrumentation-logging"]="instrumentation/"
    ["opentelemetry-instrumentation-urllib"]="instrumentation/"
    ["opentelemetry-instrumentation-urllib3"]="instrumentation/"

    ["opentelemetry-resource-detector-azure"]="resource/"
)

export CORE_REPO_SHA="0c382ee5356e1fa5a292e7a6c4961390cdfbe6df"
export CORE_REPO_URL="git+https://github.com/open-telemetry/opentelemetry-python.git@${CORE_REPO_SHA}"
echo "CONTRIB_REPO_SHA: $CORE_REPO_SHA";
echo "CONTRIB_REPO_URL: $CORE_REPO_URL";

export CONTRIB_REPO_SHA="e318c947a23152c8ff1700f0aad44261be0588cd"
export CONTRIB_REPO_URL="git+https://github.com/open-telemetry/opentelemetry-python-contrib.git@${CONTRIB_REPO_SHA}"
echo "CONTRIB_REPO_SHA: $CONTRIB_REPO_SHA";
echo "CONTRIB_REPO_URL: $CONTRIB_REPO_URL";

# for package in "${!core_packages[@]}";
for package in "${core_packages[@]}"
do
    # echo -e ""
    path=${core_package_paths[$package]}
    echo "package: $package";
    # Remote Version
    pip install -e "${CORE_REPO_URL}#egg=${package}&subdirectory=${path}${package}"
done

# for package in "${!contrib_packages[@]}";
for package in "${contrib_packages[@]}"
# for package in contrib_packages
do
    # echo -e ""
    path=${core_package_paths[$package]}
    echo "package: $package";
    # Remote Version
    # pip install -e "${CONTRIB_REPO_URL}#egg=${package}&subdirectory=${path}${package}"
done
# pip install -e "${CONTRIB_REPO_URL}#egg=opentelemetry-util-http&subdirectory=util/opentelemetry-util-http" \
# #             -e "{env:CONTRIB_REPO_URL}#egg=opentelemetry-instrumentation&subdirectory=opentelemetry-instrumentation" \
# #             -e "{env:CONTRIB_REPO_URL}#egg=opentelemetry-instrumentation-requests&subdirectory=instrumentation/opentelemetry-instrumentation-requests" \
# #             -e "{env:CONTRIB_REPO_URL}#egg=opentelemetry-instrumentation-wsgi&subdirectory=instrumentation/opentelemetry-instrumentation-wsgi"
# pip install -e "${CONTRIB_REPO_URL}#egg=opentelemetry-util-http&subdirectory=util/opentelemetry-util-http" \
#             -e "${CONTRIB_REPO_URL}#egg=opentelemetry-instrumentation&subdirectory=opentelemetry-instrumentation" \
#             -e "${CONTRIB_REPO_URL}#egg=opentelemetry-instrumentation-requests&subdirectory=instrumentation/opentelemetry-instrumentation-requests" \
#             -e "${CONTRIB_REPO_URL}#egg=opentelemetry-instrumentation-wsgi&subdirectory=instrumentation/opentelemetry-instrumentation-wsgi" \
#             -e "${CONTRIB_REPO_URL}#egg=${PACKAGE}&subdirectory=${PACKAGE_PATH}"

# servers=( 192.xxx.xxx.2 192.xxx.xxx.3
#           192.xxx.xxx.4 192.xxx.xxx.5
#           192.xxx.xxx.6 192.xxx.xxx.7
# )

# for server in "${servers[@]}" ; do
#     echo "$server"
# done