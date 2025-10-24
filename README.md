# Gilded Rose Refactoring Kata - My Solution

This repository contains my refactored solution for the Python version of the Gilded Rose Refactoring Kata.

The goal was to refactor the original code according to **SOLID**, **Clean Code (KISS, Tell-Don't-Ask)**, and **Domain-Driven Design (DDD)** and other conventional software engineering principles.

The refactoring process was done incrementally:
1.  A "Golden Master" test was established to create a safety net.
2.  A new domain model was built using the Template Method and Factory patterns (`item_updater.py`).
3.  The original `GildedRose` class was refactored to use the new domain model, following the "Tell, Don't Ask" principle.
4.  The new "Conjured" item feature was added, demonstrating the extensibility of the new design (OCP).
5.  Unit tests were added to confirm the new, isolated domain classes are easily testable.