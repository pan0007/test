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
echo "ls ." >aa.sh
docker exec -i test_fedora bash -c "chown -R fedora:root /tmp /var/tmp /home/travis"
sudo chown -R travis:travis $HOME/build/$TRAVIS_REPO_SLUG
sh aa.sh
echo "ls ." >bb.sh
sh bb.sh
docker stop test_fedora && docker rm test_fedora
exit $STATUS_ALL