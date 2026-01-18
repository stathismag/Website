# Google Scholar Citation Tracker

This repository includes an automated system to track and display Google Scholar citations, h-index, and i10-index metrics.

## Features

- 📊 **Automated Updates**: Daily automatic updates via GitHub Actions
- 🎨 **Professional Widget**: Beautiful, responsive metrics display
- 📱 **Mobile-Friendly**: Responsive design that works on all devices
- 🔄 **Real-time Updates**: JavaScript-based auto-refresh from JSON data
- 🌐 **Multi-language Support**: English and Greek versions

## Components

### 1. Python Crawler (`gs_crawler.py`)

The crawler uses SerpAPI to fetch Google Scholar metrics and updates all HTML files.

**Features:**
- Fetches citations, h-index, and i10-index from Google Scholar
- Updates multiple HTML files simultaneously
- Saves data to JSON for programmatic access
- Includes timestamp tracking

**Files Updated:**
- `content/english/google_scholar_metrics.html` - Styled English version
- `content/greek/google_scholar_metrics.html` - Styled Greek version
- `layouts/partials/google_scholar_metrics.html` - Simple partial version
- `data/google_scholar_citations.json` - JSON data file

### 2. GitHub Actions Workflow (`.github/workflows/gs_crawler.yml`)

**Automation Features:**
- Runs daily at 6:00 AM UTC
- Can be triggered manually from GitHub Actions UI
- Only commits when metrics change
- Includes citation count in commit message

**Schedule:**
```yaml
schedule:
  - cron: "0 6 * * *"  # Daily at 6:00 AM UTC
```

### 3. Professional Widget (`layouts/partials/widgets/scholar_metrics.html`)

**Features:**
- Modern gradient design
- Hover animations
- Auto-refresh from JSON data
- Font Awesome icons support
- Responsive grid layout
- Dark mode support

## Setup Instructions

### Prerequisites

1. **SerpAPI Account**:
   - Sign up at [SerpAPI](https://serpapi.com/)
   - Get your API key
   - Update the API key in `gs_crawler.py` (line 9)

2. **Google Scholar Author ID**:
   - Find your profile URL: `https://scholar.google.com/citations?user=YOUR_ID`
   - Update the author ID in `gs_crawler.py` (line 8)

### Installation

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test Locally:**
   ```bash
   python gs_crawler.py
   ```

3. **Verify Updates:**
   Check that the following files were updated:
   - `content/english/google_scholar_metrics.html`
   - `content/greek/google_scholar_metrics.html`
   - `layouts/partials/google_scholar_metrics.html`
   - `data/google_scholar_citations.json`

## Usage

### Display Metrics on Your Website

#### Option 1: Use the Widget (Recommended)

Add to your Hugo page or widget area:
```html
{{ partial "widgets/scholar_metrics.html" . }}
```

#### Option 2: Use the Simple Partial

Add to any template:
```html
{{ partial "google_scholar_metrics.html" . }}
```

#### Option 3: Include Directly

For standalone pages:
```html
{{ readFile "content/english/google_scholar_metrics.html" | safeHTML }}
```

### Manual Updates

To manually trigger an update:

1. **Via GitHub Actions:**
   - Go to your repository on GitHub
   - Click "Actions" tab
   - Select "Update Google Scholar Citations"
   - Click "Run workflow"

2. **Locally:**
   ```bash
   python gs_crawler.py
   git add .
   git commit -m "Update Google Scholar metrics"
   git push
   ```

## Data Structure

### JSON Output (`data/google_scholar_citations.json`)

```json
{
  "total_citations": 313,
  "h_index": 10,
  "i10_index": 10,
  "last_updated": "2026-01-18 23:30:00"
}
```

### Accessing Data Programmatically

```javascript
fetch('/data/google_scholar_citations.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Citations: ${data.total_citations}`);
    console.log(`H-Index: ${data.h_index}`);
    console.log(`i10-Index: ${data.i10_index}`);
  });
```

## Customization

### Update Frequency

Edit `.github/workflows/gs_crawler.yml`:

```yaml
schedule:
  - cron: "0 6 * * *"  # Change to your preferred schedule
```

Common schedules:
- Every 6 hours: `"0 */6 * * *"`
- Every week: `"0 6 * * 0"` (Sunday 6 AM)
- Every month: `"0 6 1 * *"` (1st of month, 6 AM)

### Widget Styling

Edit `layouts/partials/widgets/scholar_metrics.html` to customize:
- Colors: Modify the gradient in `.scholar-metrics-container`
- Layout: Adjust `.metrics-grid` properties
- Animation: Customize the `@keyframes countUp` animation

### Widget Colors

Current gradient:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Alternative gradients:
```css
/* Blue to cyan */
background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);

/* Orange to red */
background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);

/* Green to blue */
background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
```

## Troubleshooting

### Workflow Not Running

1. Ensure GitHub Actions is enabled in your repository
2. Check that the workflow file is in `.github/workflows/`
3. Verify the cron schedule is correct

### API Errors

1. **Rate Limiting**: SerpAPI has usage limits. Check your plan.
2. **Invalid API Key**: Verify your API key in `gs_crawler.py`
3. **Invalid Author ID**: Confirm your Google Scholar author ID

### Files Not Updating

1. Check the GitHub Actions logs for errors
2. Ensure the Python script has write permissions
3. Verify the file paths in `gs_crawler.py` are correct

### Widget Not Displaying

1. Ensure the partial is correctly included in your template
2. Check that the CSS is being loaded
3. Verify Font Awesome is loaded for icons

## Security Notes

⚠️ **Important**: The current implementation includes the SerpAPI key in the code. For better security:

1. **Use GitHub Secrets:**
   - Store API key in GitHub repository secrets
   - Access via `${{ secrets.SERPAPI_KEY }}`

2. **Use Environment Variables:**
   ```python
   import os
   api_key = os.environ.get('SERPAPI_KEY')
   ```

3. **Update Workflow:**
   ```yaml
   - name: Run Google Scholar crawler
     env:
       SERPAPI_KEY: ${{ secrets.SERPAPI_KEY }}
     run: python gs_crawler.py
   ```

## Future Enhancements

- [ ] Add citation growth charts
- [ ] Track citation history over time
- [ ] Email notifications on milestone achievements
- [ ] Compare with other researchers
- [ ] Export data to CSV/Excel
- [ ] Add more visualization options

## Contributing

Feel free to submit issues or pull requests to improve this tracker!

## License

See the main repository LICENSE file.

---

**Last Updated**: January 2026
**Maintained By**: Automated GitHub Actions
