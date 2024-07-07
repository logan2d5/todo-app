from uuid import uuid4


def uuid():
    return str(uuid4())


class Table:

    def __init__(self, columns):
        self.dict = {}
        self.cols = columns

    def _create_row(self, *args, **kwargs) -> dict:
        row = {}
        for i, col in enumerate(self.cols):
            if i < len(args):
                row[col] = args[i]
            else:
                row[col] = None
        for k in kwargs:
            row[k] = kwargs[k]
        return row

    def _update_row(self, nr, r):
        for col in nr:
            r[col] = nr[col] if nr[col] is not None else r[col]

    def create(self, *args, **kwargs) -> dict:
        tmp = self._create_row(*args, **kwargs)
        item_id = uuid()
        tmp['id'] = item_id
        self.dict[item_id] = tmp
        return tmp

    def read(self, item_id) -> dict:
        if item_id in self.dict:
            return self.dict[item_id]
        else:
            return {}

    def read_all(self) -> list:
        return [self.dict[k] for k in self.dict]

    def update(self, item_id, *args, **kwargs) -> dict:
        if item_id in self.dict:
            tmp = self._create_row(*args, **kwargs)
            self._update_row(tmp, self.dict[item_id])
            return self.dict[item_id]
        else:
            return self._create_row(*args, **kwargs)

    def delete(self, item_id) -> dict:
        if item_id in self.dict:
            return self.dict.pop(item_id)
        else:
            return {}
