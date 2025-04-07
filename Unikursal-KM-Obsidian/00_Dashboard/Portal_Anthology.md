# 📚 Anthology Portal

Welcome to your dynamic, automatically updating research anthology.  
All entries must follow the `anth_` filename format and include a `title` field in YAML.

---

## 🧠 By Title

```dataview
table title, author, date_read, grade_level, knowledge_type, file.name as "File"
from "09_Anthology"
where startswith(file
```
