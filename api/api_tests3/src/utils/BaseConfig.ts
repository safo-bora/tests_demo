import dotenv from 'dotenv';

dotenv.config();

export const BaseConfig = {
  baseUrl: process.env.BASE_URL ?? 'https://api.trello.com/1',
  apiKey: process.env.TRELLO_API_KEY,
  apiToken: process.env.TRELLO_API_TOKEN,
};
