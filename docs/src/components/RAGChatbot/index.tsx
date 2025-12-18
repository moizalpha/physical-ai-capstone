/**
 * RAG Chatbot Component
 * Embedded chatbot for querying the Physical AI book content
 */

import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: Source[];
}

interface Source {
  title: string;
  file_path: string;
  chunk_id: number;
  score: number;
}

interface RAGChatbotProps {
  apiUrl?: string;
}

export default function RAGChatbot({ apiUrl = 'http://localhost:8000' }: RAGChatbotProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: 'Hi! I can answer questions about the Physical AI book. You can also select text on the page and ask me about it!'
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Handle text selection
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      const text = selection?.toString().trim();
      if (text && text.length > 0) {
        setSelectedText(text);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => document.removeEventListener('mouseup', handleSelection);
  }, []);

  // Focus input when chatbot opens
  useEffect(() => {
    if (isOpen) {
      inputRef.current?.focus();
    }
  }, [isOpen]);

  const sendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage: Message = {
      role: 'user',
      content: inputValue
    };

    setMessages(prev => [...prev, userMessage]);
    const question = inputValue;
    setInputValue('');
    setIsLoading(true);

    try {
      const response = await fetch(`${apiUrl}/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: question,
          selected_text: selectedText || null,
          top_k: 5
        })
      });

      if (!response.ok) {
        throw new Error('Failed to get response from server');
      }

      const data = await response.json();

      const assistantMessage: Message = {
        role: 'assistant',
        content: data.answer,
        sources: data.sources
      };

      setMessages(prev => [...prev, assistantMessage]);
      setSelectedText(''); // Clear selected text after using it

    } catch (error) {
      const errorMessage: Message = {
        role: 'assistant',
        content: `⚠️ Backend not running. To use the chatbot:\n\n1. Start the backend:\n   cd rag-backend-free\n   uvicorn app.main:app --reload\n\n2. Or follow FREE-RAG-SETUP.md for full setup`
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearSelectedText = () => {
    setSelectedText('');
  };

  return (
    <>
      {/* Chatbot Toggle Button */}
      <button
        className={styles.chatbotToggle}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle chatbot"
      >
        {isOpen ? '✕' : '💬'}
      </button>

      {/* Chatbot Window */}
      {isOpen && (
        <div className={styles.chatbotWindow}>
          {/* Header */}
          <div className={styles.chatbotHeader}>
            <h3>📚 Ask About the Book</h3>
            <button
              onClick={() => setIsOpen(false)}
              className={styles.closeButton}
              aria-label="Close chatbot"
            >
              ✕
            </button>
          </div>

          {/* Selected Text Banner */}
          {selectedText && (
            <div className={styles.selectedTextBanner}>
              <div className={styles.selectedTextContent}>
                <strong>Selected text:</strong>
                <p>{selectedText.substring(0, 100)}{selectedText.length > 100 ? '...' : ''}</p>
              </div>
              <button onClick={clearSelectedText} className={styles.clearButton}>
                ✕
              </button>
            </div>
          )}

          {/* Messages */}
          <div className={styles.chatbotMessages}>
            {messages.map((message, index) => (
              <div
                key={index}
                className={`${styles.message} ${styles[message.role]}`}
              >
                <div className={styles.messageContent}>
                  {message.content}
                </div>
                {message.sources && message.sources.length > 0 && (
                  <div className={styles.sources}>
                    <strong>Sources:</strong>
                    <ul>
                      {message.sources.slice(0, 3).map((source, idx) => (
                        <li key={idx}>
                          {source.title} (Score: {source.score.toFixed(2)})
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
            {isLoading && (
              <div className={`${styles.message} ${styles.assistant}`}>
                <div className={styles.messageContent}>
                  <span className={styles.loadingDots}>●●●</span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input */}
          <div className={styles.chatbotInput}>
            <textarea
              ref={inputRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask a question about the book..."
              rows={2}
              disabled={isLoading}
            />
            <button
              onClick={sendMessage}
              disabled={isLoading || !inputValue.trim()}
              className={styles.sendButton}
            >
              {isLoading ? '...' : '➤'}
            </button>
          </div>
        </div>
      )}
    </>
  );
}
