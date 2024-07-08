import { type AxiosResponse } from 'axios';
import AxiosController, { type RequestOptions } from './AxiosController';
import { withAuth } from '../utils/auth';
import { BaseConfig } from '../utils/BaseConfig';

export class BoardController extends AxiosController {
  constructor(options: RequestOptions = { baseUrl: BaseConfig.baseUrl }) {
    super(options);
  }

  public async getBoard(id: string): Promise<AxiosResponse<any>> {
    const options = withAuth(this.options);
    return this.req<any>('GET', `/boards/${id}`, options);
  }

  public async createBoard(name: string): Promise<AxiosResponse<any>> {
    const options = withAuth(this.searchParams({ name }).options);
    return this.req<any>('POST', '/boards/', options);
  }

  public async updateBoard(id: string, data: any): Promise<AxiosResponse<any>> {
    const options = withAuth(this.body(data).options);
    return this.req<any>('PUT', `/boards/${id}`, options);
  }

  public async deleteBoard(id: string): Promise<AxiosResponse<any>> {
    const options = withAuth(this.options);
    return this.req<any>('DELETE', `/boards/${id}`, options);
  }
}
