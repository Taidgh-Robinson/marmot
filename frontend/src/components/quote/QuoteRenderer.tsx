import useSWR from "swr";
import type { Quote } from "./types";
import { API_BASE_URL } from "../../config"
import { useParams } from 'react-router-dom';

import {
  Center,
  Container,
  Image,
  Loader,
  Paper,
  Stack,
  Text,
  Title,
} from "@mantine/core";


export function QuoteRenderer() {
  const quoteFetcher = async (url: string): Promise<Quote> => {
    const res = await fetch(url);

    if (!res.ok) {
      throw new Error("Failed to fetch");
    }

    return res.json();
  };

  const { month, day, year } = useParams();

  // If there is no month or day, we are on the homepage
  const isHomepage = !month || !day || !year;
  if (isHomepage) {
    var fetch_url = `${API_BASE_URL}/quote_of_the_day`
  }
  else {
    var fetch_url = `${API_BASE_URL}/get_quote?date=${month}/${day}/${year}`
  }

  const { data, error, isLoading } = useSWR(
    fetch_url,
    quoteFetcher
  );

  if (isLoading) {
    return (
      <Center mih={500}>
        <Stack align="center" gap="sm">
          <Loader size="md" />
          <Text c="dimmed" size="sm">
            Loading today's movie quote, this may take a while...
          </Text>
        </Stack>
      </Center>
    );
  }

  if (error || !data) {
    return (
      <Center mih={500}>
        <Text c="red" ta="center">
          Failed to load quote. Please try again later.
        </Text>
      </Center>
    );
  }

  if (data.quote === null) {
    return (
      <Container size="xs" py={60}>
        <Paper
          radius="xl"
          p="xl"
          shadow="xl"
          withBorder
          style={{
            background:
              "linear-gradient(145deg, var(--mantine-color-dark-7), var(--mantine-color-dark-8))",
          }}
        >
          <Stack gap="md" align="center" py="xl">
            <Text
              size="xs"
              tt="uppercase"
              fw={700}
              c="dimmed"
              style={{ letterSpacing: "0.16em" }}
            >
              Quote of the day
            </Text>

            <Title order={2} ta="center">
              No quote today
            </Title>

            <Text c="dimmed" ta="center">
              There isn't a movie quote available for today. Check back tomorrow!
            </Text>
          </Stack>
        </Paper>
      </Container>
    );
  }

  return (
    <Container size="xs" py={60}>
      <Paper
        radius="xl"
        p="xl"
        shadow="xl"
        withBorder
        style={{
          background:
            "linear-gradient(145deg, var(--mantine-color-dark-7), var(--mantine-color-dark-8))",
        }}
      >
        <Stack gap="xl">
          <Image
            src={data.poster_url}
            alt={`${data.movie} poster`}
            radius="lg"
            h={440}
            fit="contain"
            mx="auto"
            style={{
              maxWidth: 300,
              filter: "drop-shadow(0 14px 24px rgba(0, 0, 0, 0.45))",
            }}
          />

          <Stack gap="xs" align="center">
            <Text
              size="xs"
              tt="uppercase"
              fw={700}
              c="dimmed"
              style={{ letterSpacing: "0.16em" }}
            >
              Quote of the day
            </Text>

            <Title
              order={2}
              ta="center"
              fw={700}
              style={{ lineHeight: 1.15 }}
            >
              {data.movie}
            </Title>
          </Stack>

          <Text
            ta="center"
            fs="italic"
            fw={500}
            style={{
              fontSize: "clamp(1.4rem, 3vw, 2rem)",
              lineHeight: 1.45,
              maxWidth: 520,
              marginInline: "auto",
            }}
          >
            “{data.quote}”
          </Text>
        </Stack>
      </Paper>
    </Container>
  );
}