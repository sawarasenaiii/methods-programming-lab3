"""Классы и паттерны для лабораторной работы №3."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


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


class TextFile:
    """Небольшая безопасная обёртка над текстовым файлом UTF-8."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def write(self, text: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(text, encoding="utf-8")

    def read(self) -> str:
        return self.path.read_text(encoding="utf-8")

    def append(self, text: str) -> None:
        with self.path.open("a", encoding="utf-8") as file:
            file.write(text)


class Shape(ABC):
    """Абстрактная фигура (повышенное задание №9)."""

    @abstractmethod
    def area(self) -> float:
        """Вернуть площадь фигуры."""


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Стороны должны быть положительными")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return 3.141592653589793 * self.radius**2
