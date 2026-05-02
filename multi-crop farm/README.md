# Summary of code 

Multi-crop farm is a project where we can grow the following entities:

1. Grass
2. Bush
3. Tree
4. Carrot

The overall goal is to have the drone automating the harvesting without the user needing to stop and start up a new set of code to harvest a specific entity. The program will identify what items have been harvested and will plant the corresponding plants as needed if they are low in our inventory.

# Current plan for the logic
The following items is the current brainstorming/idea on how this program works:

- center drone at 0,0 
  - identify current inventory
  - how much hay do we have?
- make drone identify lowest item count from inventory to plant first
- harvest if item below is harvestable 
- identify ground type 
  - set to correct ground type for low item count
- plant that low item count

***Tree Setup***
Tree's are a bit interesting on how it's used and making sure that it's growing efficiently. Tree's require spacing from another tree that has been planted. The following is the current structure on how to program the planting process for tree's:

- have function to identify even and odd location 
  - use the % operator 
- set trees to only plant on even y block if x coord % 2 == 0, then same thing but plant on odd y block when x coord % 2 != 0
- IF the coordinate cannot allow for tree placement, but available to plant, then plant bush as last resort

