#!/usr/bin/bash

python3 download.py
ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i raw-video.m3u8 -acodec copy -vcodec copy output.mp4