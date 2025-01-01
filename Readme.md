# Challenge 02: Time Formatter

## Overview
For this challenge, you need to write a function that:
- Takes a number of minutes as input
- Returns a string that converts it into hours and minutes
- Handles edge cases appropriately

### Examples:
```javascript
formatTime(90)    // returns "1h 30m"
formatTime(45)    // returns "45m"
formatTime(120)   // returns "2h"
formatTime(150)   // returns "2h 30m"
```

## Rules
Follow the same Git workflow practices we established in Challenge 1:

1. Fork this repo to your own Git
2. Create your working branch using this naming convention:
   - `feat/` - for the main work
   - `fix/` - for things you need to improve
   - `chore/` - for things you need to clean up

Example:
```bash
git checkout -b feat/CC-challenge-2-time-formatter
```

## Requirements
- Function should handle positive numbers
- Output format should be clean (no "0m" if minutes are 0)
- Write tests for your solution
- Think about edge cases:
  - What happens with 0 minutes?
  - What about negative numbers?
  - How do you handle decimal numbers?
  - What's the largest number you should support?

## Project Setup
```bash
npm init -y
npm install --save-dev jest
npm install --save-dev eslint prettier
```

Update your package.json with:
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
```

## Submission
- Complete your solution
- Merge everything into main
- Post your solution link in the challenge thread

Good luck! 🕒