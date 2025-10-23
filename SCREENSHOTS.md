# Screenshots Guide

To add screenshots to your README, follow these steps:

## 1. Take Screenshots

Run the app and capture:
- **Chat Interface**: Show a conversation with visualizations
- **Data Overview**: Show the tabs with statistics
- **Visualizations**: Show a chart being generated

## 2. Save Screenshots

Create a folder for images:
```bash
mkdir screenshots
```

Save your screenshots as:
- `screenshots/chat-interface.png`
- `screenshots/data-overview.png`
- `screenshots/visualizations.png`

## 3. Update README

Add this section after "## 🎨 Screenshots" in README.md:

```markdown
### Chat Interface
![Chat Interface](screenshots/chat-interface.png)
*Ask questions and get instant answers with visualizations*

### Data Overview
![Data Overview](screenshots/data-overview.png)
*Comprehensive statistics and data quality metrics*

### Visualizations
![Visualizations](screenshots/visualizations.png)
*Generate custom charts through dropdown menus or natural language*
```

## 4. Alternative: Use Online Images

If you push to GitHub, you can also use image URLs:
```markdown
![Chat](https://github.com/yourusername/repo/blob/main/screenshots/chat.png)
```

## Example Screenshots to Take

### 1. Chat Interface
- Upload titanic.csv
- Ask: "How many passengers survived?"
- Ask: "Show me a histogram of ages"
- Capture the full conversation with plots

### 2. Data Overview
- Click "Data Overview" button
- Navigate to Statistics tab
- Take screenshot showing all tabs

### 3. Visualizations
- Click "Visualizations" button
- Select "Correlation Heatmap"
- Capture the generated heatmap

## Tips for Good Screenshots

- Use full screen or maximize window
- Ensure good contrast and readability
- Crop unnecessary browser chrome
- Use PNG format for better quality
- Keep file sizes reasonable (< 1MB each)

## Tools for Screenshots

- **Windows**: Win + Shift + S (Snipping Tool)
- **Mac**: Cmd + Shift + 4
- **Linux**: gnome-screenshot or flameshot
