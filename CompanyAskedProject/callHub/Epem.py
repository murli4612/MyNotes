# class TVChannelSwitcher:
#     """
#     implement everything to get this code work and pass all assertions
#     """
#     channels =[]
#     def __init__(self, channel):
#         for ch in channel:
#             # print(ch)
#             self.channels.append(ch)
#     def add_channel(self, ch):
#         self.channels.append(ch)
#         return self
#     def remove_channel(self,channel):
#         if channel in self.channels:
#             self.channels.remove(channel)
#         return self
class TVChannelSwitcher:
    """
    A tiny fluent API for managing a personal TV‑channel list.
    
    • Each instance keeps its *own* list (no accidental sharing).
    • The public `channels` attribute is exposed as a *copy* so external
      code can read it, but cannot mutate the internal state.
    • `add_channel` / `remove_channel` return self to allow chaining.
    """
    # nothing shared at the class level – every switcher has its own list
    def __init__(self, channels):
        # make our own copy in case the caller re‑uses the same list elsewhere
        self._channels: list[str] = list(channels)
        print("murli")

    # read‑only property that hands back a shallow copy
    @property
    def channels(self) -> list[str]:
        return self._channels.copy()

    # fluent helpers ---------------------------------------------------------
    def add_channel(self, ch: str) -> "TVChannelSwitcher":
        if ch not in self._channels:
            self._channels.append(ch)
        return self

    def remove_channel(self, ch: str) -> "TVChannelSwitcher":
        if ch in self._channels:
            self._channels.remove(ch)
        return self
           
 
# ----------- you may only comment and uncomment next lines lines 
DEFAULT_CHANNELS_LIST = ["Fox news", "BBC News"]
 
parents = TVChannelSwitcher(DEFAULT_CHANNELS_LIST)
parents.add_channel("Action movies").add_channel("National geographics").add_channel("Discovery")
# you may uncomment if in one line doesnt work
# parents.add_channel("Action movies")
# parents.add_channel("National geographics")
# parents.add_channel("Discovery")
print(parents.channels)
 
kidstv = TVChannelSwitcher(DEFAULT_CHANNELS_LIST)
kidstv.add_channel("Disney cartoons").remove_channel("Fox news").add_channel("Nikelodeon")
# you may uncomment if in one line doesnt work
# kidstv.add_channel("Disney cartoons")
# kidstv.remove_channel("Fox news")
# kidstv.add_channel("Nikelodeon")

print(kidstv.channels)
 
assert "Fox news" in parents.channels
assert "BBC News" in parents.channels
assert "Action movies" in parents.channels
assert "National geographics" in parents.channels
assert "Discovery" in parents.channels
 
assert "Qwerty" not in parents.channels
assert "Disney cartoons" not in parents.channels
 
assert "Nikelodeon" in kidstv.channels
assert "BBC News" in kidstv.channels
assert "Disney cartoons" in kidstv.channels
 
assert "Fox news" not in kidstv.channels
assert "Adult movies" not in kidstv.channels
 
# attribute `channels` is list of string
kidstv.channels.append("Test") # in this line I try to brake incapsulation principles (no Exception.)
assert "Test" not in kidstv.channels # but our property is readonly and `Test` channel is not added.

Write a query to fetch the first and last name of employee with second highest salary in location Bangalore.

Schema
========

Employee Table
--------------
ID - primary key
First_Name
Last_Name
Branch_ID - foreign key

Salary Table
------------
EMP_ID - foreign key
Salary

Branch Table
------------
Branch_ID - primary key
Branch_Location

# select e.First_name, e.Last_name 
# from Employee as e
# join salary as s on s.EMP_ID = e.ID
# JOIN branch as b on b.Branch_ID = e.Branch_id
# where b.branch_location = 'Bangalore'
# And s.salary = (
    
#     select Max()
# )