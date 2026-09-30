import '@mantine/core/styles.css';

import {
  Button,
  Center,
  Container,
  MantineProvider,
  Paper,
  Stack,
  Text,
  Title,
} from '@mantine/core';

function QuoteApp() {
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