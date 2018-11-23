class ShoppingCart:
    def __init__(self, employee_discount = None):
        self._total = 0;
        self._items = {};
        self._employee_discount = employee_discount;
        
    def get_total(self):
        return round(self._total,2)
    def set_total(self,total):
        self._total = total;
    def del_total(self):
        del self._total;
    total = property(get_total, set_total, del_total)
    
    
    def get_items(self):
        return self._items
    def set_items(self,items):
        self._items = items
    def del_items(self):
        del self._items
    items = property(get_items, set_items, del_items)
    
    
    def get_employee_discount(self):
        return self._employee_discount
    def set_employee_discount(self,employee_discount):
        self._employee_discount = employee_discount
    def del_employee_discount(self):
        del self._employee_discount
    employee_discount = property(get_employee_discount, set_employee_discount, del_employee_discount)
    
    def add_item(self, name, price, quantity = 1):
        items = self.items
        if name in items:
            items[name][quantity] = quantity
        else:
            items.update({name:{'price': price, 'quantity': quantity}})
        self.items = items;
        self.total += price*quantity
        self._last_item = name
        return self.total
    
    def mean_item_price(self):
        num_items = sum([self.items[x]['quantity'] for x in self.items])
        return round(float(self.total/num_items),2)
    
    def median_item_price(self):
        prices = [self.items[x]['price'] for x in self.items]
        prices.sort()
        if len(prices)%2:
            return prices[int(len(prices)/2+0.5)]
        else:
            return (prices[int(len(prices)/2)] + prices[int(len(prices)/2+1)])/2
        
    def apply_discount(self):
        if self.employee_discount:
            return self.total * (1-float(self.employee_discount/100))
        else:
            return 'Sorry, there is no discount applied to your cart : ('
        
    def item_names(self):
        return list(self.items.keys())
    
    def void_last_item(self):
        if len(self._items):
            if self._items[self._last_item]['quantity'] > 1:
                self._items[self._last_item]['quantity'] -= 1
            else:
                self._items.pop(self._last_item)
            self._total -= self._items[self._last_item]['price']
            return self._total
        else:
            return 'There are no items in your cart!'
        
        
        
        
        
