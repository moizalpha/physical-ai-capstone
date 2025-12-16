// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const {themes} = require('prism-react-renderer');
const lightTheme = themes.github;
const darkTheme = themes.dracula;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI Capstone Quarter',
  tagline: 'Integrating ROS 2, Simulation Technologies, and AI-Robot Interaction',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://moizalpha.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/physical-ai-capstone/',

  // GitHub pages deployment config.
  organizationName: 'moizalpha', // Usually your GitHub org/user name.
  projectName: 'physical-ai-capstone', // Usually your repo name.

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Remove this to remove the "edit this page" links.
          editUrl: undefined,
        },
        blog: {
          showReadingTime: true,
          // Remove this to remove the "edit this page" links.
          editUrl: undefined,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Physical AI Capstone',
        logo: {
          alt: 'Physical AI Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentation',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/your-org/physical-ai-capstone',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro',
              },
              {
                label: 'Literature Review',
                to: '/docs/literature-review/overview',
              },
            ],
          },
          {
            title: 'Research Paper Sections',
            items: [
              {
                label: 'Curriculum Design',
                to: '/docs/curriculum-design/overview',
              },
              {
                label: 'ROS 2 Technical',
                to: '/docs/ros2-technical/overview',
              },
              {
                label: 'Simulation Platforms',
                to: '/docs/simulation-platforms/overview',
              },
            ],
          },
          {
            title: 'Resources',
            items: [
              {
                label: 'Planning Documents',
                to: '/docs/planning/overview',
              },
              {
                label: 'References',
                to: '/docs/references',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI Capstone Project. Built with Docusaurus.`,
      },
      prism: {
        theme: lightTheme,
        darkTheme: darkTheme,
        additionalLanguages: ['python', 'bash', 'yaml', 'json'],
      },
    }),
};

module.exports = config;
