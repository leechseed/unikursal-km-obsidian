
---

### `Portal_Encyclopedia.md`

```markdown
# 📚 Portal: Encyclopedia

## Key Categories
- Concepts
- Disciplines
- Historical Figures

## Recent Entries
```dataview
table title, discipline
from "10_Encyclopedia"
where contains(tags, "encyclopedia")
sort file.ctime desc
