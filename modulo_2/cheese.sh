#! /usr/bin/env bash

default_time=5

nvgstcapture-1.0 --orientation 2 --image-res=3 --file-name _output -A -S "${1:-$default_time}" -C 1 --capture-auto
mv _output* data/camera_output.jpg
