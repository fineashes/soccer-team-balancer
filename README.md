# Soccer Team Balancer

A web app that extracts player names from Viber poll screenshots using OCR and creates balanced soccer teams.

## Features

- 📸 OCR extraction from Viber poll screenshots (up to 6 images)
- ⚖️ Balanced team creation (2 or 4 teams)
- 🎯 Position-based balancing (Strikers, Midfielders, Defenders)
- 💪 Skill-based weight distribution
- 🔄 Redistribute teams randomly
- ➕ Add players manually
- 📱 Works on iPhone/Safari

## Deploy to GitHub Pages

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in (or create an account)
2. Click the **"+"** icon in the top right → **"New repository"**
3. Name it: `soccer-team-balancer` (or any name you prefer)
4. Set to **Public**
5. Click **"Create repository"**

### Step 2: Upload Your Files

**Option A: Using GitHub Web Interface (Easiest)**

1. On your new repository page, click **"uploading an existing file"**
2. Drag and drop `index.html` into the upload area
3. Click **"Commit changes"**

**Option B: Using Git Command Line**

```bash
cd /Users/ahada/CascadeProjects/soccer
git init
git add index.html
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/soccer-team-balancer.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. In your repository, click **"Settings"** (top menu)
2. Click **"Pages"** in the left sidebar
3. Under **"Source"**, select **"main"** branch
4. Click **"Save"**
5. Wait 1-2 minutes for deployment

### Step 4: Access Your App

Your app will be live at:
```
https://YOUR_USERNAME.github.io/soccer-team-balancer/
```

Share this URL with anyone - it works on all devices including iPhone!

## Usage

1. **Upload Screenshots**: Click to upload up to 6 Viber poll screenshots
2. **Extract Players**: Click "Extract Player Names" to process images
3. **Add Missing Players**: Fill in details for any unrecognized players or phone numbers
4. **Create Teams**: Select 2 or 4 teams and click "Create Balanced Teams"
5. **Redistribute**: Click "Redistribute" to shuffle players into new balanced teams
6. **Drag & Drop**: Move players between teams by dragging their cards

## Player Database

The app includes 50 pre-loaded players. To add more players:
1. Edit `index.html`
2. Find the `loadPlayersData()` function (around line 187)
3. Add new player objects to the array:
```javascript
{name: "Player Name", position: "S", secondaryPosition: "M", seed: 3}
```

**Positions**: S (Striker), M (Midfield), D (Defense)  
**Skill (seed)**: 1 (lowest) to 4 (highest)

## Technical Details

- **OCR**: Tesseract.js
- **Styling**: TailwindCSS
- **Icons**: Font Awesome
- **No Backend Required**: Fully client-side application

## License

Free to use and modify.
