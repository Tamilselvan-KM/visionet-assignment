#!/bin/sh
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 5

