#!/bin/bash
inotifywait -e modify -e moved_to -e moved_from -e move_self -e create -e delete -e delete_self -mr ./main/blob/blob/media/pictures > ./log.txt
