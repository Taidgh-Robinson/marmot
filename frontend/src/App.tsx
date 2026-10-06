import '@mantine/core/styles.css';

import {
  MantineProvider,
} from '@mantine/core';
import { QuoteRenderer } from './components/quote/QuoteRenderer';

function QuoteApp() {
  
  return (
    <div>
      <QuoteRenderer /> 
    </div>
  );
}

export default function App() {
  return (
    <MantineProvider defaultColorScheme="auto">
      <QuoteApp />
    </MantineProvider>
  );
}