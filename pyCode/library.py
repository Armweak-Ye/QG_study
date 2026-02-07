#  燃尽力，悲
class Library:
    _total_book = 0
    def __init__(self, name, number):
        self._name = name
        self._number = number
        Library._total_book += 1

class Book(Library):
    def __init__(self):
        self.book_shelf = []

    def judge_number(self, book_number):
        for book in self.book_shelf:
            if book._number == book_number:
                return True
            else:
                return False

    def add_book(self):
        while True:
            book_number = input("请输入书籍编号：")
            if self.judge_number(book_number):
                print("书籍编号已存在，请重新输入")
            else:
                book_name = input("请输入书籍名称：")
                book = Library(book_name, book_number)
                self.book_shelf.append(book)
                print("书籍添加成功")
            more = input("是否继续添加书籍？(y/n)：")
            if more.lower() == 'y':
                continue
            else:
                break

    def display_books(self):
        print("书籍列表：")
        for book in self.book_shelf:
            print(f"书籍名称：“{book._name}”，书籍编号：{book._number}\n")

    def set_book(self):
        while True:
            book_number = input("请输入要修改的书籍编号：")
            if self.judge_number(book_number):
                new_name = input("请输入新的书籍名称：")
                for book in self.book_shelf:
                    if book._number == book_number:
                        book._name = new_name
                        print("书籍信息修改成功")
            else:
                print("书籍编号不存在，无法修改")
            more = input("是否继续修改书籍？(y/n)：")
            if more.lower() == 'y':
                continue
            else:
                break

    def main(self):
        while True:
            print("欢迎使用图书管理系统")
            print("我们一共有{}本书籍".format(Library._total_book))
            print("添加书籍--->1")
            print("显示书籍--->2")
            print("修改书籍--->3")
            print("退出系统--->4")
            choice = input("请输入操作编号：")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.display_books()
            elif choice == '3':
                self.set_book()
            elif choice == '4':
                print("感谢使用图书管理系统，再见！")
                break
            else:
                print("输入有误，请重新输入")
if __name__ == "__main__":
    book_system = Book()
    book_system.main()