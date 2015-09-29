#!/usr/bin/env bash

if [ "$TRAVIS_PULL_REQUEST" == "false" ] ; then
    if [ "$TRAVIS_REPO_SLUG" != "pan0007/test" ] ; then
        echo "Permission denied to upload srpm package!"
        exit 0
    fi
    package_name=$(ls /tmp/tito/*.src.rpm) #name RPM package
    cd $HOME/build
    cd $TRAVIS_REPO_SLUG
    python rel-eng/travis/upload.py $COPR_LOGIN $COPR_TOKEN $package_name
    exit_code=$?
    cd .. 
    git clone https://62d1fa33fb82fbb732485614fef2561558850a02@github.com/pan0007/test status_rpg
    cd status_rpg
    POST /repos/:owner/:repo/statuses/:sha < rel-eng/travis/status
    exit $exit_code
fi
exit 0
