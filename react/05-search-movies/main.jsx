import React from 'react'
import { createRoot } from 'react-dom/client'

import './src/styles/normalize.css'
import './src/styles/simple.css'
import './src/styles/App.css'

import { App } from './src/components/App.jsx'

const root = createRoot(document.getElementById('root'))

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
