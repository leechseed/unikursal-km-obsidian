import os
import re
import yaml
from pathlib import Path

def refactor_yaml_block(content):
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return content, False  # No YAML block found

    yaml_block = match.group(1)
    metadata = yaml.safe_load(yaml_block)

    if not metadata or "dn_tags" not in metadata:
        return content, False  # Nothing to refactor

    # Extract and refactor dn_tags
    dn_tags = metadata.pop("dn_tags", [])
    function, dimension, technique = [], [], []

    for tag in dn_tags:
        if "::" in tag:
            category, value = tag.split("::", 1)
            category = category.strip().lower()
            value = value.strip()
            if category == "function":
                function.append(value)
            elif category == "dimension":
                dimension.append(value)
            elif category == "technique":
                technique.append(value)

    if function:
        metadata["function"] = sorted(set(function))
    if dimension:
        metadata["dimension"] = sorted(set(dimension))
    if technique:
        metadata["technique"] = sorted(set(technique))

    # Rebuild YAML
    new_yaml = yaml.dump(metadata, sort_keys=False).strip()
    new_content = f"---\n{new_yaml}\n---\n" + content[match.end():]
    return new_content, True

def process_directory(directory_path):
    md_files = Path(C:\Users\U01_LEECHSEED\Projekts\unikursal-km-obsidian\Unikursal-KM-Obsidian\09_Anthology).rglob("*.md")
    updated_count = 0

    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content, updated = refactor_yaml_block(content)

        if updated:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"[UPDATED] {file_path}")
            updated_count += 1

    print(f"\n✔️ Finished. {updated_count} file(s) updated.")

if __name__ == "__main__":
    folder = input("Enter path to your Obsidian folder (e.g., 09_Anthology): ").strip()
    process_directory(folder)
