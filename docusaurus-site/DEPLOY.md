# Deploy to GitHub Pages - moizalpha

## ✅ Configuration Already Set

Your `docusaurus.config.js` is configured for:
- **GitHub Username**: moizalpha
- **Repository**: physical-ai-capstone
- **Site URL**: https://moizalpha.github.io/physical-ai-capstone/

## 🚀 Deployment Steps

### Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. **Repository name**: `physical-ai-capstone`
3. **Visibility**: Public (required for free GitHub Pages)
4. **DON'T** initialize with README, .gitignore, or license
5. Click **Create repository**

### Step 2: Deploy Commands

Open your terminal and run these commands **one by one**:

```bash
# Navigate to docusaurus-site directory
cd "D:\physical ai book\physical-ai\docusaurus-site"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Physical AI Capstone Docusaurus site"

# Add GitHub remote
git remote add origin https://github.com/moizalpha/physical-ai-capstone.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main

# Build and deploy to GitHub Pages
USE_SSH=false GIT_USER=moizalpha npm run deploy
```

### Step 3: Enable GitHub Pages (Auto-configured)

The `npm run deploy` command automatically:
- Creates a `gh-pages` branch
- Builds your site
- Pushes to the `gh-pages` branch

GitHub Pages should auto-enable. To verify:
1. Go to: https://github.com/moizalpha/physical-ai-capstone/settings/pages
2. Ensure **Source** is set to `gh-pages` branch
3. Your site will be live at: **https://moizalpha.github.io/physical-ai-capstone/**

## 📝 Alternative: GitHub Desktop

If you prefer a GUI:

1. Open GitHub Desktop
2. File → Add Local Repository
3. Choose: `D:\physical ai book\physical-ai\docusaurus-site`
4. Publish repository to GitHub
5. Then run: `npm run deploy` in terminal

## 🔄 Updating Your Site

After making changes:

```bash
cd "D:\physical ai book\physical-ai\docusaurus-site"

# Commit your changes
git add .
git commit -m "Update content"
git push origin main
# Deploy to GitHub Pages
USE_SSH=false GIT_USER=moizalpha npm run deploy
```

## ⚠️ Troubleshooting

### Authentication Issues

If you get authentication errors, use a Personal Access Token:

1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: `repo` (full control)
4. Use token as password when prompted

Or use SSH:
```bash
git remote set-url origin git@github.com:moizalpha/physical-ai-capstone.git
USE_SSH=true npm run deploy
```

### Build Errors

```bash
# Clear cache and rebuild
npm run clear
npm install
npm run build
```

## 🎉 Your Site Will Be Live At:

**https://moizalpha.github.io/physical-ai-capstone/**

Usually takes 2-5 minutes after first deployment.

---

**Need help?** Just ask and I can guide you through any step!
