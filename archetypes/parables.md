---
id: "{{ .File.ContentBaseName }}"
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
type: parable
summary: ""
origin: ""
moral: ""
traditions: []
related: []
tags: []
languages:
  en: "{{ replace .File.ContentBaseName "-" " " | title }}"
sources:
  - title: ""
    tradition: ""
created: {{ .Date.Format "2006-01-02" }}
updated: {{ .Date.Format "2006-01-02" }}
version: 1
license: CC-BY-SA-4.0
---
