/**
 * Root component wrapper for Docusaurus
 * This adds the RAG chatbot to all pages
 */

import React from 'react';
import RAGChatbot from '../components/RAGChatbot';

export default function Root({ children }) {
  // Default to localhost for development
  // Update this URL when you deploy your backend
  const apiUrl = 'http://localhost:8000';

  return (
    <>
      {children}
      <RAGChatbot apiUrl={apiUrl} />
    </>
  );
}
