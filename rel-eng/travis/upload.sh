#!/usr/bin/env bash

if [ "$TRAVIS_PULL_REQUEST" == "false" ] ; then
    if [ "$TRAVIS_REPO_SLUG" != "pan0007/test" ] ; then
        echo "Permission denied to upload srpm package!"
        exit 0
    fi
    tito build --srpm --test
    package_name=$(ls /tmp/tito/*.src.rpm) #name RPM package
    cd $HOME/build
    cd $TRAVIS_REPO_SLUG
    python rel-eng/travis/display.py $COPR_LOGIN $COPR_TOKEN $package_name >copr.sh
    sh copr.sh
    exit $?
fi
exit 0
