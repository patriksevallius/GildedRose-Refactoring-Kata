# -*- coding: utf-8 -*-


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __new__(cls, name, *args):
        if name == "Aged Brie":
            return super().__new__(BrieItem)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return super().__new__(BackstageItem)
        elif name == "Sulfuras, Hand of Ragnaros":
            return super().__new__(SulfurasItem)
        else:
            return super().__new__(cls)

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.decrement_quality()
        self.decrement_quality()

    def decrement_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality += 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class BrieItem(Item):
    def update_quality(self):
        self.sell_in -= 1
        self.increase_quality()
        if self.sell_in < 0:
            self.increase_quality()


class BackstageItem(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
        else:
            self.increase_quality()
            if self.sell_in < 10:
                self.increase_quality()
            if self.sell_in < 5:
                self.increase_quality()


class SulfurasItem(Item):
    def update_quality(self):
        pass
