package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/PuerkitoBio/goquery"
)

func ExampleScrape(user string) {
	// Request the HTML page.
	parse_url := fmt.Sprintf("https://www.last.fm/user/%s/neighbours", user)
	res, err := http.Get(parse_url)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != 200 {
		log.Fatalf("status code error: %d %s", res.StatusCode, res.Status)
	}

	// Load the HTML document
	doc, err := goquery.NewDocumentFromReader(res.Body)
	if err != nil {
		log.Fatal(err)
	}

	// Find the review items
	doc.Find(".user-list-name").Each(func(i int, s *goquery.Selection) {
		title := s.Find("a").Text()
		fmt.Println(i, title)
	})
}

func main() {
	ExampleScrape("RedJin")
}
