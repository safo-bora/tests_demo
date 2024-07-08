import dotenv from 'dotenv';

dotenv.config();

export const BaseConfig = {
  baseUrl: process.env.BASE_URL ?? 'https://api.trello.com/1',
  trelloApiKey: process.env.TRELLO_API_KEY,
  trelloApiToken: process.env.TRELLO_API_TOKEN,
};
