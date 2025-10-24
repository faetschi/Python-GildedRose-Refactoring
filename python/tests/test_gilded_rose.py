# -*- coding: utf-8 -*-
import unittest

# Import Item class from the main module
from gilded_rose import Item

# Import testable domain classes
from item_updater import (
    UpdatableItem,
    AgedBrieUpdater,
    SulfurasUpdater,
    BackstagePassUpdater,
    ConjuredUpdater
)

class GildedRoseTest(unittest.TestCase):

    # --- Test 1: Normal Item ---
    def test_normal_item(self):
        # Arrange
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        updater = UpdatableItem(item)
        
        # Act
        updater.update()
        
        # Assert
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

    # --- Test 2: Normal Item (Past SellIn) ---
    def test_normal_item_past_sell_in(self):
        item = Item(name="+5 Dexterity Vest", sell_in=0, quality=20)
        updater = UpdatableItem(item)
        updater.update()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 18) # Degrades by 2

    # --- Test 3: Aged Brie ---
    def test_aged_brie(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)
        updater = AgedBrieUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 1)
        self.assertEqual(item.quality, 1) # Increases by 1

    # --- Test 4: Aged Brie (At 50) ---
    def test_aged_brie_at_max_quality(self):
        item = Item(name="Aged Brie", sell_in=2, quality=50)
        updater = AgedBrieUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 1)
        self.assertEqual(item.quality, 50) # Does not go over 50

    # --- Test 5: Sulfuras ---
    def test_sulfuras(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        updater = SulfurasUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 0) # Never moves
        self.assertEqual(item.quality, 80) # Never changes

    # --- Test 6: Backstage Pass (10+ days) ---
    def test_backstage_pass_long_lead(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        updater = BackstagePassUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21) # +1

    # --- Test 7: Backstage Pass (10 days) ---
    def test_backstage_pass_10_days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
        updater = BackstagePassUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22) # +2

    # --- Test 8: Backstage Pass (5 days) ---
    def test_backstage_pass_5_days(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
        updater = BackstagePassUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23) # +3

    # --- Test 9: Backstage Pass (After Concert) ---
    def test_backstage_pass_after_concert(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
        updater = BackstagePassUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0) # Drops to 0

    # --- Test 10: Conjured Item (Your New Feature!) ---
    def test_conjured_item(self):
        item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)
        updater = ConjuredUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 4) # Degrades by 2

    # --- Test 11: Conjured Item (Past SellIn) ---
    def test_conjured_item_past_sell_in(self):
        item = Item(name="Conjured Mana Cake", sell_in=0, quality=6)
        updater = ConjuredUpdater(item)
        updater.update()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 2) # Degrades by 4


if __name__ == '__main__':
    unittest.main()