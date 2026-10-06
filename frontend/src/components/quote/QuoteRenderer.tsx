import useSWR from "swr";
import type { Quote } from "./types";

import {
  Container,
  Image,
  Paper,
  Stack,
  Text,
  Title,
  Loader
} from '@mantine/core';

export function QuoteRenderer() {
    const quoteFetcher = async (url: string): Promise<Quote> => {
        const res = await fetch(url);
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
    };
    
    const { data, error, isLoading } = useSWR('http://localhost:8000/get_quote?date=07/04/2026', quoteFetcher);

    console.log(data)
    if (isLoading) {
      return (
        <Container size="sm" style={{ minHeight: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <Stack align="center" gap="md">
            <Loader size="lg" />
            <Text c="dimmed">Loading daily quote, this may take a while...</Text>
          </Stack>
        </Container>
      );
    }

    if (error) {
      return (
        <Container size="sm">
          <Text c="red" ta="center">Failed to load quote. Please try again later.</Text>
        </Container>
      );
    }

    return (
      <Container size="sm">
        <Paper shadow="md" radius="lg" p="xl">
          <Stack align="center">

            <Image
                src={data?.poster_url}
                radius="md"
                h={512}
                fit="contain"
              />
            

            <Title order={1}>{data?.movie}</Title>

            <Text size="xl" ta="center" fs="italic">
              "{data?.quote}"
            </Text>
          </Stack>
        </Paper>
      </Container>

    )
}