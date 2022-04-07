#!/bin/bash
git status &&  git add . && git commit -m "`date +%Y-%m-%d`" && proxychains git pull && proxychains git push origin master
