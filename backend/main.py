import uvicorn
from utils import Table


cols = ('title', 'completed')
data = Table(cols)
data.create('task A', False)

if __name__ == '__main__':

    uvicorn.run(
        'todo:todo_api',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
