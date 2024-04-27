import json
import os
from AdrBookExceptions import *


class TerminalAdrBook:
    def __init__(self):
        with open('ardBook.json', 'r') as data:
            if os.stat("ardBook.json").st_size != 0:
                self.book = json.load(data)
            else:
                self.book = {}

    def __save_book(self):
        with open('ardBook.json', 'w+') as file:
            json.dump(self.book, file, indent=4)

    def __add_number(self, data: list):
        data[1] = data[1].strip()

        self.book[data[1]] = {}
        self.book[data[1]]['number'] = data[0].strip()

        self.__save_book()

    def __verify_and_split_data(self, data: str) -> list:
        if '-' in data and data.count('-') == 1:
            data = data.split('-')
        else:
            self.__save_book()
            raise ABInputError()

        if len(data) != 2:
            self.__save_book()
            raise ABInputError()

        return data

    def __append_number_to_adrbook(self, data: list = None, n: int = 1) -> None:
        if data is None:
            print('Enter {number - Family Name Surname} or exit')
            for i in range(n):
                data = input('-> ')

                if data == 'exit':
                    self.__save_book()
                    break

                self.__add_number(
                    self.__verify_and_split_data(data)
                )

        else:
            self.__add_number(data)

    def __delete_number_from_adrbook(self, key: str) -> None:
        if key in self.book:
            del self.book[key]
            self.__save_book()
        else:
            print("Number not found to delete")

    def __print_all_numbers(self):
        max_len = max([len(key) for key in self.book.keys()])
        for number in sorted(self.book, key=lambda x: x):
            print(f"{number:<{max_len+5}} \t {self.book[number]['number']}")

    def find_number_in_book(self, name: str):
        if name in self.book:
            print(f"{name} \t {self.book[name]['number']}")
            return self.book[name]
        else:
            print("Name not found")


    def __select_command(self) -> None:
        while True:
            try:
                guess = input('c -> ').lower()

                if guess.strip() == 'exit':
                    return

                if len(guess.split('append')) == 0 \
                        or guess.count('append') == 1 \
                        and len(guess.split()) <= 2:

                    if len(guess.split('append')) == 2\
                            and all(i.isdigit() for i in guess.split('append')[1].strip()):
                        self.__append_number_to_adrbook(n=int(guess.split()[1]))
                    else:
                        self.__append_number_to_adrbook(self.__verify_and_split_data(guess.split('append')[1]))

                elif len(guess.split('del')) == 0 \
                        or guess.count('del') == 1:

                    self.__delete_number_from_adrbook(guess.split("del")[1].strip())

                elif len(guess.split('print')) == 0 \
                        or guess.count('print') == 1:
                    self.__print_all_numbers()

                elif 'find' in guess and \
                        len(guess.split('find')) == 1 \
                        or guess.count('find') == 1 \
                        and len(guess.split('find')) > 1:

                    self.find_number_in_book(guess.split("find")[1].strip())

                else:
                    print('You enter invalid command')

            except ABInputError as abi:
                print(abi)

    def start(self):
        print(
            'Hello!',
            'Enter print to print all your numbers',
            'Enter append n to append n numbers (n=1)',
            'Enter del {some number} to delete number',
            'Enter find {some name} to find number',
            'Enter exit to exit',
            sep='\n'
        )
        self.__select_command()
