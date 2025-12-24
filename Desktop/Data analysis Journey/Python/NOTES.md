# Learning Notes - Day 1

## Session Notes

### Initial Issue
- **Problem**: Syntax error - missing opening quote in print statement
- **Error**: `SyntaxError: unterminated string literal`
- **Fixed**: Added proper quotes around the string

### Code Review Feedback

#### What's Good ✅
1. Clear comments explaining your code
2. Good use of basic Python concepts (input, conditionals, arithmetic)
3. Exploring `end=''` parameter for print formatting
4. Well-organized structure

#### Suggestions for Improvement 💡
1. **Variable naming**: Use lowercase for variable names (Python convention)
   - Changed `Age` to `age` ✓

2. **Unused import**: `from pprint import pprint` was imported but never used
   - Can be removed if not needed

3. **Type conversion**: Consider converting input to int immediately:
   ```python
   age = int(input("How old are you: "))
   ```

4. **Error handling**: Add try/except for non-numeric age input:
   ```python
   try:
       age = int(input("How old are you: "))
   except ValueError:
       print("Please enter a valid number")
       age = 0
   ```

### Git Workflow - Setting Up Remote Repository

#### Steps Taken:

1. **Check for existing remote**
   ```bash
   git remote -v
   ```
   - Result: No remote configured

2. **Add remote repository**
   ```bash
   git remote add origin https://github.com/Rogue-weeb/30-days-of-python.git
   ```
   - Links local repo to GitHub

3. **First push attempt**
   ```bash
   git push -u origin main
   ```
   - Result: Rejected (remote had README.md not in local repo)

4. **Pull remote changes**
   ```bash
   git pull origin main --allow-unrelated-histories
   ```
   - Merged remote README.md with local code
   - `--allow-unrelated-histories` flag needed for diverged histories

5. **Successful push**
   ```bash
   git push -u origin main
   ```
   - Code now on GitHub! 🎉

### Future Git Commands

For future updates:
```bash
git add .                    # Stage all changes
git commit -m "message"      # Commit changes
git push                     # Push to GitHub (upstream already set)
```

### Repository
- **GitHub URL**: https://github.com/Rogue-weeb/30-days-of-python
- **Branch**: main
- **First commit**: "Day 1: Basic Python exercises - input, conditionals, and arithmetic operations"

---

*Notes created: January 2025*

