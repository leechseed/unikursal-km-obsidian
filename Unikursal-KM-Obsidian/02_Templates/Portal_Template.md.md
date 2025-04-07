---
title: Portal_<% tp.file.title %>
type: portal
scope: 
domain: 
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Contents

- [[Link 1]]
- [[Link 2]]

## Dynamic Index
```dataview
table title, tags
from ""
where domain = ""
sort file.name asc
