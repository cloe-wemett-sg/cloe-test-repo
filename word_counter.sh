#!/usr/bin/env bash

usage() {
  echo "Usage: $0 [OPTIONS] <file>"
  echo "Options:"
  echo "  -w    Count words"
  echo "  -l    Count lines"
  echo "  -c    Count characters"
  echo "  -u    Count unique words"
  echo "  -t    Show top 10 most frequent words"
  echo "  -a    Show all stats"
  exit 1
}

count_words()   { wc -w < "$1" | tr -d ' '; }
count_lines()   { wc -l < "$1" | tr -d ' '; }
count_chars()   { wc -c < "$1" | tr -d ' '; }
count_unique()  { tr '[:space:]' '\n' < "$1" | tr '[:upper:]' '[:lower:]' | grep -v '^$' | sort -u | wc -l | tr -d ' '; }

top_words() {
  echo "Top 10 words:"
  tr '[:space:]' '\n' < "$1" \
    | tr '[:upper:]' '[:lower:]' \
    | tr -d '.,!?;:"()' \
    | grep -v '^$' \
    | sort \
    | uniq -c \
    | sort -rn \
    | head -10 \
    | awk '{printf "  %3d  %s\n", $1, $2}'
}

[ $# -lt 1 ] && usage

SHOW_WORDS=false
SHOW_LINES=false
SHOW_CHARS=false
SHOW_UNIQUE=false
SHOW_TOP=false

while getopts "wlcuta" opt; do
  case $opt in
    w) SHOW_WORDS=true ;;
    l) SHOW_LINES=true ;;
    c) SHOW_CHARS=true ;;
    u) SHOW_UNIQUE=true ;;
    t) SHOW_TOP=true ;;
    a) SHOW_WORDS=true; SHOW_LINES=true; SHOW_CHARS=true; SHOW_UNIQUE=true; SHOW_TOP=true ;;
    *) usage ;;
  esac
done

shift $((OPTIND - 1))
FILE="$1"

[ -z "$FILE" ] && { echo "Error: no file specified"; usage; }
[ ! -f "$FILE" ] && { echo "Error: file '$FILE' not found"; exit 1; }

echo "File: $FILE"
$SHOW_LINES  && echo "Lines:        $(count_lines "$FILE")"
$SHOW_WORDS  && echo "Words:        $(count_words "$FILE")"
$SHOW_CHARS  && echo "Characters:   $(count_chars "$FILE")"
$SHOW_UNIQUE && echo "Unique words: $(count_unique "$FILE")"
$SHOW_TOP    && top_words "$FILE"
