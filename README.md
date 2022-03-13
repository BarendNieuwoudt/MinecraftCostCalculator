# MinecraftCostCalculator
Simple App, that tells you how much of each resource you need to collect, and what to craft it into, to end up with the exact amount of an item that you need

The recipes will need to be defined in json objects, I havent done this yet. 

But technically, this works.

Example: 
```
python costCalculator.py hopper:616,chest:528,barrel:176,redstone_torch:88,comparator:88,repeater:88,redstone_dust:176
```
Output:
```
hopper (616.0)
-chest (616.0)
--plank (4928.0)
---log : 1232.0 = 19.25 stacks
-iron_ingot : 3080.0 = 48.12 stacks
------------------------------
chest (528.0)
-plank (4224.0)
--log : 1056.0 = 16.5 stacks
------------------------------
barrel (176.0)
-wood_slab (352.0)
--plank (176.0)
---log : 44.0 = 0.69 stacks
-plank (1056.0)
--log : 264.0 = 4.12 stacks
------------------------------
redstone_torch (88.0)
-stick (88.0)
--plank (44.0)
---log : 11.0 = 0.17 stacks
-redstone_dust : 88.0 = 1.38 stacks
------------------------------
comparator (88.0)
-redstone_torch (264.0)
--stick (264.0)
---plank (132.0)
----log : 33.0 = 0.52 stacks
--redstone_dust : 264.0 = 4.12 stacks
-quartz : 88.0 = 1.38 stacks
-stone : 264.0 = 4.12 stacks
------------------------------
repeater (88.0)
-redstone_torch (176.0)
--stick (176.0)
---plank (88.0)
----log : 22.0 = 0.34 stacks
--redstone_dust : 176.0 = 2.75 stacks
-stone : 264.0 = 4.12 stacks
-redstone_dust : 88.0 = 1.38 stacks
------------------------------
redstone_dust (176.0)
-redstone_dust : 176.0 = 2.75 stacks
------------------------------

Final Costs
log : 2662.0 = 41.59 stacks
iron_ingot : 3080.0 = 48.12 stacks
redstone_dust : 792.0 = 12.38 stacks
quartz : 88.0 = 1.38 stacks
stone : 528.0 = 8.25 stacks
```
