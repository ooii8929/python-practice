class Event:
    def __init__(self, name: str = None, *event_types, **extra_info):
        self.name = name
        self.event_types = list(event_types)
        self.extra_info = extra_info

    def display_info(self):
        type_str = ", ".join(self.event_types)
        print(f"Event name is {self.name}, Types are {type_str}")

class Vod(Event):
  def __init__(self, Rate: str = None, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.Rate = Rate

  def display_info(self):
    super().display_info()
    for key, value in self.extra_info.items():
        print("{0} == {1}".format(key, value))
    print(f"Rate is {self.Rate}")

vod = Vod("G", "King Kong", "Love" , "Horror", author = "alvin")

vod.display_info()

#反向使用 
print("反向使用")

# 使用 *args 方式
args = ("fantasy", "historical")

# 使用 **kwargs 方式
kwargs = {"author": "abc", "publish_year": "2024"}

vod2 = Vod("G", "Inception", *args, **kwargs)

vod2.display_info()

