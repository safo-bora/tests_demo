import { RequestOptions } from '../controllers/AxiosController';
import { BaseConfig } from './BaseConfig';

export function withAuth(options: RequestOptions): RequestOptions {
  return {
    ...options,
    queryParams: {
      ...options.queryParams,
      key: BaseConfig.trelloApiKey,
      token: BaseConfig.trelloApiToken,
    },
  };
}
