Here is the **updated `Metadata_Schema.md`** with the `guts99_stage` field added to all relevant sections — cleanly integrated and standardized.

---

````markdown
# Metadata Schema (YAML)

## Common Fields

```yaml
title:
tags: []
created:
modified:
status: draft | complete | reviewed
category: encyclopedia | pattern | summary | project
domain: DesignNarratology | Encyclopedia | Anthology | etc.
function: []
dimension: []
technique: []
guts99_stage: Model | Development | Production | Distribution | Reception
```
````

# 📑 Metadata Schema (YAML Frontmatter)

This file defines and standardizes every field used in YAML frontmatter across your vault. Apply consistently for clean dataviews, linking, and versioning.

---

## 🧱 Core Fields (Global to All Notes)

| Field          | Type   | Description                                                                                             |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| `title`        | string | Title of the note (usually matches file name)                                                           |
| `tags`         | list   | General tags, lowercase, plural where appropriate                                                       |
| `created`      | date   | Creation date in `YYYY-MM-DD` format                                                                    |
| `modified`     | date   | Last modified date (can be auto-updated with plugin)                                                    |
| `status`       | string | `draft`, `complete`, `reviewed`, `archived`                                                             |
| `category`     | string | `summary`, `pattern`, `entry`, `project`, etc.                                                          |
| `domain`       | string | Top-level namespace: `Anthology`, `Encyclopedia`, etc.                                                  |
| `UID`          | string | Unique identifier, format: `YYYYMMDD-###`                                                               |
| `guts99_stage` | string | Narrative product lifecycle phase: `Model`, `Development`, `Production`, `Distribution`, or `Reception` |

---

## 📚 Anthology-Specific Fields

| Field             | Type    | Description                                                         |
| ----------------- | ------- | ------------------------------------------------------------------- |
| `author`          | string  | Author of the book                                                  |
| `date_read`       | date    | When you completed reading the work                                 |
| `summary_status`  | string  | `draft`, `partial`, `complete`, `reviewed`                          |
| `genre`           | list    | Themes or disciplines (e.g., `Narratology`, `Structuralism`)        |
| `function`        | list    | Narrative roles (e.g., `Character`, `Conflict`)                     |
| `dimension`       | list    | Conceptual axes of analysis (e.g., `Time`, `Focalization`)          |
| `technique`       | list    | Formal devices or methods (e.g., `Flashback`, `Interior Monologue`) |
| `guts99_stage`    | string  | Where the work fits in the narrative lifecycle                      |
| `related_works`   | list    | Other `Work_*` notes referenced or connected                        |
| `notes_status`    | string  | `none`, `minimal`, `annotated`, `critical`                          |
| `personal_rating` | integer | 1–10 scale for subjective evaluation                                |
| `grade_level`     | integer | Teaching/reference depth: 1 = intro, 2 = intermediate, etc.         |
| `knowledge_type`  | string  | `explicit` = easily communicated; `tacit` = deep, layered, complex  |
| `Summary`         | string  | Short, high-level summary of key insight                            |
| `REASON`          | string  | Why this work is included, and how it fits your system              |

---

## 🧠 Design Narratology Fields

| Field       | Type   | Description                                                      |
| ----------- | ------ | ---------------------------------------------------------------- |
| `function`  | list   | Narrative roles like `Character`, `Narrator`, `Conflict`         |
| `dimension` | list   | Abstract properties like `Time`, `Space`, `Focalization`, `Bias` |
| `technique` | list   | Formal devices like `Flashback`, `Stream of Consciousness`       |
| `category`  | string | Always `theory`, `dimension`, `function`, or `lens`              |

---

## 🎭 Pattern Layer Fields

| Field           | Type   | Description                                                 |
| --------------- | ------ | ----------------------------------------------------------- |
| `pattern_type`  | string | `structural`, `symbolic`, `character`, `device`, etc.       |
| `function`      | list   | Optional: narrative function(s) represented                 |
| `dimension`     | list   | Optional: analytical dimensions this pattern interacts with |
| `technique`     | list   | Optional: techniques by which this pattern is expressed     |
| `related_works` | list   | Optional: fiction or theoretical sources referenced         |

---

## 📘 Encyclopedia Fields

| Field        | Type   | Description                                           |
| ------------ | ------ | ----------------------------------------------------- |
| `field`      | string | Broad subject field (e.g., `Philosophy`, `Semiotics`) |
| `discipline` | string | More specific academic or practical context           |

---

## ⚙️ Project Notes

| Field            | Type   | Description                                  |
| ---------------- | ------ | -------------------------------------------- |
| `project_status` | string | `active`, `on-hold`, `completed`, `archived` |
| `deadline`       | date   | Optional deadline                            |
| `milestones`     | list   | List of milestone goals                      |

---

## 🗂 Portal Notes

| Field   | Type   | Description                                                |
| ------- | ------ | ---------------------------------------------------------- |
| `type`  | string | Always set to `portal`                                     |
| `scope` | string | What this portal covers: `domain`, `category`, `tag`, etc. |

```

---
```
