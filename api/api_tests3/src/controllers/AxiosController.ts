import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from 'axios';
import { logger } from '../utils/logger';

export interface RequestOptions {
  baseUrl?: string;
  queryParams?: Record<string, string>;
  body?: any;
  headers?: Record<string, string>;
}

export default class AxiosController {
  private instance: AxiosInstance;

  protected options: RequestOptions;

  constructor(options: RequestOptions = { baseUrl: process.env.BASE_URL }) {
    this.options = options;
    this.instance = axios.create({
      baseURL: this.options.baseUrl,
    });

    this.instance.interceptors.request.use(request => {
      logger.info(`Request: ${request.method?.toUpperCase()} ${request.url}`);
      return request;
    });

    this.instance.interceptors.response.use(
      response => {
        logger.info(`Response: ${response.status} ${response.statusText}`);
        return response;
      },
      error => {
        logger.error(`Error: ${error.response?.status} ${error.response?.statusText}`);
        return Promise.reject(error);
      },
    );
  }

  public async get<T>(path: string): Promise<AxiosResponse<T>> {
    return this.req<T>('GET', path);
  }

  public async post<T>(path: string): Promise<AxiosResponse<T>> {
    return this.req<T>('POST', path);
  }

  public async put<T>(path: string): Promise<AxiosResponse<T>> {
    return this.req<T>('PUT', path);
  }

  public async patch<T>(path: string): Promise<AxiosResponse<T>> {
    return this.req<T>('PATCH', path);
  }

  public async delete<T>(path: string): Promise<AxiosResponse<T>> {
    return this.req<T>('DELETE', path);
  }

  public searchParams(queryParams: Record<string, any>): this {
    this.options = {
      ...this.options,
      queryParams: {
        ...this.options.queryParams,
        ...queryParams,
      },
    };
    return this;
  }

  public body(data: any): this {
    this.options = {
      ...this.options,
      body: data,
    };
    return this;
  }

  public headers(data: Record<string, string>): this {
    this.options = {
      ...this.options,
      headers: {
        ...this.options.headers,
        ...data,
      },
    };
    return this;
  }

  protected async req<T>(method: string, path: string, options?: RequestOptions): Promise<AxiosResponse<T>> {
    const finalOptions = options || this.options;
    const config: AxiosRequestConfig = {
      method,
      url: path,
      params: finalOptions.queryParams,
      headers: { ...finalOptions.headers },
      data: method === 'GET' ? undefined : finalOptions.body,
    };

    try {
      const response = await this.instance.request<T>(config);
      return response;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        logger.error(`Axios error: ${error.message}`);
        if (error.response) {
          logger.error(`Response data: ${JSON.stringify(error.response.data)}`);
        }
      } else {
        logger.error(`Unexpected error: ${JSON.stringify(error)}`);
      }
      throw error;
    } finally {
      this.options.body = undefined;
      this.options.queryParams = undefined;
    }
  }
}
