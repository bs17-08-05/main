import csv

def make_csv_file(orders, response):
    writer = csv.writer(response)
    writer.writerow(['ID','Time', 'Customer name', 'Customer phone', 'address',
        'Delivered', 'Finished', 'Price', 'Order'])
    
    for order in orders:
        writer.writerow([order.id, order.time.strftime('%d-%m-%Y %H:%M:%S'), order.user_name,
            order.user_phone, order.address, order.delivered, order.finished,
            order.price, get_order(order.goods)])
    return response 


def get_order(goods):
    goods = goods.values_list('name','goodsquantityorder__quantity')
    return ';'.join([' * '.join(map(str,good)) for good in goods])
