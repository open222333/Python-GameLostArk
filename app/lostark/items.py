import math


class Material():

    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.quantity = kwargs.get('quantity', 1)  # 單位數量
        self.price = kwargs.get('price', 1)
        self.demand = kwargs.get('demand', 1)  # 需求量

    def get_cost(self):
        return round(self.price / self.quantity, 2) * self.demand


class Items():

    """合成資訊
    """

    def __init__(self, item_name: str, fee: int, unit_of_quantity) -> None:
        self.materials = []
        self.item_name = item_name  # 合成物名稱
        self.fee = fee  # 製作費用
        self.unit_of_quantity = unit_of_quantity  # 製作出單組數量

        self.number = 0
        self.total_units = 0
        self.total_amount = 0

        self.result = {
            "物品名": self.item_name
        }

    def set_number(self, number: int):
        """設置製作數量

        Args:
            number (int): _description_
        """
        self.number = number

    def add_material_list(self, name: str, quantity: int, price: int, demand: int):
        self.materials.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "demand": demand
        })

    def calculate(self):
        """計算
        """
        detail = []
        self.total_units = math.ceil(self.number / self.unit_of_quantity)
        self.total_amount += self.total_units * self.fee

        for material in self.materials:
            required_number_of_unit = math.ceil((material.get("demand") * self.total_units) / material.get("quantity"))
            amount = material.get("price") * (required_number_of_unit)
            self.total_amount += amount
            detail.append({
                '名稱': material.get('name'),
                '需購買數量': required_number_of_unit,
                '費用': amount
            })

        self.result['總費用'] = self.total_amount
        self.result['單個成本'] = round(self.total_amount / (required_number_of_unit * self.unit_of_quantity), 2)
        self.result['材料細節'] = detail

    def get_result(self):
        self.calculate()
        return self.result
