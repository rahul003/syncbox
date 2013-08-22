while inotifywait -e modify ./log.txt
do
	python req.py
	> ./log.txt
done
