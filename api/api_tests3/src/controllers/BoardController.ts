import { type AxiosResponse } from 'axios';
import AxiosController, { type RequestOptions } from './AxiosController';
import { BaseConfig } from '../utils/BaseConfig';

export class BoardController extends AxiosController {
  private apiKey: string;

  private apiToken: string;

  constructor(options: RequestOptions = { baseUrl: BaseConfig.baseUrl }) {
    super(options);
    this.apiKey = BaseConfig.trelloApiKey;
    this.apiToken = BaseConfig.trelloApiToken;
  }

  private withAuth(): this {
    this.searchParams({ key: this.apiKey, token: this.apiToken });
    return this;
  }

  public async createBoard(name: string): Promise<AxiosResponse<any>> {
    return this.searchParams({ name }).withAuth().req<any>('POST', '/boards/');
  }

  public async getBoard(id: string): Promise<AxiosResponse<any>> {
    return this.withAuth().req<any>('GET', `/boards/${id}`);
  }

  public async updateBoard(id: string, data: any): Promise<AxiosResponse<any>> {
    return this.withAuth().body(data).req<any>('PUT', `/boards/${id}`);
  }

  public async deleteBoard(id: string): Promise<AxiosResponse<any>> {
    return this.withAuth().req<any>('DELETE', `/boards/${id}`);
  }
}
