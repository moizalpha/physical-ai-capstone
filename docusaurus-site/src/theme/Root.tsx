/**
 * Root component wrapper for Docusaurus
 * This adds the RAG chatbot to all pages
 */

import React from 'react';
import RAGChatbot from '../components/RAGChatbot';

export default function Root({ children }) {
  return (
    <>
      {children}
      <RAGChatbot apiUrl={process.env.REACT_APP_API_URL || 'http://localhost:8000'} />
    </>
  );
}
