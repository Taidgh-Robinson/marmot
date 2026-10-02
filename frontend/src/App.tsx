import '@mantine/core/styles.css';
import useSWR from 'swr';

import {
  Center,
  Container,
  MantineProvider,
  Paper,
  Stack,
  Text,
  Title,
} from '@mantine/core';
import { QuoteRenderer } from './components/quote/QuoteRenderer';

function QuoteApp() {
  
  return (<div>
    <QuoteRenderer /> 
    <Center mih="100vh">
    </Center>
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