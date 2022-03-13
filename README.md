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
hopper
-chest
--plank
---log : 1232.0 = 19.25 stacks
-iron_ingot : 3080.0 = 48.12 stacks
------------------------------
chest
-plank
--log : 1056.0 = 16.5 stacks
------------------------------
barrel
-wood_slab
--plank
---log : 44.0 = 0.69 stacks
-plank
--log : 264.0 = 4.12 stacks
------------------------------
redstone_torch
-stick
--plank
---log : 11.0 = 0.17 stacks
-redstone_dust : 88.0 = 1.38 stacks
------------------------------
comparator
-redstone_torch
--stick
---plank
----log : 33.0 = 0.52 stacks
--redstone_dust : 264.0 = 4.12 stacks
-quartz : 88.0 = 1.38 stacks
-stone : 264.0 = 4.12 stacks
------------------------------
repeater
-redstone_torch
--stick
---plank
----log : 22.0 = 0.34 stacks
--redstone_dust : 176.0 = 2.75 stacks
-stone : 264.0 = 4.12 stacks
-redstone_dust : 88.0 = 1.38 stacks
------------------------------
redstone_dust
-redstone_dust : 30976.0 = 484.0 stacks
------------------------------

Final Costs
log : 2662.0 = 41.59 stacks
iron_ingot : 3080.0 = 48.12 stacks
redstone_dust : 792.0 = 12.38 stacks
quartz : 88.0 = 1.38 stacks
stone : 528.0 = 8.25 stacks
```
