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

<Mermaid chart = 'classDiagram
class Percept{
north
east
south
west
toString()
}'
/>
<Mermaid chart = 'classDiagram
class seed_generator{
generate_truck_locations(trucks: int, width: int, height: int): dict
generate_goal_locations(goals: int, width: int, height: int): dict
generateWhiteNoise(width: int,height: int, seed: int, trucks: int, goals: int): [], Cell[]
}'
/>
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



 