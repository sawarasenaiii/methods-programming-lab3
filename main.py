"""Классы и паттерны для лабораторной работы №3."""

from __future__ import annotations


class Book:
    """Книга с названием и автором."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} — {self.author}"
