from infra.base_object import MongoBaseModel


class StockModel(MongoBaseModel):
    # collection = 'stocks'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get('name')
        self.symbol = kwargs.get('symbol')
        self.price = kwargs.get('price')
        self.change = kwargs.get('change')
        self.change_percent = kwargs.get('change_percent')
        self.last_updated = kwargs.get('last_updated')

    def to_dict(self):
        return {
            'name': self.name,
            'symbol': self.symbol,
            'price': self.price,
            'change': self.change,
            'change_percent': self.change_percent,
            'last_updated': self.last_updated
        }