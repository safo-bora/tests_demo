import { type AxiosResponse } from 'axios';
import AxiosController, { type RequestOptions } from './AxiosController';
import { withAuth } from '../utils/auth';
import { BaseConfig } from '../utils/BaseConfig';
import { type BoardResponse } from '../interfaces/board';

export class BoardController extends AxiosController {
  constructor(options: RequestOptions = { baseUrl: BaseConfig.baseUrl }) {
    super(options);
  }

  public async getBoard(id: string): Promise<AxiosResponse<BoardResponse>> {
    const options: RequestOptions = withAuth(this.options);
    return this.req<BoardResponse>('GET', `/boards/${id}`, options);
  }

  public async createBoard(name: string): Promise<AxiosResponse<BoardResponse>> {
    const options: RequestOptions = withAuth(this.searchParams({ name }).options);
    return this.req<BoardResponse>('POST', '/boards/', options);
  }

  public async updateBoard(id: string, data: Record<string, any>): Promise<AxiosResponse<BoardResponse>> {
    const options: RequestOptions = withAuth(this.body(data).options);
    return this.req<BoardResponse>('PUT', `/boards/${id}`, options);
  }

  public async deleteBoard(id: string): Promise<AxiosResponse<void>> {
    const options: RequestOptions = withAuth(this.options);
    return this.req<void>('DELETE', `/boards/${id}`, options);
  }
}
