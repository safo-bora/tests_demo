import { type AxiosResponse } from 'axios';
import { BoardController } from '../controllers/BoardController';

export class BoardClient {
  private boardController: BoardController;

  constructor() {
    this.boardController = new BoardController();
  }

  public async createBoard(name: string): Promise<any> {
    try {
      const response: AxiosResponse<any> = await this.boardController.createBoard(name);
      return response;
    } catch (error) {
      console.error('Error creating board:', error);
      throw error;
    }
  }

  public async getBoard(id: string): Promise<any> {
    try {
      const response: AxiosResponse<any> = await this.boardController.getBoard(id);
      return response;
    } catch (error) {
      console.error('Error fetching board:', error);
      throw error;
    }
  }

  public async updateBoard(id: string, data: any): Promise<any> {
    try {
      const response: AxiosResponse<any> = await this.boardController.updateBoard(id, data);
      return response;
    } catch (error) {
      console.error('Error updating board:', error);
      throw error;
    }
  }

  public async deleteBoard(id: string): Promise<any> {
    try {
      const response: AxiosResponse<any> = await this.boardController.deleteBoard(id);
      return response;
    } catch (error) {
      console.error('Error deleting board:', error);
      throw error;
    }
  }
}
