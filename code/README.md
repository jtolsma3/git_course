# Time Stuff (Git Practice Repo)

This repository exists for one reason: **to practice Git**.

The code itself is intentionally lightweight and a little silly. It computes various time-related facts about the present moment and prints them out in a human-readable paragraph. Nothing here is meant to be production-ready, historically precise, or architecturally impressive.

## What This Project Does

When run, the script:

- Detects the system’s local timezone
- Calculates how many days remain until Christmas
- Computes how many days various people have been alive (via helper functions)
- Computes how many years have passed since several major historical events
- Prints all of the above as a single formatted text block

That’s it. No CLI flags. No configuration. Just vibes.

## Example Concepts Used

This project intentionally touches a few basic Python concepts so there’s something to refactor later:

- `datetime` and time arithmetic
- Simple helper functions in a `utils.py` module
- Basic math and rounding
- String formatting with f-strings
- Import organization

## Project Structure (Minimal)
```
 |── main.py # The main script that prints the paragraph
 |── utils.py # Helper functions (birthdates, event years, etc.)
 |── README.md
```

## Why This Repo Exists

This repository is used to practice:

- Git commits
- Branching and merging
- Rebasing
- Conflict resolution
- Refactoring commits
- Writing commit messages without fear

If something looks odd, inefficient, or unnecessary — that’s probably intentional.

## Disclaimer

- Historical dates are approximate.
- Time calculations are intentionally simple.
- This code exists to be edited, broken, fixed, and rewritten.

Feel free to clone, modify, or delete with zero emotional attachment.
