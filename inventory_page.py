class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.products = ".inventory_item"
        self.add_to_cart_btn = "button.btn_inventory"
        self.cart_icon = ".shopping_cart_link"

    def add_first_product(self):
        self.page.click(self.add_to_cart_btn)

    def go_to_cart(self):
        self.page.click(self.cart_icon)