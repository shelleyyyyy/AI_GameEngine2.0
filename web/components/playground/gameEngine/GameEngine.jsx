import {React, useState, useEffect} from 'react';
import Grid from "./Grid"
import InputFields from "./InputFields"
import axios from 'axios'
import PocketBase from 'pocketbase'

export default function GameEngine({ setSavedData, activeTab, setActiveTab, setData, reset, data }){

    const [loading, setLoading] = useState(false)
    // const [grid, setGrid] = useState(data.grid)

    function nestedCopy(array) {
        return JSON.parse(JSON.stringify(array));
    }

    function updateGrid(x, y, status, passed){
        console.log("RUNNING RUNNING RUNNING")
        let newData = passed
        newData.grid[x][y] = status
        setData(nestedCopy(newData))
    }

    function moveAgent(agents, position, status, iter, passed){
        let x = position.x;
        let y = position.y;
        switch(status){
            case "a-u":
                updateGrid(x, y, "p-u", passed)
                agents[iter].position.x -= 1;
                x -= 1;
                updateGrid(x, y, "a-u", passed)
                break;
            case "a-r":
                updateGrid(x, y, "p-r", passed)
                agents[iter].position.y += 1;
                y += 1;
                updateGrid(x, y, "a-r", passed)
                break;
            case "a-d":
                updateGrid(x, y, "p-d", passed)
                agents[iter].position.x += 1;
                x += 1
                updateGrid(x, y, "a-d", passed)
                break;
            case "a-l":
                updateGrid(x, y, "p-l", passed)
                agents[iter].position.y -= 1;
                y -= 1
                updateGrid(x, y, "a-l", passed)
                break;
        }
    }

    function turnAgent(agents, position, status, turn, iter, passed){
        let x = position.x;
        let y = position.y;

        switch(status){
            case "a-u":
                if(turn == "l"){
                    updateGrid(x, y, "a-l", passed)
                    agents[iter].status = "a-l"
                }else{
                    updateGrid(x, y, "a-r", passed)
                    agents[iter].status = "a-r"
                }
                break;
            case "a-r":
                if(turn == "l"){
                    updateGrid(x, y, "a-u", passed)
                    agents[iter].status = "a-u"
                }else{
                    updateGrid(x, y, "a-d", passed)
                    agents[iter].status = "a-d"
                }
                break;
            case "a-d":
                if(turn == "l"){
                    updateGrid(x, y, "a-r", passed)
                    agents[iter].status = "a-r"
                }else{
                    updateGrid(x, y, "a-l", passed)
                    agents[iter].status = "a-l"
                }
                break;
            case "a-l":
                if(turn == "l"){
                    updateGrid(x, y, "a-d", passed)
                    agents[iter].status = "a-d"
                }else{
                    updateGrid(x, y, "a-u", passed)
                    agents[iter].status = "a-u"
                }
                break;
        }
    }

    function run(agents, agent, cmd, iter, passed){
        if(cmd == 'm'){
            moveAgent(agents, agent.position, agent.status, iter, passed)
        } else{
            turnAgent(agents, agent.position, agent.status, cmd, iter, passed)
        }
    }

    async function runAgents(passed){
        console.log("RUNNING AGENTS", passed)
        setData({...passed})
        console.log(passed)
        for(let i = 0; i < 30; i++){
            for(let j = 0; j < passed.agents.length; j++){
                run(passed.agents, passed.agents[j], passed.agents[j].sequence[i], j, passed)
            }
            await new Promise(r => setTimeout(r, 1000));
        }
    }

    const [gridSize, setGridSize] = useState(10)
    const [seed, setSeed] = useState("joe")
    const [trucks, setTrucks] = useState(1)
    const [searchType, setSearchType] = useState("Breadth First Search")

    const fetchData = () => {
        setLoading(true)
        axios.post('http://127.0.0.1:5000/search', {
            "trucks": trucks,
            "seed": seed,
            "goals": trucks,
            "gridsize": gridSize,
            "search": "Breadth First Search"
        })
        .then(function (response) {
            console.log(response.data)
            setData({...response.data})
            // setSavedData({...response.data})
            localStorage.setItem('search', JSON.stringify(response.data));
            setLoading(false)
            runAgents(response.data)
        })
    }

    const [oldID, setOldID] = useState("")

    const loadOld = () => {
        setLoading(true)
        const fetchOld = async () => {
            const pb = new PocketBase('http://localhost:8090')

            const authData = await pb.admins.authWithPassword('shelleywr23@mail.vmi.edu', 'rootrootroot');
            console.log("OLD ID", oldID)
            const record = await pb.collection('searchRecords').getOne(oldID);
            
            setData({...record.search})
            setLoading(false)
            console.log({"records": record.search})
            return record.search
        }
        
        fetchOld()
            .then((data) => { 
                runAgents(data)
            })
            
    }
    
    if(loading){
        return <div>Loading...</div>
    }

    return(
        <div className="flex justify-center gap-10">
            <InputFields setGridSize={setGridSize} setSeed={setSeed} setTrucks={setTrucks} setSearchType={setSearchType} runAgents={runAgents} activeTab={activeTab} setActiveTab={setActiveTab} oldID={oldID} setOldID={setOldID} reset={reset} loadOld={loadOld} fetchData={fetchData}/>
            {/* {InputFields({setGridSize, setSeed, setTrucks, setSearchType, runAgents, activeTab, setActiveTab, oldID, setOldID, reset, loadOld, fetchData})} */}
            <Grid grid={data.grid}/>
        </div>
    )
}
