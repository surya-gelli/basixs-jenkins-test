#!/bin/bash

DIR_PATH=$1
if [ ! -d "$DIR_PATH" ]; then
    echo "Directory '$DIR_PATH' not exists"
    exit 1
fi

if [ -z "$GIT_COMMIT" ]; then
    echo "No current commit... fail"
    exit 1
fi

if [ -z "$GIT_PREVIOUS_COMMIT" ]; then
    echo "No previous commit, files are changed!"
    exit 0
fi

# Check is files in given directory changed between commits
# NOTE: $GIT_PREVIOUS_COMMIT and $GIT_COMMIT provided by Jenkins GIT Plugin
CHANGED=`git diff --name-only $GIT_PREVIOUS_COMMIT $GIT_COMMIT $DIR_PATH`

if [ -z "$CHANGED" ]; then
    echo "No changes dettected..."
else
    echo "Directory changed"
fi