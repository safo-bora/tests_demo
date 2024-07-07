import dotenv from 'dotenv';
dotenv.config();

export const API_KEY = process.env.TRELLO_API_KEY!;
export const TOKEN = process.env.TRELLO_API_TOKEN!;
export const BASE_URL = process.env.BASE_URL ?? 'https://api.trello.com/1';
