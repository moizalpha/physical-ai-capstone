# Physical AI Capstone Quarter - Docusaurus Site

This Docusaurus site presents the Physical AI Capstone Quarter research paper in an interactive, web-based format.

## Quick Start

### Installation

```bash
cd docusaurus-site
npm install
```

### Local Development

```bash
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```bash
USE_SSH=true npm run deploy
```

Not using SSH:

```bash
GIT_USER=<Your GitHub username> npm run deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

## Project Structure

```
docusaurus-site/
├── docs/                          # Documentation files (markdown)
│   ├── intro.md                  # Introduction page
│   ├── planning/                 # Planning & specification docs
│   │   ├── overview.md
│   │   ├── specification.md
│   │   ├── implementation-plan.md
│   │   ├── tasks.md
│   │   └── research-strategy.md
│   ├── literature-review/        # P1 content
│   ├── curriculum-design/        # P2 content
│   ├── ros2-technical/           # P3 content
│   ├── simulation-platforms/     # P4 content
│   ├── ai-integration/           # P5 content
│   └── evaluation/               # P6 content
├── src/
│   ├── pages/                    # Custom pages
│   │   └── index.js             # Homepage
│   └── css/
│       └── custom.css           # Custom styling
├── static/                       # Static files (images, etc.)
├── docusaurus.config.js         # Site configuration
├── sidebars.js                  # Sidebar navigation
└── package.json                 # Dependencies
```

## Content Organization

The site is organized to mirror the research paper structure:

1. **Introduction** - Overview and paper organization
2. **Planning & Specification** - Project planning documents
3. **Literature Review (P1)** - Physical AI, ROS 2, simulation, education
4. **Curriculum Design (P2)** - Module structure and pedagogy
5. **ROS 2 Technical (P3)** - Architecture and integration
6. **Simulation Platforms (P4)** - Gazebo, Unity, Isaac comparison
7. **AI-Robot Integration (P5)** - VSLAM, VLA, perception
8. **Evaluation Framework (P6)** - Assessment and future directions
9. **Conclusion & References** - Summary and bibliography

## Features

- 📱 **Responsive Design** - Mobile-friendly layout
- 🌙 **Dark Mode** - Toggle between light and dark themes
- 🔍 **Search** - Built-in documentation search
- 📊 **Code Syntax Highlighting** - Support for Python, YAML, JSON, Bash
- ✅ **Task Checklists** - Interactive checkboxes for task tracking
- 📚 **Sidebar Navigation** - Easy navigation between sections

## Customization

### Changing the Theme

Edit `docusaurus.config.js` to change:
- Site title and tagline
- Theme colors
- Navbar items
- Footer links

### Adding Content

1. Create markdown files in the `docs/` directory
2. Add front matter for metadata:
   ```md
   ---
   sidebar_position: 1
   ---
   # Your Title
   ```
3. Update `sidebars.js` if needed for custom ordering

### Styling

- Global styles: Edit `src/css/custom.css`
- CSS variables: Defined in `:root` section of custom.css
- Component styles: Create `.module.css` files alongside components

## Converting From Existing Paper Content

To add content from your paper to Docusaurus:

1. **Copy markdown files** from `paper/` directory to corresponding `docs/` subdirectories
2. **Add front matter** to each file:
   ```md
   ---
   sidebar_position: 1
   title: "Your Title"
   ---
   ```
3. **Update internal links** to use Docusaurus routing (e.g., `/docs/section/page`)
4. **Update sidebars.js** if you add new categories or pages

## Next Steps

1. Install dependencies: `npm install`
2. Start development server: `npm start`
3. Add your research paper content to the `docs/` directory
4. Customize the homepage in `src/pages/index.js`
5. Update site config in `docusaurus.config.js`
6. Build and deploy: `npm run build` then deploy to your hosting

## Resources

- [Docusaurus Documentation](https://docusaurus.io/)
- [Markdown Guide](https://www.markdownguide.org/)
- [MDX Documentation](https://mdxjs.com/)

---

**Created**: 2025-12-17
**Framework**: Docusaurus 3.0
**Theme**: Classic with TypeScript
