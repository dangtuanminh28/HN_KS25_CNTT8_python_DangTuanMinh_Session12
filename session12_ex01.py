cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]


while True :
    final_total_price = 0
    final_total_number = 0
    print("""
--- SHOPEE CART MANAGEMENT SYSTEM
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
""")
    choice = input("Mời bạn chọn chức năng(1-5): ").strip()
    if choice == '1' :
        if not cart_items :
            print("Danh sách trống!")
        else :
            print("--- CHI TIẾT GIỎ HÀNG ---")
            print("STT | Mã SP | Tên sản phẩm         | SL | Đơn giá     | Thành tiền")
            for i, cart in enumerate(cart_items, start=1) :
                total_price = cart['number'] * cart['price']
                final_total_price += total_price
                final_total_number += cart['number']

                print(f"{i:<3} | {cart["id"]:<5} | {cart['name']:<20} | "
                      f"{cart['number']:<2} | {cart['price']:<10}đ | "
                      f"{total_price:,}đ")
            
            print(f"==> Tổng số lượng sản phẩm trong giỏ: {final_total_number}")
            print(f"==> Tổng tiền thanh toán: {final_total_price:,}đ")

    elif choice == '2':
        while True:
            add_id = input("Nhập mã sản phẩm: ").strip().upper()
            if add_id == '':
                print("Vui lòng nhập mã!")
                continue
            
            for cart in cart_items:
                if add_id == cart['id']:
                    print("Mã đã tồn tại! Vui lòng nhập lại.")
                    break
            else:
                break
                
        while True:
            add_name = input("Nhập tên sản phẩm: ").strip()
            if add_name != '':
                break
            print("Tên sản phẩm không được để trống!")

        while True:
            try:
                add_number = int(input("Nhập số lượng: "))
                if add_number > 0:
                    break
                print("Số lượng phải lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập một số nguyên!")

        while True:
            try:
                add_price = int(input("Nhập đơn giá: "))
                if add_price > 0:
                    break
                print("Đơn giá phải lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập một số tiền hợp lệ!")

        cart_items.append({
            'id': add_id,
            'name': add_name,
            'number': add_number,
            'price': add_price
        })
        print(f"Đã thêm sản phẩm '{add_name}' thành công!")

    elif choice == '3':
        while True:
            update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            if update_id == '':
                print("Vui lòng nhập mã!")
                continue
            
            for cart in cart_items:
                if update_id == cart['id']:
                    print(f"--- Tìm thấy sản phẩm: {cart['name']} ---")
                    temp_name = cart['name']
                    temp_number = cart['number']
                    temp_price = cart['price']
                    
                    while True:
                        new_name = input("Nhập tên mới: ").strip()
                        if new_name != '':
                            temp_name = new_name
                        break 

                    while True:
                        new_number_str = input("Nhập số lượng mới: ").strip()
                        if new_number_str == '':
                            break 
                        try:
                            new_number = int(new_number_str)
                            if new_number > 0:
                                temp_number = temp_number
                                break
                            print("Số lượng phải lớn hơn 0!")
                        except ValueError:
                            print("Vui lòng nhập một số nguyên!")

                    while True:
                        new_price_str = input("Nhập đơn giá mới: ").strip()
                        if new_price_str == '':
                            break 
                        try:
                            new_price = float(new_price_str)
                            if new_price > 0:
                                temp_price = new_price
                                break
                            print("Đơn giá phải lớn hơn 0!")
                        except ValueError:
                            print("Vui lòng nhập một số tiền hợp lệ!")

                    cart['name'] = temp_name
                    cart['number'] = temp_number
                    cart['price'] = temp_price
                    
                    print("Cập nhật thông tin sản phẩm thành công!")
                    break
            else:
                print("Mã sản phẩm không tồn tại! Vui lòng kiểm tra lại.")
                continue 
            break
                    
    elif choice == '4':
        while True:
            delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            if delete_id == '':
                print("Vui lòng nhập mã!")
                continue
            target_item = None
            for cart in cart_items:
                if delete_id == cart['id']:
                    target_item = cart
                    break
            else:
                print("Mã sản phẩm không tồn tại! Vui lòng kiểm tra lại.")
                continue
            
            cart_items.remove(target_item)
            print(f"Đã xóa sản phẩm  thành công!")
            break
    elif choice == '5' :
        print("Thoát")
        break
    else :
        print("Vui lòng nhập lại(1-5)!")