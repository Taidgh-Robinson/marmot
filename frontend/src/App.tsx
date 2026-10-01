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

function QuoteApp() {
  const fetcher = (url) => fetch(url).then((res) => res.json());
  const { data, error, isLoading } = useSWR('http://localhost:8000/quote_of_the_day', fetcher);

  if (error) return <div>Failed to load user.</div>;
  if (isLoading) return <div>Loading...</div>;

  console.log(data)

  return (
    <Center mih="100vh">
      <Container size="sm">
        <Paper shadow="md" radius="lg" p="xl">
          <Stack align="center">
            <Title order={1}>MOVIE TITLE GOES HERE</Title>

            <Text size="xl" ta="center" fs="italic">
              MOVIE QUOTE GOES HERE
            </Text>
          </Stack>
        </Paper>
      </Container>
    </Center>
  );
}

export default function App() {
  return (
    <MantineProvider defaultColorScheme="auto">
      <QuoteApp />
    </MantineProvider>
  );
}