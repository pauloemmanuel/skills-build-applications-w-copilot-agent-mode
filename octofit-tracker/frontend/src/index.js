import React from 'react';
import { createRoot } from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';

const codespace = process.env.REACT_APP_CODESPACE_NAME;
const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
console.log('[index] REACT_APP_CODESPACE_NAME:', process.env.REACT_APP_CODESPACE_NAME);
console.log('[index] API base URL:', baseUrl);

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
