class Review:
    """
      Класс для представления обзора
      Атрибуты:
          title (str): заголовок обзора
          content (str): текст обзора
          author (str): автор обзора
          date (str): дата создания обзора в формате
          pros (list): список плюсов
          cons (list): список минусов
      """
    def __init__(self, title, content, author = "Эксперт", date = None, pros = None, cons = None):
        self.__title = title
        self.__content = content
        self.__author = author
        self.__date = date
        self.__pros = pros.copy() if pros is not None else []
        self.__cons = pros.copy() if cons is not None else []



    @property
    def title(self) -> str:
        """Геттер для заголовка. Возвращает текущий заголовок обзора."""
        return self.__title


    @title.setter
    def title(self, value: str) -> None:
        """Сеттер для заголовка. Принимает новый заголовок, проверяет его на то, чтобы он был строкой.
               И выводит сообщение если заголовок неправильный.
               """
        if isinstance(value, str):
            self.__title = value
            print(f'Заголовок вашего обзора: {self.__title}')
        else:
            print(f'Заголовок не может быть написан числами!')



    @property
    def content(self) -> str:
        """Геттер для содержания. Возвращает текст обзора."""
        return self.__content


    @content.setter
    def content(self, value: str) -> None:
        """ Сеттер для содержания. Принимает новый текст обзора и проверяет его с помощью isinstanse.
              И выводит сообщение если обзор неправильный.
              """
        if isinstance(value, str):
            self.__content = value
            print(f'Текст вашего обзора(Проверьте, всё ли вы правильно указали.): {self.__content}')
        else:
            print(f'Обзор не может состоять только из чисел!')



    @property
    def author(self) -> str:
        """Геттер для автора. Возвращает имя автора обзора."""
        return self.__author


    @author.setter
    def author(self, value: str) -> None:
        """ Сеттер для автора. Сохраняет имя автора."""
        self.__author = value
        print(f'Другие пользователи будут видеть вас под ником: {self.__author}')



    @property
    def date(self) -> str:
        """Геттер для даты. Возвращает дату создания обзора."""
        return self.__date


    @date.setter
    def date(self, value: str) -> None:
        self.__date = value



    @property
    def pros(self) -> list:
        """ Геттер для списка плюсов. Возвращает КОПИЮ списка"""
        return self.__pros.copy()


    @pros.setter
    def pros(self, list_pros: list) -> None:
        """Сохраняется копия списка для инкапсуляции."""
        self.pros = list_pros[:]



    @property
    def cons(self) -> list:
        """Сохраняется копия списка для инкапсуляции."""
        return self.__cons.copy()


    @cons.setter
    def cons(self, list_cons: list) -> None:
        """Сохраняется копия списка для инкапсуляции."""
        self.__cons = list_cons[:]



    def add_pro(self, pro_text: str) -> None:
        """Добавляет новый плюс в список."""
        if len(pro_text) > 200:
            print(f'Текст плюса слишком длинный')
        else:
            self.__pros.append(pro_text)
            print(f'Ваш плюс добавлен✅')



    def add_con(self, con_text: str) -> None:
        """Добавляет новый минус в список."""
        if len(con_text) > 200:
            print(f'Текст минуса слишком длинный')
        else:
            self.__cons.append(con_text)
            print(f'Ваш минус добавлен✅')



    def remove_pro(self, index: int) -> None:
        """Удаляет плюс по индексу."""
        if 0 <= index < len(self.__pros):
            removed = self.__pros.pop(index)
            print(f"Плюс '{removed}' удалён")
        else:
            print(f'Индекс {index} вне диапазона')



    def remove_con(self, index: int) -> None:
        """Удаляет минус по индексу."""
        if 0 <= index < len(self.__cons):
            removed = self.__cons.pop(index)
            print(f"Минус '{removed}' удалён")
        else:
            print(f'Индекс {index} вне диапазона')



if __name__ == "__main__":
    # 1. ТЕСТ СОЗДАНИЯ ОБЗОРА
    phone_review = Review(
        title="Samsung Galaxy S24 Ultra",
        content="Флагманский телефон с отличной камерой и производительностью",
        author="ТехноБлогер",
        date="2025-02-23",
        pros=None,
        cons=None
    )

    # 2. ТЕСТ ГЕТТЕРОВ (ЧТЕНИЕ)
    print(f"{phone_review.title}")
    print(f"{phone_review.content}")
    print(f"{phone_review.author}")
    print(f"{phone_review.date}")
    print(f"{phone_review.pros}")
    print(f"{phone_review.cons}")

    # 3. ТЕСТ СЕТТЕРОВ (ИЗМЕНЕНИЕ)
    print("\n3. ПРОВЕРКА СЕТТЕРОВ:")
    phone_review.title = "iPhone 15 Pro Max"
    phone_review.content = "Обзор нового iPhone"
    phone_review.author = "AppleFan"
    phone_review.date = "2025-02-24"

    print(f"\nПосле изменений:")
    print(f"Заголовок: {phone_review.title}")
    print(f"Автор: {phone_review.author}")

    # 4. ТЕСТ ДОБАВЛЕНИЯ ПЛЮСОВ
    print("\n4. ДОБАВЛЕНИЕ ПЛЮСОВ:")
    phone_review.add_pro("Отличный экран")
    phone_review.add_pro("Быстрая зарядка")

    # Тест слишком длинного плюса
    long_text = "Очень длинный текст" * 50
    phone_review.add_pro(long_text)

    print(f"Плюсы сейчас: {phone_review.pros}")

    # 5. ТЕСТ ДОБАВЛЕНИЯ МИНУСОВ
    print("\n5. ДОБАВЛЕНИЕ МИНУСОВ:")
    phone_review.add_con("Дорогой")
    phone_review.add_con("Нет зарядки в комплекте")

    print(f"Минусы сейчас: {phone_review.cons}")

    # 6. ТЕСТ УДАЛЕНИЯ
    print("\n6. УДАЛЕНИЕ ПЛЮСА ПО ИНДЕКСУ:")
    print(f"Плюсы до удаления: {phone_review.pros}")
    phone_review.remove_pro(1)
    print(f"Плюсы после удаления: {phone_review.pros}")

    # Тест удаления с неверным индексом
    print("\nТест неверного индекса:")
    phone_review.remove_pro(10)
    phone_review.remove_pro(-5)




