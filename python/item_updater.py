# -*- coding: utf-8 -*-
from gilded_rose import Item

class UpdatableItem:
    """
    This class wraps the anemic 'Item' object and adds
    the domain logic for updating it. This is our rich domain object.

    This is the "Template Method" design pattern.
    The `update` method is the template, and subclasses
    can override any of the specific `_update_...` steps.

    This default implementation handles "Normal Items".
    """
    def __init__(self, item: Item):
        # We hold a *reference* to the original item.
        # Mutating self.item mutates the item in GildedRose.items
        # This respects the constraint "do not alter the Item class".
        self.item = item

    def update(self):
        """The main Template Method for updating an item."""
        self._update_sell_in()
        self._update_quality()
        self._constrain_quality_limits()

    def _update_sell_in(self):
        """Default: Sell_in decreases by 1."""
        self.item.sell_in -= 1

    def _update_quality(self):
        """Default: Quality decreases by 1, twice as fast after sell_in."""
        if self.item.quality > 0:
            # Quality decreases by 2 if past sell_in date, else by 1
            decrease = 2 if self.item.sell_in < 0 else 1
            self.item.quality -= decrease

    def _constrain_quality_limits(self):
        """Default: Quality is between 0 and 50."""
        # Quality is never negative
        if self.item.quality < 0:
            self.item.quality = 0

        # Quality is never more than 50
        if self.item.quality > 50:
            self.item.quality = 50