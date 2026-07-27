# AGENTS.md

## Repository Purpose

Personal LeetCode solutions repository with explanations for each problem.

## Structure

```
leetcode/
├── README.md              # Root index with links to all problems
├── {number}. {Problem Name}/
│   ├── solution.py        # Python solution
│   └── README.md          # Problem explanation
```

## Conventions

### Folder Naming
- Format: `{number}. {Problem Name}`
- Example: `3536. Maximum Product of Two Digits`

### solution.py
- Contains only the solution class and method
- No test cases, no imports unless required by the solution
- Uses `List[int]` type hint style (LeetCode convention)

### README.md (per problem)
- Sections: Problem, Approach, Complexity, Solution
- Approach explains the user's specific solution strategy
- Complexity includes time and space
- Solution code block matches solution.py exactly

### Root README.md
- Organized by categories (Math, Array, Graph, etc.)
- Each category has a table with columns: #, Problem (hyperlink), Difficulty
- Links use URL-encoded folder names (spaces as %20)

## User's Solution Style

- Prefers simple, readable approaches
- Uses built-in Python functions (max, sorted, remove)
- Single-pass tracking for finding top elements
