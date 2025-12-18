# Docusaurus Setup for Physical AI Capstone Paper

## ✅ What's Been Created

A complete Docusaurus website structure for presenting your Physical AI Capstone research paper online.

### Directory Structure

```
docusaurus-site/
├── package.json                  # Dependencies and scripts
├── docusaurus.config.js         # Site configuration
├── sidebars.js                  # Navigation structure
├── README.md                    # Setup instructions
├── setup.sh                     # Quick setup script (Unix/Mac)
├── .gitignore                   # Git ignore patterns
│
├── docs/                        # Content directory
│   ├── intro.md                # Landing introduction
│   ├── planning/               # Planning documents
│   │   └── overview.md        # Planning overview with links
│   └── literature-review/      # P1 content
│       └── overview.md        # Literature review overview
│
├── src/
│   ├── pages/
│   │   ├── index.js           # Homepage with features
│   │   └── index.module.css   # Homepage styles
│   └── css/
│       └── custom.css         # Global styles
│
└── static/                     # Static assets (images, etc.)
    └── img/                   # Image directory
```

## 🚀 Quick Start

### Option 1: Using Setup Script (Unix/Mac/Git Bash)

```bash
cd docusaurus-site
./setup.sh
npm start
```

### Option 2: Manual Setup (Windows/All Platforms)

```bash
cd docusaurus-site
npm install
npm start
```

The site will open at `http://localhost:3000`

## 📝 Adding Your Paper Content

### Step 1: Organize Your Content

Your research paper sections should map to Docusaurus docs like this:

```
paper/02-literature-review/        →  docs/literature-review/
├── physical-ai-definitions.md    →  ├── physical-ai-definitions.md
├── ros2-middleware-research.md   →  ├── ros2-middleware.md
├── simulation-technologies.md    →  ├── simulation-technologies.md
└── robotics-education-pedagogy.md→  └── robotics-education.md

paper/03-curriculum-design/        →  docs/curriculum-design/
└── ...                           →  └── ...

(Continue for P3-P6 sections)
```

### Step 2: Add Front Matter

Each markdown file needs front matter at the top:

```markdown
---
sidebar_position: 1
title: "Physical AI Definitions"
---

# Physical AI Definitions

Your content here...
```

### Step 3: Copy Content

```bash
# Example for literature review
cp paper/02-literature-review/*.md docusaurus-site/docs/literature-review/

# Add front matter to each file (manual step)
```

### Step 4: Update Sidebars (If Needed)

Edit `docusaurus-site/sidebars.js` to customize navigation order and grouping.

## 🎨 Customization

### Change Site Title/Tagline

Edit `docusaurus-site/docusaurus.config.js`:

```js
title: 'Your Custom Title',
tagline: 'Your custom tagline',
```

### Change Theme Colors

Edit `docusaurus-site/src/css/custom.css`:

```css
:root {
  --ifm-color-primary: #2e8555;  /* Change to your color */
}
```

### Modify Homepage

Edit `docusaurus-site/src/pages/index.js` to change:
- Feature cards
- Homepage sections
- Call-to-action buttons

## 📦 Building for Production

### Build Static Site

```bash
cd docusaurus-site
npm run build
```

This creates a `build/` directory with static HTML/CSS/JS files.

### Preview Production Build

```bash
npm run serve
```

### Deploy Options

**1. GitHub Pages**
```bash
GIT_USER=<your-username> npm run deploy
```

**2. Netlify**
- Connect your Git repository
- Build command: `npm run build`
- Publish directory: `build`

**3. Vercel**
- Import project from Git
- Framework preset: Docusaurus
- Build command: `npm run build`
- Output directory: `build`

**4. Static File Hosting**
Upload the `build/` directory to any static host:
- AWS S3 + CloudFront
- Azure Static Web Apps
- Google Cloud Storage
- Cloudflare Pages

## 🔗 Site Structure

Your Docusaurus site includes:

### Navigation
- **Homepage** - Landing page with module overview
- **Introduction** - Paper introduction and organization
- **Planning & Specification** - Project docs (spec, plan, tasks, research)
- **Literature Review (P1)** - Physical AI, ROS 2, simulation, education
- **Curriculum Design (P2)** - Module structure and pedagogy
- **ROS 2 Technical (P3)** - Architecture deep-dive
- **Simulation Platforms (P4)** - Gazebo, Unity, Isaac
- **AI-Robot Integration (P5)** - VSLAM, VLA, perception
- **Evaluation Framework (P6)** - Assessment and future
- **Conclusion & References** - Final sections

### Features
✅ Responsive mobile-friendly design
✅ Dark mode toggle
✅ Search functionality (built-in)
✅ Code syntax highlighting (Python, YAML, JSON, Bash)
✅ Interactive task checklists
✅ Clean academic styling
✅ Fast static site generation

## 📚 Content Guidelines

### Markdown Formatting

```markdown
# H1 - Section Title
## H2 - Subsection
### H3 - Sub-subsection

**Bold text**
*Italic text*
`inline code`

\`\`\`python
# Code block with syntax highlighting
def hello():
    print("Hello Physical AI!")
\`\`\`

> Blockquote for important notes

- Bullet list
- Item 2

1. Numbered list
2. Item 2

[Link text](./other-page.md)

![Image alt](./image.png)
```

### Internal Links

Use relative paths:
```markdown
[See planning docs](../planning/overview.md)
[Literature review](./literature-review/overview.md)
```

### Task Lists

```markdown
- [ ] Incomplete task
- [x] Completed task
```

## 🆘 Troubleshooting

### Port Already in Use
```bash
npm start -- --port 3001
```

### Build Errors
```bash
npm run clear   # Clear cache
npm install     # Reinstall dependencies
npm run build   # Try building again
```

### Module Not Found
```bash
rm -rf node_modules package-lock.json
npm install
```

## 📖 Next Steps

1. ✅ **Install dependencies**: Run setup script or `npm install`
2. ✅ **Start dev server**: Run `npm start` and visit http://localhost:3000
3. 📝 **Add content**: Copy your paper sections to `docs/` subdirectories
4. 🎨 **Customize**: Update colors, title, homepage in config files
5. 🚀 **Deploy**: Build and deploy to your chosen hosting platform

## 📞 Resources

- **Docusaurus Docs**: https://docusaurus.io/docs
- **Markdown Guide**: https://www.markdownguide.org/
- **Deployment Guide**: https://docusaurus.io/docs/deployment

---

**Created**: 2025-12-17
**Your project**: D:\physical ai book\physical-ai\docusaurus-site\
**Dev server**: `npm start` → http://localhost:3000
**Build**: `npm run build` → creates `build/` directory
