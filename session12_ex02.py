saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True :
    print("""
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
""")
    choice = input("Vui lòng nhập (1-7): ").strip()
    if choice == '1' :
        if saving_accounts == [] :
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else :
            print("Danh sách sổ tiết kiệm:")
            for i, acc in enumerate(saving_accounts, start=1) :
                print(f"{i}. Mã sổ: {acc['account_id']:<6} | Khách hàng: {acc['customer_name']:<15} |"
                      f"Số tiền gửi: {acc['balance']:<10} | Kỳ hạn: {acc['term_months']:<2} tháng |"
                      f"Lãi suất: {acc['interest_rate']:<4}%/năm | Trạng thái: {acc['status']}"
                    )
    elif choice == '2':
        is_found = False
        check_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        for acc in saving_accounts:
            if check_id == acc['account_id']:
                print("Mã sổ tiết kiệm đã tồn tại!")
                break
        else:
            add_name = input("Nhập tên khách hàng: ").strip()
            if add_name == "":
                print("Tên khách hàng không được để trống!")
                continue

            add_price = int(input("Nhập số tiền gửi mới: "))
            if add_price <= 0:
                print("Số tiền gửi không hợp lệ!")
                continue

            add_term = int(input("Nhập kỳ hạn gửi theo tháng: "))
            if add_term <= 0:
                print("Kỳ hạn không hợp lệ!")
                continue

            add_rate = float(input("Nhập lãi suất mới: "))
            if add_rate <= 0:
                print("Số lãi suất không hợp lệ!")
                continue
            new_account = {
                "account_id": check_id,
                "customer_name": add_name,
                "balance": add_price,
                "term_months": add_term,
                "interest_rate": add_rate,
                "status": "active"
            }
            saving_accounts.append(new_account)
            print("Thêm sổ tiết kiệm mới thành công!")
    elif choice == '3':
        is_found = False
        check_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
        for acc in saving_accounts:
            if check_id == acc['account_id']:
                is_found = True
                if acc['status'] != "active":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                else:
                    up_name = input("Nhập tên khách hàng mới: ").strip()
                    if up_name == "":
                        print("Tên khách hàng mới không được để trống!")
                    else:
                        up_price = int(input("Nhập số tiền gửi mới: "))
                        if up_price <= 0:
                            print("Số tiền gửi mới không hợp lệ")
                        else:
                            up_term = int(input("Nhập kỳ hạn mới theo tháng: "))
                            if up_term <= 0:
                                print("Kỳ hạn mới không hợp lệ")
                            else:
                                up_rate = float(input("Nhập lãi suất năm mới: "))
                                if up_rate <= 0:
                                    print("Lãi suất năm mới không hợp lệ")
                                else:
                                    acc['customer_name'] = up_name
                                    acc['balance'] = up_price
                                    acc['term_months'] = up_term
                                    acc['interest_rate'] = up_rate
                                    print("Cập nhật thành công!")
                break  
        if is_found == False:
            print("Không tìm thấy mã sổ tiết kiệm!")
    elif choice == '4':
        is_found = False
        check_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
        for acc in saving_accounts:
            if check_id == acc['account_id']:
                is_found = True
                if acc['status'] == "closed":
                    print("Sổ tiết kiệm này đã được tất toán từ trước!")
                else:
                    acc['status'] = "closed"
                    print(f"Tất toán thành công sổ tiết kiệm {check_id}!")
                    print("Sổ đã được chuyển sang trạng thái 'closed' để lưu trữ lịch sử.")
                break
                
        if is_found == False:
            print("Không tìm thấy mã sổ tiết kiệm!")
                    
    elif choice == '5':
        is_found = False
        check_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
        
        for acc in saving_accounts:
            if check_id == acc['account_id']:
                is_found = True
                
                if acc['status'] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                else:
                    bill_balance = acc['balance']
                    bill_rate = acc['interest_rate']
                    bill_term = acc['term_months']
                    
                    # Tiền lãi = Số tiền gửi * Lãi suất năm / 100 * Kỳ hạn gửi / 12
                    interest = bill_balance * (bill_rate / 100) * (bill_term / 12)
                    # Tổng tiền nhận khi đến hạn = Số tiền gửi + Tiền lãi
                    total_bill = bill_balance + interest
                    
                    print(f"Mã sổ: {check_id}")
                    print(f"Khách hàng: {acc['customer_name']}")
                    print(f"Tiền lãi dự kiến: {int(interest)}đ")
                    print(f"Tổng tiền nhận khi đến hạn: {int(total_bill)}đ")
                break

        if is_found == False:
            print("Không tìm thấy mã sổ tiết kiệm!")
    elif choice == '6':
        is_found = False
        check_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
        for acc in saving_accounts:
            if check_id == acc['account_id']:
                is_found = True
                if acc['status'] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                else:
                    thuc_gui = int(input("Nhập số tháng thực gửi: "))
                    if thuc_gui <= 0:
                        print("Số tháng thực gửi không hợp lệ")
                    else:
                        goi_tien = acc['balance']
                        ky_han_goc = acc['term_months']
                        
                        if thuc_gui < ky_han_goc:
                            print("Áp dụng lãi suất 0.5%/năm")
                            lai_suat_ap_dung = 0.5
                        else:
                            print("Áp dụng lãi suất ban đầu")
                            lai_suat_ap_dung = acc['interest_rate']
                        # Tiền lãi thực nhận = Số tiền gửi * Lãi suất áp dụng / 100 * Số tháng thực gửi / 12
                        tien_lai_thuc = goi_tien * (lai_suat_ap_dung / 100) * (thuc_gui / 12)
                        # Tổng tiền thực nhận = Số tiền gửi + Tiền lãi thực nhận
                        tong_thuc_nhan = goi_tien + tien_lai_thuc
                        
                        print(f"Mã sổ: {check_id}")
                        print(f"Khách hàng: {acc['customer_name']}")
                        print(f"Lãi suất áp dụng: {lai_suat_ap_dung}%/năm")
                        print(f"Tiền lãi thực nhận: {int(tien_lai_thuc)}đ")
                        print(f"Tổng tiền thực nhận: {int(tong_thuc_nhan)}đ")
                break
                
        if is_found == False:
            print("Không tìm thấy mã sổ tiết kiệm!")
    elif choice == '7':
        print("Thoát chương trình")
        break
    else :
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
