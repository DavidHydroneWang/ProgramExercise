#!/bin/bash
git status &&  git add . && git commit -m "`date +%Y-%m-%d`" && git pull && git push origin master
