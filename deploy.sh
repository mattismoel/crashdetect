GOOS=linux GOARCH=arm GOARM=7 go build -v -o ./bin/crashdetect-web main.go

git add -A && git commit -m "push" && git push
