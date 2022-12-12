---
sidebar_label: 'Game-Engine'
sidebar_position: 1
---
import { Mermaid } from 'mdx-mermaid/Mermaid';



<Mermaid chart = 'classDiagram
class environment{
gridSize
nonPassableCount
truckAgentCount
goalCount
seed
root : Cell[]
percept: []
goal: []
trucks: []
cells : Cell[]
generateEnvironment()
makeCells()
check_if_open(Cell): bool
populateEnvWithSeed(trucks: int, goals: int, seed: int)
populateEnv(trucks: int, blocks: int, goals: int)
populateEnvPreBuilt()
get_cells_by_type(): []
toString()
truckHere()
}'
/>

Then Enviroment Class is used to create the Enviroment that our Agents use to find there goals. 

<Mermaid chart = 'classDiagram
class Action{
costN 
costS 
costE
costW 
northF 
westF
eastF 
southF 
north 
west 
east 
south 
getCost(action)
}'
/>

Action is a file that holds all the costs per each action. The getcost method gets the cost of a action. 

<Mermaid chart = 'classDiagram
class Cell{
x
y
direction
truck
cell_type
percepts : Percept
location : Location
found
toString()
setType(cellType)
set_found(bool)
get_found()
}'
/>

The Cell class is filling each grid slot and holding data refrading to that cell. It stores the x,y values for its posistion in the grid.
Truck and direction to hold the truck thats in the cell and what direction its facing. cell_type to see what type of cell(Truck, Goal, Open, Blocked).
found for whether or not the goal has been found in this cell. Percept for the cell to see whats around it. 

<Mermaid chart = 'classDiagram
class Percept{
north
east
south
west
toString()
}'
/>

The Percept class is the percept that each cell will use to see what is around it. 

<Mermaid chart = 'classDiagram
class seed_generator{
generate_truck_locations(trucks: int, width: int, height: int): dict
generate_goal_locations(goals: int, width: int, height: int): dict
generateWhiteNoise(width: int,height: int, seed: int, trucks: int, goals: int): [], Cell[]
}'
/>

The seed_generator will generate a specific seed for the infermation passed in, and will create the same seed if the same information is passed in. Essentually
hasing the data to produce the same seed every time. 

<Mermaid chart = 'classDiagram
class TruckAgent{
x
y
direction
percept
movable
toString()
updateLocation(location)
}'
/>

TruckAgent is the Agent that will be moving around the grid. Holds its x,y location, direction facing, percepts around it. 



 