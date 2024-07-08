import { expect } from 'chai';
import { faker } from '@faker-js/faker';
import { BoardController } from '../controllers/BoardController';

describe('Board', function () {
  let board: BoardController;
  let boardId: string;

  before(function () {
    board = new BoardController();
  });

  it('should create a new board', async function () {
    const boardName = faker.company.name();
    const response = await board.createBoard(boardName);

    expect(response.status).to.equal(200);
    expect(response.data).to.have.property('id');

    boardId = response.data.id;
  });

  it('should get the created board', async function () {
    const response = await board.getBoard(boardId);

    expect(response.status).to.equal(200);
    expect(response.data.id).to.equal(boardId);
  });

  it('should update the board name', async function () {
    const newBoardName = faker.company.name();
    const response = await board.updateBoard(boardId, { name: newBoardName });

    expect(response.status).to.equal(200);
    expect(response.data.name).to.equal(newBoardName);
  });

  it('should delete the board', async function () {
    const response = await board.deleteBoard(boardId);
    expect(response.status).to.equal(200);

    await board.getBoard(boardId).then(
      () => expect.fail('The status code is not correct'),
      error => {
        expect(error.response.status).to.equal(404);
        expect(error.response.data).to.equal('The requested resource was not found.');
      },
    );
  });
});
