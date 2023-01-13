import crolling_gold_price

#Get The information with gram
def gold_calc_gram(muge, ind):
    bayul = muge / 3.75
    result = ind * bayul
    info = [bayul, result] #0: 무게, 1: 결과값

    print_info(info)
    return info
    
#Get The information with don
def gold_calc_don(muge, ind):
    bayul = muge
    result = ind * bayul
    info = [bayul, result]

    print_info(info)
    return info

#Print The information about bayul, result(price)
def print_info(info):
    bayul = info[0]
    result = info[1]

    print(f"{bayul}돈")
    print(format(result, ','))
    print()

def main():
    #crolling_gold_price.save_data()
    kind_of_golds = crolling_gold_price.load_data()
    price_14k = kind_of_golds['info_14k'][2]
    price_18k = kind_of_golds['info_18k'][2]
    price_24k = kind_of_golds['info_24k'][2]

    gold_calc_gram(3.75, price_14k)
    #gold_calc_gram(6.3, price_18k)
    #gold_calc_gram(806.2, price_24k)

    #sum_gold = one[1] + two[1] + three[1]
    #print(format(sum_gold, ","))

main()