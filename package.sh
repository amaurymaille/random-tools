#!/bin/sh

HERE=$(pwd)

PY_FILES=$(ls *.py)
ALL_FILES=$PY_FILES
VERSION=$2
NAME=$1
PACKAGE=${NAME}_${VERSION}

cd /tmp
mkdir $PACKAGE
cd $PACKAGE
mkdir usr
mkdir usr/local
mkdir usr/local/bin
mkdir DEBIAN

cd $HERE
cp "$ALL_FILES" /tmp/$PACKAGE/usr/local/bin
cd /tmp/$PACKAGE
cat << EOF > DEBIAN/control
Package: random-tools
Version: $VERSION
Section: base
Priority: optional
Architecture: i386
Depends: python3
Maintainer: Amaury Maillé (amaury.maille@gmail.com)
Description: random-tools
  A collection of script doing miscellaneous things that may end up useful for
  the everyday life of programmers. Sadly, it doesn't prepare coffee. Yet.

EOF

cd ..
dpkg-deb --build $PACKAGE 
