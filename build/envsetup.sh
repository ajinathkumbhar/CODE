#!/bin/bash

#####################################
# File   : envsetup.sh
# Author : ajinathkumbhar@gmail.com
# Usage  :
# source build/envsetup.sh
#
# This script provide some useful
# shell funtion/command for development
#
#####################################

#log tag
TAG=$(basename $0)

#root path
BUILD_ROOT=`pwd`

#Get current time
function getlogtime() {
  logtime=$(date +%T)
  echo $logtime
}

#Print information logs
function loginfo() {
  msg=$1
  echo "`getlogtime` I $msg"
}

#Print debug logs
function logerr() {
  msg=$1
  echo "`getlogtime` D $msg"
}

#Print error logs
function logdebug() {
  msg=$1
  echo "`getlogtime` E $msg"
}


#Get top dir location
function gettop() {
  if [ -z $BUILD_ROOT ]; then
    logerr "build root not set"
  fi
  echo $BUILD_ROOT
}

#Change dir to build root or to top dir
function croot() {
  local T=$(gettop)
  if [ -z $T ]; then
    logerr "Couldn't locate the top of tree, Try setting top"
    return
  fi

  if [ "$1" ]; then
    \cd $(gettop)/$1
  else
    \cd $(gettop)
  fi
}

