def calculate_goods(total_goods, goods_on_first_second, goods_on_second_third):
    goods_third = total_goods - goods_on_first_second
    goods_second = goods_on_second_third - goods_third
    goods_first = goods_on_first_second - goods_second
    
    return goods_first, goods_second, goods_third

def calculate_computer_cost(due_date, payment_per_month):
    return due_date * payment_per_month

def calculate_order_cost(need_big_pizzas, need_middle_pizzas, need_juices, need_cakes, need_water):
    return (need_big_pizzas * 274) + (need_middle_pizzas * 218) + (need_juices * 35) + (need_cakes * 350) + (need_water * 21)

def calculate_pages(all_photos, photos_on_page):
    if all_photos % photos_on_page == 0:
        return all_photos // photos_on_page
    else:
        return (all_photos // photos_on_page) + 1

def unique_symbols_check(user_input):
    input_set = set(user_input)
    return len(input_set) > 10