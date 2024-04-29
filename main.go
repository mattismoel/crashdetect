package main

import (
	"embed"
	"fmt"
	"html/template"
	"net/http"
)

//go:embed template
var tmplFS embed.FS

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/", handleIndex())

	mux.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello world"))
	})

	mux.HandleFunc("/register", func(w http.ResponseWriter, r *http.Request) {
		username := r.PathValue("username")

		fmt.Println("registered", username)
	})

	http.ListenAndServe(":8080", mux)
}

func handleIndex() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		tmpl, err := template.ParseFS(tmplFS, "template/index.html")
		if err != nil {
			http.Error(w, "could not load template", http.StatusInternalServerError)
			return
		}

		err = tmpl.Execute(w, nil)
		if err != nil {
			http.Error(w, "could not execute template", http.StatusInternalServerError)
			return
		}
	}
}
