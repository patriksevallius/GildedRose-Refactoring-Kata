# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.update_brie_quality()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.update_backstage_quality()
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.update_sulfuras_quality()
            else:
                item.update_item_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_sulfuras_quality(self):
        pass

    def update_backstage_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
        else:
            if self.quality < 50:
                self.quality += 1
            if self.sell_in < 10 and self.quality < 50:
                self.quality += 1
            if self.sell_in < 5 and self.quality < 50:
                self.quality += 1

    def update_brie_quality(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1

    def update_item_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality -= 1
        if self.quality > 0:
            self.quality -= 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
