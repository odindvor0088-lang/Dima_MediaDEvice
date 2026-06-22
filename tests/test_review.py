from src.review.review import Review
import pytest


class TestReview:
    def setup_method(self):
        self.u = Review(
            title="Обзор Honor 7A",
            content="Хороший бюджетный смартфон",
            author="Дима",
        )

    def test_create_review(self):
        assert self.u.author == "Дима"
        assert self.u.content == "Хороший бюджетный смартфон"
        assert self.u.title == "Обзор Honor 7A"

    def test_add_pro_and_con(self):
        self.u.add_pro("Хорошая цена")
        self.u.add_con("Слабая камера")

        assert self.u.pros == ["Хорошая цена"]
        assert self.u.cons == ["Слабая камера"]


    def test_remove_pro_and_con(self):
        self.u.add_pro("Хорошая цена")
        self.u.add_con("Слабая камера")

        self.u.remove_pro(0)
        self.u.remove_con(0)

        assert self.u.pros == []
        assert self.u.cons == []



