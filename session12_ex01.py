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
    print("""
--- SHOPEE CART MANAGEMENT SYSTEM ---
1. Xem chi tiết giỏ hàng và tính tổng tiền
2. Thêm sản phẩm mới / cộng dồn số lượng 
3. Cập nhật số lượng của 1 sản phẩm
4. Xóa sản phẩm khỏi kho hàng
5. Thoát chương trình
""")
    choice = input("Mời bạn chọn chức năng(1-5): ")
    if choice == '1' :
        if cart_items == [] :
            print("Giỏ hàng hiện đang trống")
            continue
        else :
            total_cart_all = 0
            count_num = 0
            print("STT | Mã SP | Tên sản phẩm           | SL  | Đơn giá       | Thành tiền")
            for i, cart in enumerate(cart_items, start=1) :
                total_cart = cart['number'] * cart['price']
                total_cart_all += total_cart
                count_num += cart["number"]
                print(f"{i:<3} | {cart['id']:<5} | {cart['name']:<22} | {cart['number']:<3} | {cart['price']:<12}đ | {total_cart}đ")
        
            print(f"Tổng số lượng sản phẩm trong giỏ: {count_num}")
            print(f"TỔNG TIỀN THANH TOÁN: {total_cart_all}đ")

    elif choice == '2' :
        is_found = False
        check_id = input("Nhập mã sản phẩm để thêm:").strip().upper()
        for cart in cart_items :
            if check_id == cart['id'] :
                print("Mã sản phẩm đã tồn tại!")
                add_number = int(input("Nhập số lượng để thêm: "))
                if add_number <= 0:
                    print("Số lượng không hợp lệ!")
                else :
                    cart['number'] += add_number
                    print("Thêm số lượng thành công!")
                    is_found = True
                break
        if is_found == False :
            add_name = input("Nhập tên sản phẩm để thêm: ")
            add_number = int(input("Nhập số lượng sản phẩm để thêm: "))
            if add_number <= 0 :
                print("Số lượng không hợp lệ!")
            else :
                add_price = int(input("Nhập đơn giá để thêm: "))
                if add_price < 0 :
                    print("Số đơn giá không hợp lệ!")
                else :
                    new_cart = {
                        "id" : check_id,
                        "name": add_name,
                        "number": add_number,
                        "price": add_price
                    }
                    print("Thêm thành công!")
                    cart_items.append(new_cart)
                    is_found = True
                    
    elif choice == "3":
        is_found = False
        check_id = input("Nhập mã sản phẩm để cập nhật:").strip().upper()
        for cart in cart_items :
            if check_id == cart["id"] :
                up_id = input("Nhập id mới: ").strip().upper()
                up_name = input("Nhập tên mới: ")
                up_number = int(input("Nhập số lượng mới: "))
                if up_number <= 0:
                    print("Số lượng không hợp lệ!")
                else :
                    cart['id'] = up_id
                    cart['name'] = up_name
                    cart['number'] = up_number
                    print("Cập nhật thành công!")
                    is_found = True
                break
        if is_found == False :
            print("Mã sản phẩm không tồn tại trong giỏ hàng!")
    elif choice == '4':
        is_found = False
        check_id = input("Nhập mã sản phẩm để xóa:").strip().upper()
        for cart in cart_items :
            if check_id == cart["id"] :
                cart_items.remove(cart)
                print("Xóa thành công!")
                is_found = True
                break
        if is_found == False :
            print("Mã sản phẩm không tồn tại!")

    elif choice == '5':
        print("Thoát chương trình")
        break
    else :
        print("Vui lòng nhập chức năng (1-5)")