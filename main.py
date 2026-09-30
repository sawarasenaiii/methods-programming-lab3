"""Классы и паттерны для лабораторной работы №3."""

from __future__ import annotations


class Book:
    """Книга с названием и автором."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    @staticmethod
    def is_valid_title(title: str) -> bool:
        """Проверить, что заголовок не пустой после удаления пробелов."""
        return bool(title.strip())

    def __str__(self) -> str:
        return f"{self.title} — {self.author}"
