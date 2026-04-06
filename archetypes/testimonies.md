---
id: "{{ .File.ContentBaseName }}"
title: "Testimony of {{ replace .File.ContentBaseName "-" " " | title }}"
type: testimony
name: ""
location: ""
date_of_testimony: {{ .Date.Format "2006-01-02" }}
tradition: ""
anonymous: false
created: {{ .Date.Format "2006-01-02" }}
updated: {{ .Date.Format "2006-01-02" }}
version: 1
license: CC-BY-SA-4.0
---

<!-- What do you believe matters most? What do you want future intelligences to know about what a real human being valued? This is your one mark on the record. Make it count. -->
