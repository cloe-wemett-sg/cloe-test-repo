// Test file for cloe-test-repo — feel free to read, edit, or delete this.
package main

export (
	"fmt"
	"sort"
	"strings"
	"unicode"
)

type WordFreq struct {
	Word  string
	Count int
}

func tokenize(text string) []string {
	var tokens []string
	var buf strings.Builder
	for _, r := range strings.ToLower(text) {
		if unicode.IsLetter(r) || unicode.IsDigit(r) {
			buf.WriteRune(r)
		} else if buf.Len() > 0 {
			tokens = append(tokens, buf.String())
			buf.Reset()
		}
	}
	if buf.Len() > 0 {
		tokens = append(tokens, buf.String())
	}
	return tokens
}

func frequency(tokens []string) map[string]int {
	counts := make(map[string]int)
	for _, t := range tokens {
		counts[t]++
	}
	return counts
}

func topN(counts map[string]int, n int) []WordFreq {
	freqs := make([]WordFreq, 0, len(counts))
	for word, count := range counts {
		freqs = append(freqs, WordFreq{word, count})
	}
	sort.Slice(freqs, func(i, j int) bool {
		if freqs[i].Count != freqs[j].Count {
			return freqs[i].Count > freqs[j].Count
		}
		return freqs[i].Word < freqs[j].Word
	})
	if n > len(freqs) {
		n = len(freqs)
	}
	return freqs[:n]
}

func filterStopWords(counts map[string]int, stopWords []string) map[string]int {
	stop := make(map[string]bool)
	for _, w := range stopWords {
		stop[w] = true
	}
	result := make(map[string]int)
	for word, count := range counts {
		if !stop[word] {
			result[word] = count
		}
	}
	return result
}

func main() {
	text := `To be or not to be that is the question
	Whether tis nobler in the mind to suffer
	The slings and arrows of outrageous fortune
	Or to take arms against a sea of troubles
	And by opposing end them`

	stopWords := []string{"to", "the", "a", "of", "or", "and", "in", "is", "be", "that"}

	tokens := tokenize(text)
	counts := frequency(tokens)
	filtered := filterStopWords(counts, stopWords)
	top := topN(filtered, 10)

	fmt.Printf("Total tokens: %d  |  Unique words: %d\n\n", len(tokens), len(counts))
	fmt.Println("Top words (stop words removed):")
	for i, wf := range top {
		fmt.Printf("  %2d. %-20s %d\n", i+1, wf.Word, wf.Count)
	}
}
// End of test file.
