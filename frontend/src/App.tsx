import { BrowserRouter, Routes, Route } from 'react-router-dom';
import '@mantine/core/styles.css';

import {
  MantineProvider,
} from '@mantine/core';
import { QuoteRenderer } from './components/quote/QuoteRenderer';

export default function App() {
  return (
    <MantineProvider defaultColorScheme="auto">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<QuoteRenderer />} />
          <Route path="/:month/:day/:year?" element={<QuoteRenderer />} />
        </Routes>
      </BrowserRouter>
    </MantineProvider>
  );
}