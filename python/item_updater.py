# -*- coding: utf-8 -*-
from gilded_rose import Item

# --- Constants for Magic Strings ---
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"


# --- Base Class ---
class UpdatableItem:
    """
    This is our base class (Template Method) from Step 2.
    It handles "Normal Items" by default.
    """
    def __init__(self, item: Item):
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
        decrease = 2 if self.item.sell_in < 0 else 1
        self._decrease_quality(decrease)

    def _constrain_quality_limits(self):
        """Default: Quality is between 0 and 50."""
        if self.item.quality < 0:
            self.item.quality = 0
        if self.item.quality > 50:
            self.item.quality = 50

    # --- Helper methods for subclasses ---
    def _increase_quality(self, amount: int = 1):
        """Increases quality, respecting the 50 limit."""
        if self.item.quality < 50:
            self.item.quality += amount

    def _decrease_quality(self, amount: int = 1):
        """Decreases quality, respecting the 0 limit."""
        if self.item.quality > 0:
            self.item.quality -= amount


# --- Specialized Subclasses ---
# Each class is responsible for ONE item type logic.

class AgedBrieUpdater(UpdatableItem):
    """Handles the logic for "Aged Brie"."""
    def _update_quality(self):
        # Quality increases, twice as fast after sell_in
        increase = 2 if self.item.sell_in < 0 else 1
        self._increase_quality(increase)

class SulfurasUpdater(UpdatableItem):
    """Handles the logic for "Sulfuras"."""
    def _update_sell_in(self):
        """Sulfuras never has to be sold."""
        pass # Do nothing

    def _update_quality(self):
        """Sulfuras' quality never alters."""
        pass # Do nothing

    def _constrain_quality_limits(self):
        """Sulfuras' quality is always 80."""
        # We override the base 0-50 constraint
        pass # Do nothing

class BackstagePassUpdater(UpdatableItem):
    """Handles the logic for "Backstage passes"."""
    def _update_quality(self):
        if self.item.sell_in < 0:
            # After the concert, quality is 0
            self.item.quality = 0
        elif self.item.sell_in < 5:
            # 5 days or less: +3
            self._increase_quality(3)
        elif self.item.sell_in < 10:
            # 10 days or less: +2
            self._increase_quality(2)
        else:
            # More than 10 days: +1
            self._increase_quality(1)

    def _constrain_quality_limits(self):
        """
        Special constraint: Can increase up to 50,
        but drops to 0 after concert (handled in _update_quality).
        """
        super()._constrain_quality_limits()
        # After update, quality could be > 50, so we cap it.
        if self.item.quality > 50:
            self.item.quality = 50

class ConjuredUpdater(UpdatableItem):
    """Handles the logic for "Conjured" items.
    
    For refactoring, this must match the
    original Golden Master, which treated "Conjured"
    like a normal item.
    """
    pass # Inherits the "Normal Item" behavior from UpdatableItem

    # example actual implementation
    # def _update_quality(self):
    #     # "degrade in Quality twice as fast as normal items"
    #     decrease = 4 if self.item.sell_in < 0 else 2
    #     self._decrease_quality(decrease)


# --- Factory ---
# This is the only place that maps strings (Item names)
# to Domain Objects (the Updater classes)

# 1. The registry of all specialized types
ITEM_UPDATERS = {
    AGED_BRIE: AgedBrieUpdater,
    BACKSTAGE_PASS: BackstagePassUpdater,
    SULFURAS: SulfurasUpdater,
    CONJURED: ConjuredUpdater
}

def create_item_updater(item: Item) -> UpdatableItem:
    """
    Factory function.
    It looks up the item's name in our registry.
    If it finds a special class, it returns that.
    If not, it returns the default `UpdatableItem` class.
    """
    # Get the specialized class, or default to UpdatableItem
    UpdaterClass = ITEM_UPDATERS.get(item.name, UpdatableItem)

    # Return an *instance* of that class, wrapping the item
    return UpdaterClass(item)