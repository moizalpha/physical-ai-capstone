import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Read the Paper - 5min ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureItem({title, description, emoji}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center" style={{fontSize: '4rem'}}>
        {emoji}
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          <FeatureItem
            emoji="📡"
            title="Module 1: ROS 2 Nervous System"
            description="Master middleware fundamentals - nodes, topics, services, and Python integration for robot control."
          />
          <FeatureItem
            emoji="🎮"
            title="Module 2: Digital Twin Simulation"
            description="Build virtual environments with Gazebo, Unity, and NVIDIA Isaac for safe experimentation."
          />
          <FeatureItem
            emoji="🧠"
            title="Module 3: AI-Robot Brain"
            description="Integrate VSLAM navigation, Vision-Language-Action models, and multi-modal perception."
          />
        </div>
      </div>
    </section>
  );
}

function ResearchHighlights() {
  return (
    <section className={styles.highlights}>
      <div className="container">
        <div className="row">
          <div className="col col--12">
            <Heading as="h2" className="text--center margin-bottom--lg">
              Research Paper Highlights
            </Heading>
          </div>
        </div>
        <div className="row">
          <div className="col col--3">
            <div className="card">
              <div className="card__header">
                <h3>📚 6 User Stories</h3>
              </div>
              <div className="card__body">
                <p>Comprehensive coverage from literature review to evaluation framework (P1-P6)</p>
              </div>
            </div>
          </div>
          <div className="col col--3">
            <div className="card">
              <div className="card__header">
                <h3>✅ 162 Tasks</h3>
              </div>
              <div className="card__body">
                <p>Detailed implementation plan with setup, research, drafting, and validation phases</p>
              </div>
            </div>
          </div>
          <div className="col col--3">
            <div className="card">
              <div className="card__header">
                <h3>📖 15+ Sources</h3>
              </div>
              <div className="card__body">
                <p>≥50% peer-reviewed with APA 7th edition citations</p>
              </div>
            </div>
          </div>
          <div className="col col--3">
            <div className="card">
              <div className="card__header">
                <h3>🎯 6,500 Words</h3>
              </div>
              <div className="card__body">
                <p>Target length within 5,000-7,000 academic standard</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="A comprehensive curriculum for Physical AI education integrating ROS 2, simulation technologies, and AI-robot interaction">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <ResearchHighlights />
      </main>
    </Layout>
  );
}
