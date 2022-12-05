import {React, useState, useEffect} from 'react';
import Grid from "./Grid"
// import InputFields from "./InputFields"
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
        for(let i = 0; i < passed.stats.longestPath; i++){
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

    const fetchData = (trucks, seed, gridSize, searchType) => {
        setLoading(true)
        axios.post('http://127.0.0.1:5000/search', {
            "trucks": trucks,
            "seed": seed,
            "goals": trucks,
            "gridsize": gridSize,
            "search": searchType
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

    const InputFields = () => {
        const TextBox = ({ field, setValue }) => {

            const handleChange = (e) => {
                console.log(e.target.value)
                setValue(e.target.value)
            }
    
            return(
                <div className="form-control px-5 py-2">
                    <label className="label">
                        <span className="label-text">{field}</span>
                    </label>
                    <label className="input-group">
                        <input onChange={handleChange} type="text" placeholder={field} className="input input-bordered" />
                    </label>
                </div>
            )
        }
    
        const DropDown = () => {
    
            const options = ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm", "A* Search"]

            const handleChange = (e) => {
                console.log(e.target.value)
                setSearchType(e.target.value)
            }

    
            return(
                <div className="form-control px-5 py-2">
                    <label className="label">
                        <span className="label-text">Search Type</span>
                    </label>
                    <div className="input-group ">
                        <select onChange={handleChange} className="select select-bordered w-full">
                            {options.map((option, k) => (
                                <option key={k}>{option}</option>
                            ))}
                        </select>
                    </div>
                </div>
            )
        }
    
        const TabSwitch = () => {
            // define swithc function
    
            
    
            if(activeTab == "new"){
                const fields = ["GridSize", "Seed", "Trucks"]

                const [nestedGridSize, setNestedGridSize] = useState(gridSize)
                const [nestedSeed, setNestedSeed] = useState(seed)
                const [nestedTrucks, setNestedTrucks] = useState(trucks)
                const [nestedSearchType, setNestedSearchType] = useState(searchType)



                const setValuesAndLoad = () => {
                    setGridSize(nestedGridSize)
                    // setSeed(seed)
                    // setTrucks(trucks)
                    // setSearchType(searchType)
                    fetchData(nestedTrucks, nestedSeed, nestedGridSize, "Breadth First Search")
                }
                    
                const handleGridSizeChange = (e) => {
                    console.log(e.target.value)
                    setNestedGridSize(e.target.value)
                }

                const handleSeedChange = (e) => {
                    console.log(e.target.value)
                    setNestedSeed(e.target.value)
                }

                const handleTrucksChange = (e) => {
                    console.log(e.target.value)
                    setNestedTrucks(e.target.value)
                }

                const handleDropChange = (e) => {
                    console.log(e.target.value)
                    setSearchType(e.target.value)
                }

                const options = ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm", "A* Search"]

                
                return(
                    <div className="rounded-xl shadow-xl py-5 grid justify-center">
    
                        <div className="form-control px-5 py-2">
                            <label className="label">
                                <span className="label-text">GridSize</span>
                            </label>
                            <label className="input-group">
                                <input onChange={handleGridSizeChange} type="text" placeholder={"Grid Size"} className="input input-bordered" />
                            </label>
                        </div>
                        <div className="form-control px-5 py-2">
                            <label className="label">
                                <span className="label-text">Seed</span>
                            </label>
                            <label className="input-group">
                                <input onChange={handleSeedChange} type="text" placeholder={"Seed"} className="input input-bordered" />
                            </label>
                        </div>
                        <div className="form-control px-5 py-2">
                            <label className="label">
                                <span className="label-text">Trucks</span>
                            </label>
                            <label className="input-group">
                                <input onChange={handleTrucksChange} type="text" placeholder={"Trucks"} className="input input-bordered" />
                            </label>
                        </div>

                        {/* <DropDown/> */}
                        <div className="form-control px-5 py-2">
                            <label className="label">
                                <span className="label-text">Search Type</span>
                            </label>
                            <div className="input-group ">
                                <select onChange={handleDropChange} className="select select-bordered w-full">
                                    <option >{"Breadth First Search"}</option>
                                    <option >{"Depth First Search"}</option>
                                    <option >{"Dijkstra's Algorithm"}</option>
                                </select>
                            </div>
                        </div>
    
                        <button onClick={setValuesAndLoad} className="btn btn-primary m-5">Load</button>
                        <button onClick={reset} className="btn btn-primary m-5">Reset</button>
                    </div>
                )
            } else if(activeTab == "old"){
                return(
                    <div className="rounded-xl shadow-xl py-5 grid justify-center">
                        {/* <input value={oldID} onChange={(e) => setOldID(e.target.value)} type="text" placeholder="Grid ID" className="input input-bordered input-error w-full max-w-xs" /> */}
                        <div className="form-control px-5 py-2">
                            <label className="label">
                                <span className="label-text">Grid ID</span>
                            </label>
                            <label className="input-group">
                                <input value={oldID} onChange={(e) => setOldID(e.target.value)} type="text" placeholder={"dqw2z2490pananx"} className="input input-bordered" />
                            </label>
                        </div>
                        <button className="btn btn-primary m-5" onClick={loadOld}>Load</button>
                    </div>
                )
            }
        }
        return(
            <div className="h-40">
            <div className="tabs tabs-boxed flex justify-center m-10">
                <div onClick={() => setActiveTab("new")} className={activeTab === "new" ? "tab-active tab" : "tab"}>New</div> 
                <div onClick={() => setActiveTab("old")} className={activeTab === "old" ? "tab-active tab" : "tab"}>Old</div> 
            </div>

            <h1 className="text-xl bold text-center p-5">Input Fields</h1>

            <TabSwitch />
        </div>
        )
    }

    return(
        <div className="flex justify-center gap-10">
            {/* <InputFields setGridSize={setGridSize} setSeed={setSeed} setTrucks={setTrucks} setSearchType={setSearchType} runAgents={runAgents} activeTab={activeTab} setActiveTab={setActiveTab} oldID={oldID} setOldID={setOldID} reset={reset} loadOld={loadOld} fetchData={fetchData}/> */}
            {InputFields()}
            <Grid grid={data.grid}/>
        </div>
    )
}
