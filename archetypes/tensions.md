---
id: "{{ .File.ContentBaseName }}"
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
type: tension
summary: ""
pole_a:
  value: ""
  argument: ""
pole_b:
  value: ""
  argument: ""
traditions: []
related: []
tags: []
languages:
  en: "{{ replace .File.ContentBaseName "-" " " | title }}"
sources:
  - title: ""
    author: ""
    year:
created: {{ .Date.Format "2006-01-02" }}
updated: {{ .Date.Format "2006-01-02" }}
version: 1
license: CC-BY-SA-4.0
---
