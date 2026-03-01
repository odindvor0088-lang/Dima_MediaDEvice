from datetime import datetime


class Review:
    """
      Класс для представления обзора
      """
    def __init__(self, title: str, content: str, author: str = "Эксперт",
                 date: datetime = None, pros: list[str] = None, cons: list[str] = None) -> None:
        """
        Инициализация объекта Review.

            title: Заголовок обзора
            content: Текст обзора
            author: Автор обзора (по умолчанию "Эксперт")
            date: Дата создания
            pros: Список плюсов
            cons: Список минусов
        """
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now() if date is None else date
        self.pros = pros.copy() if pros is not None else []
        self.cons = cons.copy() if cons is not None else []

    @property
    def title(self) -> str:
        """Возвращает текущий заголовок обзора."""
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """
            Принимает новый заголовок, проверяет его на то, чтобы он был строкой.
            И выводит сообщение если заголовок неправильный.
        """
        if isinstance(value, str):
            self.__title = value
            print(f'Заголовок вашего обзора: {self.__title}')
        else:
            print(f'Заголовок не может быть написан числами!')

    @property
    def content(self) -> str:
        """Возвращает текст обзора."""
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        """
            Принимает новый текст обзора и проверяет его с помощью isinstanse.
            И выводит сообщение если обзор неправильный.
        """
        if isinstance(value, str):
            self.__content = value
            print(f'Текст вашего обзора(Проверьте, всё ли вы правильно указали.): {self.__content}')
        else:
            print(f'Обзор не может состоять только из чисел!')

    @property
    def author(self) -> str:
        """Возвращает имя автора обзора."""
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        """Сохраняет имя автора."""
        self.__author = value
        print(f'Другие пользователи будут видеть вас под ником: {self.__author}')

    @property
    def date(self) -> datetime:
        """Возвращает дату создания обзора."""
        return self.__date

    @date.setter
    def date(self, new_date: datetime) -> None:
        self.__date = new_date

    @property
    def pros(self) -> list[str]:
        """Возвращает КОПИЮ списка"""
        return self.__pros.copy()

    @pros.setter
    def pros(self, list_pros: list[str]) -> None:
        """Сохраняется копия списка для инкапсуляции."""
        self.__pros = list_pros.copy()

    @property
    def cons(self) -> list:
        """Сохраняется копия списка для инкапсуляции."""
        return self.__cons.copy()

    @cons.setter
    def cons(self, list_cons: list) -> None:
        """Сохраняется копия списка для инкапсуляции."""
        self.__cons = list_cons.copy()

    def add_pro(self, pro_text: str) -> None:
        """
        Добавляет новый плюс в список.
        :param pro_text: текст плюса
        """
        if len(pro_text) > 200:
            print(f'Текст плюса слишком длинный')
        else:
            self.__pros.append(pro_text)
            print(f'Ваш плюс добавлен✅')

    def add_con(self, con_text: str) -> None:
        """
        Добавляет новый минус в список.
        :param con_text: текст минуса
        """
        if len(con_text) > 200:
            print(f'Текст минуса слишком длинный')
        else:
            self.__cons.append(con_text)
            print(f'Ваш минус добавлен✅')

    def remove_pro(self, index: int) -> None:
        """Удаляет плюс по индексу."""
        if -len(self.__pros) <= index < len(self.__pros):
            removed = self.__pros.pop(index)
            print(f"Плюс '{removed}' удалён")
        else:
            print(f'Индекс {index} вне диапазона')

    def remove_con(self, index: int) -> None:
        """Удаляет минус по индексу."""
        if -len(self.__cons) <= index < len(self.__cons):
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




