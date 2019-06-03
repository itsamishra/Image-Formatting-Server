package main

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"net/http"
)

func HandleHome(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("HandleHome"))
}

func HandleFormatImage(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("HandleFormatImage"))
}

func ConvertImageUrlToBase64(url string) string {
	var client http.Client
	response, err := client.Get(url)
	HandleError(err)
	bodyBytes, err := ioutil.ReadAll(response.Body)
	HandleError(err)
	// bodyString := string(bodyBytes)

	return base64.StdEncoding.EncodeToString(bodyBytes)
}

func main() {
	url := "https://cdn-images-1.medium.com/max/800/1*30aoNxlSnaYrLhBT0O1lzw.png"
	fmt.Println(ConvertImageUrlToBase64(url))
	// resp, _ := http.Get(url)
	// fmt.Println(resp.Body)
	// file, _ := os.Create("testfile")
	// io.Copy(file, resp.Body)

	// router := mux.NewRouter()
	// router.HandleFunc("/", HandleHome)
	// router.HandleFunc("/api/format-image", HandleFormatImage)

	// http.ListenAndServe(":8080", router)
}

func HandleError(err error) {
	if err != nil {
		panic(err)
	}
}
