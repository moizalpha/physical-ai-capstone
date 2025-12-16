// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: '📋 Planning & Specification',
      collapsed: false,
      items: ['planning/overview', 'planning/specification'],
    },
    {
      type: 'category',
      label: '📚 1. Literature Review (P1)',
      collapsed: false,
      items: ['literature-review/overview'],
    },
    {
      type: 'category',
      label: '🎓 2. Curriculum Design (P2)',
      items: ['curriculum-design/overview'],
    },
    {
      type: 'category',
      label: '⚙️ 3. ROS 2 Technical (P3)',
      items: ['ros2-technical/overview'],
    },
    {
      type: 'category',
      label: '🎮 4. Simulation Platforms (P4)',
      items: ['simulation-platforms/overview'],
    },
    {
      type: 'category',
      label: '🤖 5. AI-Robot Integration (P5)',
      items: ['ai-integration/overview'],
    },
    {
      type: 'category',
      label: '📊 6. Evaluation Framework (P6)',
      items: ['evaluation/overview'],
    },
    {
      type: 'category',
      label: '🎯 Conclusion & References',
      items: ['conclusion', 'references'],
    },
  ],
};

module.exports = sidebars;
