HOST="192.168.54.195"
USER="pi"

GOOS=linux GOARCH=arm GOARM=7 go build -v -o ./bin/crashdetect-web main.go

scp ./bin/crashdetect-web $USER@$HOST:/home/pi/Documents/crash_detector/crashdetect-web
