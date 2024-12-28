# 修改添加备注
import datetime
# 初始化存储收入、支出的列表
incomes = []
expenses = []
budget = 0  # 用户预算
def record_income():
    date = input("请输入日期 (YYYY-MM-DD): ")
    amount = float(input("请输入收入金额: "))
    if amount <= 0:
        print("收入金额必须为正数！")
        return
    category = input("请输入收入类别: ")
    note = input("请输入备注: ")
    incomes.append({"date": date, "amount": amount, "category": category, "note": note})
    print("收入记录已添加！")
def record_expense():
    date = input("请输入日期 (YYYY-MM-DD): ")
    amount = float(input("请输入支出金额: "))
    if amount <= 0:
        print("支出金额必须为正数！")
        return
    category = input("请输入支出类别: ")
    note = input("请输入备注: ")
    expenses.append({"date": date, "amount": amount, "category": category, "note": note})
    print("支出记录已添加！")
def query_records():
    print("\n1. 查询收入记录")
    print("2. 查询支出记录")
    choice = input("请选择查询类型: ")
    if choice == "1":
        records = incomes
        record_type = "收入"
    elif choice == "2":
        records = expenses
        record_type = "支出"
    else:
        print("无效选择！")
        return
    
    print(f"\n所有{record_type}记录:")
    for record in records:
        print(f"日期: {record['date']}, 金额: {record['amount']}, 类别: {record['category']}, 备注: {record['note']}")
def calculate_statistics():
    total_income = sum(record['amount'] for record in incomes)
    total_expense = sum(record['amount'] for record in expenses)
    balance = total_income - total_expense
    print(f"\n总收入: {total_income}")
    print(f"总支出: {total_expense}")
    print(f"当前余额: {balance}")
    if budget > 0:
        if total_expense > budget:
            print("警告：您的支出已超出预算！")
        else:
            print(f"您的支出在预算范围内，剩余预算: {budget - total_expense}")
def set_budget():
    global budget
    budget = float(input("请输入您的预算金额: "))
    print("预算已设置！")
def main_menu():
    while True:
        print("\n个人账单管理系统")
        print("1. 记录收入")
        print("2. 记录支出")
        print("3. 查询记录")
        print("4. 统计")
        print("5. 设置预算")
        print("6. 退出")
        choice = input("请选择操作: ")
        if choice == "1":
            record_income()
        elif choice == "2":
            record_expense()
        elif choice == "3":
            query_records()
        elif choice == "4":
            calculate_statistics()
        elif choice == "5":
            set_budget()
        elif choice == "6":
            print("退出系统。")
            break
        else:
            print("无效选择，请重新输入！")
if __name__ == "__main__":
    main_menu()