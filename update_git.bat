@echo off
chcp 65001 >nul
cd /d "C:\Users\tm74\Projects\GazoHenkan"

echo Adding files to git...
git add README.md CLAUDE.md

echo Checking git status...
git status

echo Committing changes...
git commit -m "README.md and CLAUDE.md updates - Fix README encoding and add GitHub repository info - Record correct GitHub URL information in both files - Generated with Claude Code - Co-Authored-By: Claude <noreply@anthropic.com>"

echo Pushing to GitHub...
git push origin main

echo Done!
pause