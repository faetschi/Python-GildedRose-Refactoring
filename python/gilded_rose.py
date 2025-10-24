# -*- coding: utf-8 -*

class GildedRose(object):

    def __init__(self, items):
        # Import the factory
        from item_updater import create_item_updater
        # Instead of storing the raw items, 
        # store new "UpdatableItem" wrappers
        self.items = [create_item_updater(item) for item in items]

    def update_quality(self):
            # Tell, Don't Ask
            for item in self.items:
                item.update()


class Item:
    """
    This class must not be changed as per the requirements
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
