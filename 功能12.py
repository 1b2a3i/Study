# import datetime
#
# # 初始化存储收入、支出的列表
# incomes = []
# expenses = []
# budget = 0  # 用户预算
#
#
# def record_income():
#     date = input("请输入日期 (YYYY-MM-DD): ")
#     amount = float(input("请输入收入金额: "))
#     if amount <= 0:
#         print("收入金额必须为正数！")
#         return
#     category = input("请输入收入类别: ")
#     note = input("请输入备注: ")
#     incomes.append({"date": date, "amount": amount, "category": category, "note": note})
#     print("收入记录已添加！")
#
#
# def record_expense():
#     date = input("请输入日期 (YYYY-MM-DD): ")
#     amount = float(input("请输入支出金额: "))
#     if amount <= 0:
#         print("支出金额必须为正数！")
#         return
#     category = input("请输入支出类别: ")
#     note = input("请输入备注: ")
#     expenses.append({"date": date, "amount": amount, "category": category, "note": note})
#     print("支出记录已添加！")
#
#
# def query_records():
#     print("\n1. 查询收入记录")
#     print("2. 查询支出记录")
#     choice = input("请选择查询类型: ")
#     if choice == "1":
#         records = incomes
#         record_type = "收入"
#     elif choice == "2":
#         records = expenses
#         record_type = "支出"
#     else:
#         print("无效选择！")
#         return
#
#     print(f"\n所有{record_type}记录:")
#     for record in records:
#         print(f"日期: {record['date']}, 金额: {record['amount']}, 类别: {record['category']}, 备注: {record['note']}")
#
#
# def calculate_statistics():
#     total_income = sum(record['amount'] for record in incomes)
#     total_expense = sum(record['amount'] for record in expenses)
#     balance = total_income - total_expense
#     print(f"\n总收入: {total_income}")
#     print(f"总支出: {total_expense}")
#     print(f"当前余额: {balance}")
#
#     if budget > 0:
#         if total_expense > budget:
#             print("警告：您的支出已超出预算！")
#         else:
#             print(f"您的支出在预算范围内，剩余预算: {budget - total_expense}")
#
#
# def set_budget():
#     global budget
#     budget = float(input("请输入您的预算金额: "))
#     print("预算已设置！")
#
#
# def view_all_bills():
#     all_bills = incomes + expenses
#     if not all_bills:
#         print("没有账单记录！")
#         return
#
#     # 按日期排序
#     all_bills.sort(key=lambda x: x['date'])
#
#     print("\n所有账单记录:")
#     for bill in all_bills:
#         bill_type = "收入" if bill in incomes else "支出"
#         print(
#             f"类型: {bill_type}, 日期: {bill['date']}, 金额: {bill['amount']}, 类别: {bill['category']}, 备注: {bill['note']}")
#
#
# def search_bills():
#     print("\n1. 按日期查询")
#     print("2. 按类别查询")
#     choice = input("请选择查询方式: ")
#
#     if choice == "1":
#         date = input("请输入日期 (YYYY-MM-DD): ")
#         results = [bill for bill in incomes + expenses if bill['date'] == date]
#     elif choice == "2":
#         category = input("请输入类别: ")
#         results = [bill for bill in incomes + expenses if bill['category'] == category]
#     else:
#         print("无效选择！")
#         return
#
#     if not results:
#         print("未找到符合条件的账单记录！")
#         return
#
#     print("\n查询结果:")
#     for bill in results:
#         bill_type = "收入" if bill in incomes else "支出"
#         print(
#             f"类型: {bill_type}, 日期: {bill['date']}, 金额: {bill['amount']}, 类别: {bill['category']}, 备注: {bill['note']}")
#
#
# def main_menu():
#     while True:
#         print("\n个人账单管理系统")
#         print("1. 记录收入")
#         print("2. 记录支出")
#         print("3. 查询记录")
#         print("4. 统计")
#         print("5. 设置预算")
#         print("6. 查看所有账单")
#         print("7. 查询账单")
#         print("8. 退出")
#         choice = input("请选择操作: ")
#
#         if choice == "1":
#             record_income()
#         elif choice == "2":
#             record_expense()
#         elif choice == "3":
#             query_records()
#         elif choice == "4":
#             calculate_statistics()
#         elif choice == "5":
#             set_budget()
#         elif choice == "6":
#             view_all_bills()
#         elif choice == "7":
#             search_bills()
#         elif choice == "8":
#             print("退出系统。")
#             break
#         else:
#             print("无效选择，请重新输入！")
#
#
# if __name__ == "__main__":
#     main_menu()

import sys
from datetime import datetime

# 全局变量
incomes = []
expenses = []
monthly_budget = 0


def record_income():
    print("请输入收入信息：")
    date = input("日期（YYYY-MM-DD）：")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("错误：日期格式不正确，请输入YYYY-MM-DD格式的日期。")
        return

    amount = input("金额：")
    try:
        amount = float(amount)
        if amount <= 0:
            print("错误：收入金额必须为正数。")
            return
    except ValueError:
        print("错误：金额必须为数字。")
        return

    category = input("类别（如工资、奖金等）：")
    note = input("备注：")

    incomes.append({
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    })
    print("收入已成功记录！")


def record_expense():
    print("请输入支出信息：")
    date = input("日期（YYYY-MM-DD）：")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("错误：日期格式不正确，请输入YYYY-MM-DD格式的日期。")
        return

    amount = input("金额：")
    try:
        amount = float(amount)
        if amount <= 0:
            print("错误：支出金额必须为正数。")
            return
    except ValueError:
        print("错误：金额必须为数字。")
        return

    category = input("类别（如餐饮、交通、购物等）：")
    note = input("备注：")

    expenses.append({
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    })
    print("支出已成功记录！")


def show_all_bills():
    print("收入记录：")
    for income in incomes:
        print(f"日期: {income['date']}, 金额: {income['amount']}, 类别: {income['category']}, 备注: {income['note']}")

    print("\n支出记录：")
    for expense in expenses:
        print(
            f"日期: {expense['date']}, 金额: {expense['amount']}, 类别: {expense['category']}, 备注: {expense['note']}")


def query_bills():
    print("请选择查询方式：")
    print("1. 按日期查询")
    print("2. 按日期范围查询")
    print("3. 按类别查询")
    choice = input("请输入选项序号：")

    if choice == "1":
        date = input("请输入日期（YYYY-MM-DD）：")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("错误：日期格式不正确，请输入YYYY-MM-DD格式的日期。")
            return

        print("收入记录：")
        for income in incomes:
            if income["date"] == date:
                print(
                    f"日期: {income['date']}, 金额: {income['amount']}, 类别: {income['category']}, 备注: {income['note']}")

        print("\n支出记录：")
        for expense in expenses:
            if expense["date"] == date:
                print(
                    f"日期: {expense['date']}, 金额: {expense['amount']}, 类别: {expense['category']}, 备注: {expense['note']}")

    elif choice == "2":
        start_date = input("请输入开始日期（YYYY-MM-DD）：")
        end_date = input("请输入结束日期（YYYY-MM-DD）：")
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("错误：日期格式不正确，请输入YYYY-MM-DD格式的日期。")
            return

        print("收入记录：")
        for income in incomes:
            if start_date <= income["date"] <= end_date:
                print(
                    f"日期: {income['date']}, 金额: {income['amount']}, 类别: {income['category']}, 备注: {income['note']}")

        print("\n支出记录：")
        for expense in expenses:
            if start_date <= expense["date"] <= end_date:
                print(
                    f"日期: {expense['date']}, 金额: {expense['amount']}, 类别: {expense['category']}, 备注: {expense['note']}")

    elif choice == "3":
        category = input("请输入类别：")

        print("收入记录：")
        for income in incomes:
            if income["category"] == category:
                print(
                    f"日期: {income['date']}, 金额: {income['amount']}, 类别: {income['category']}, 备注: {income['note']}")

        print("\n支出记录：")
        for expense in expenses:
            if expense["category"] == category:
                print(
                    f"日期: {expense['date']}, 金额: {expense['amount']}, 类别: {expense['category']}, 备注: {expense['note']}")

    else:
        print("错误：无效的选项序号。")


def set_monthly_budget():
    global monthly_budget
    budget = input("请输入月度预算：")
    try:
        monthly_budget = float(budget)
        if monthly_budget <= 0:
            print("错误：预算金额必须为正数。")
            return
    except ValueError:
        print("错误：金额必须为数字。")
        return
    print("月度预算已成功设置！")


def show_monthly_statistics():
    month = input("请输入月份（YYYY-MM）：")
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("错误：月份格式不正确，请输入YYYY-MM格式的月份。")
        return

    total_income = sum(income["amount"] for income in incomes if income["date"].startswith(month))
    total_expense = sum(expense["amount"] for expense in expenses if expense["date"].startswith(month))

    print(f"{month} 月度统计：")
    print(f"总收入: {total_income}")
    print(f"总支出: {total_expense}")
    print(f"剩余预算: {monthly_budget - total_expense}")

    print("\n收入类别统计：")
    income_categories = {}
    for income in incomes:
        if income["date"].startswith(month):
            if income["category"] in income_categories:
                income_categories[income["category"]] += income["amount"]
            else:
                income_categories[income["category"]] = income["amount"]
    for category, amount in income_categories.items():
        print(f"{category}: {amount}")

    print("\n支出类别统计：")
    expense_categories = {}
    for expense in expenses:
        if expense["date"].startswith(month):
            if expense["category"] in expense_categories:
                expense_categories[expense["category"]] += expense["amount"]
            else:
                expense_categories[expense["category"]] = expense["amount"]
    for category, amount in expense_categories.items():
        print(f"{category}: {amount}")


def main_menu():
    while True:
        print("=================================")
        print("欢迎使用个人账单管理系统")
        print("=================================")
        print("请选择操作：")
        print("1. 记录收入")
        print("2. 记录支出")
        print("3. 查看所有账单")
        print("4. 查询账单")
        print("5. 设置月度预算")
        print("6. 查看月度统计报告")
        print("7. 退出系统")

        choice = input("请输入选项序号：")

        if choice == "1":
            record_income()
        elif choice == "2":
            record_expense()
        elif choice == "3":
            show_all_bills()
        elif choice == "4":
            query_bills()
        elif choice == "5":
            set_monthly_budget()
        elif choice == "6":
            show_monthly_statistics()
        elif choice == "7":
            print("感谢使用个人账单管理系统，再见！")
            sys.exit()
        else:
            print("错误：无效的选项序号。")

        input("\n按任意键返回主菜单...")


if __name__ == "__main__":
    main_menu()