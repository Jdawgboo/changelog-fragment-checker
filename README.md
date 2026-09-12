# Changelog Fragment Checker

Validate changelog-fragment filenames (`issue.category.md`) and short descriptions against allowed categories.

```bash
cat fragments.json | python tool.py
python -m unittest -v
```

The policy is intentionally small and repository-specific. It does not assemble a final changelog.
