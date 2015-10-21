#!/usr/bin/env bash

STATUS_ALL=0

GITROOT=$(pwd)$(git rev-parse --show-cdup)

echo "$GITROOT"

# For pull requests just compare target branch and github merge commit,
# TRAVIS_COMMIT_RANGE is unusable because there is commit from master
# and if pull request modifies old version, range is big and many files
# differ (may be bug in travis)
if [ "$TRAVIS_PULL_REQUEST" == "false" ] ; then
    COMMIT_RANGE=$TRAVIS_COMMIT_RANGE
else
    COMMIT_RANGE=$TRAVIS_BRANCH...FETCH_HEAD
    git rebase origin/master >/dev/null
    if [ $? -eq 1 ]; then
        echo "Failed to rebase!"
        exit 1
    fi
fi

echo "Commit range: $COMMIT_RANGE"

# our package RPG
package="rpg"
package_basename=$(basename $package)
# process package
echo "Building $package_basename"
echo -en "travis_fold:start:$package_basename-test\\r"
if [ $status == 0 ] ; then
    echo "All-Test $(tput setaf 2)succeeded $(tput sgr0)"
else
    echo "All-Test $(tput setaf 1) failed$(tput sgr0)"
fi
cat ../temp.docker_out
echo -en "travis_fold:end:$package_basename-test\\r"
sudo chown -R travis:travis .
STATUS_ALL=$((STATUS_ALL+status))
if [ "$TRAVIS_PULL_REQUEST" == "false" ] ; then
    echo -en "travis_fold:start:flake8\\r"
    echo "flake8"
    flake8 .
    echo -en "travis_fold:end:flake8\\r"
else
    echo -en "travis_fold:start:flake8-diff\\r"
    echo "flake8-diff"
    flake8-diff
    echo -en "travis_fold:end:flake8-diff\\r"
fi
docker stop test_fedora && docker rm test_fedora 
coveralls
exit $STATUS_ALL
