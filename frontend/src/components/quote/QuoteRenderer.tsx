import useSWR from "swr";
import type { Quote } from "./types";

import {
  Container,
  Image,
  Paper,
  Stack,
  Text,
  Title,
} from '@mantine/core';

export function QuoteRenderer() {
    const quoteFetcher = async (url: string): Promise<Quote> => {
        const res = await fetch(url);
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
    };
    
    const { data, error, isLoading } = useSWR('http://localhost:8000/quote_of_the_day', quoteFetcher);

    console.log(data)

    return (
      <Container size="sm">
        <Paper shadow="md" radius="lg" p="xl">
          <Stack align="center">

            <Image
                src="https://m.media-amazon.com/images/M/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_QL75_UY562_CR9,0,380,562_.jpg"
                radius="md"
                h={200}
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