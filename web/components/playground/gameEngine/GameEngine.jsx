import {React, useState} from 'react';
import Grid from "./Grid"
import InputFields from "./InputFields"
import axios from 'axios'

export default function GameEngine({ activeTab, setActiveTab, oldID, setOldID, setData, reset, loadOld, data }){

    let longestPath = data.stats.longestPath
    const [grid, setGrid] = useState(data.grid)
    const [agents, setAgents] = useState(data.agents)

    // console.log(data)

    const [loading, setLoading] = useState(false)

    function updateGrid(x, y, status){
        let newGrid = grid
        newGrid[x][y] = status
        setGrid([...newGrid])
    }

    function moveAgent(position, status, iter){
        let x = position.x;
        let y = position.y;
        switch(status){
            case "a-u":
                updateGrid(x, y, "p-u")
                agents[iter].position.x -= 1;
                x -= 1;
                updateGrid(x, y, "a-u")
                break;
            case "a-r":
                updateGrid(x, y, "p-r")
                agents[iter].position.y += 1;
                y += 1;
                updateGrid(x, y, "a-r")
                break;
            case "a-d":
                updateGrid(x, y, "p-d")
                agents[iter].position.x += 1;
                x += 1
                updateGrid(x, y, "a-d")
                break;
            case "a-l":
                updateGrid(x, y, "p-l")
                agents[iter].position.y -= 1;
                y -= 1
                updateGrid(x, y, "a-l")
                break;
        }
    }

    function turnAgent(position, status, turn, iter){
        let x = position.x;
        let y = position.y;

        switch(status){
            case "a-u":
                if(turn == "l"){
                    updateGrid(x, y, "a-l")
                    agents[iter].status = "a-l"
                }else{
                    updateGrid(x, y, "a-r")
                    agents[iter].status = "a-r"
                }
                break;
            case "a-r":
                if(turn == "l"){
                    updateGrid(x, y, "a-u")
                    agents[iter].status = "a-u"
                }else{
                    updateGrid(x, y, "a-d")
                    agents[iter].status = "a-d"
                }
                break;
            case "a-d":
                if(turn == "l"){
                    updateGrid(x, y, "a-r")
                    agents[iter].status = "a-r"
                }else{
                    updateGrid(x, y, "a-l")
                    agents[iter].status = "a-l"
                }
                break;
            case "a-l":
                if(turn == "l"){
                    updateGrid(x, y, "a-d")
                    agents[iter].status = "a-d"
                }else{
                    updateGrid(x, y, "a-u")
                    agents[iter].status = "a-u"
                }
                break;
        }
    }

    const fetchData = () => {
        setLoading(true)
        axios.post('http://127.0.0.1:5000/search', {
            "trucks": 3,
            "seed": "joe",
            "goals": 4,
            "gridsize": 10,
            "search": "Breadth First Search"
        })
        .then(function (response) {
            // console.log(response)
            setData(response.data)
            // setAgents(response.data.agents)
            // setGrid(response.data.grid)
            // console.log(response.data.agents)
            setLoading(false)
            runAgents()
        })
    }

    async function runAgents(){
        for(let i = 0; i < longestPath; i++){
            for(let j = 0; j < data.agents.length; j++){
                run(data.agents[j], data.agents[j].sequence[i], j)
            }
            await new Promise(r => setTimeout(r, 1000));
        }
    }

    function run(agent, cmd, iter){
        if(cmd == 'm'){
            moveAgent(agent.position, agent.status, iter)
        } else{
            turnAgent(agent.position, agent.status, cmd, iter)
        }
    }

    if(loading){
        return <div>Loading...</div>
    }

    return(
        <div className="flex justify-center gap-10">
            <InputFields activeTab={activeTab} setActiveTab={setActiveTab} oldID={oldID} setOldID={setOldID} reset={reset} loadOld={loadOld} test={fetchData}/>
            <Grid grid={grid}/>
        </div>
    )
}