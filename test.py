from models import Production,Customer,Seller,Administrator,Orders,Sale
# print (Production.order_production_data(2))
# print(Production.edit(26,"图书","喜为你疾,药石无医","31.4","20","wei.png","This is i like book","新品上架"))
# print(Production.basket_production_data(2))
# print(Seller.add_new_production(1,28,"0.9","200-20"))
# print(Seller.delete_production(2,25))
# print(Seller.query_seller_product(2))
# print(Production.all_query())
# print(Orders.add_from_basket(14))
# print(Production.query_by_type_type1("图书", "新品上架"))
# print(Seller.search_id_by_name('john'))
# print(Seller.change_production(2,25,'0.9','0'))
# print(Production.basket_production_data(2))
print(Sale.get_price_full_sub(Production.basket_production_data(2)))

