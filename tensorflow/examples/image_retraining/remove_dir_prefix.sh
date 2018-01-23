#!/bin/bash
for dirname in */; do
	mv $dirname ${dirname#*-}
done