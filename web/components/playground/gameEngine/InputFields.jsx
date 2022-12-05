import {React, useState} from "react"

export default function InputFields(props, { box1 }){

    const [gridSize, setGridSize] = useState(10)
    const [trucks, setTrucks] = useState(1)
    const [seed, setSeed] = useState(0)
    const [searchType, setSearchType] = useState("dfs")

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

        const options = ["Breadth First Search", "Depth First Search", "Depth Limit Search", "Uniform Cost Search",
        "Iterative Depth Limited Search", "Dijkstra's Algorithm", "A* Search"]

        return(
            <div className="form-control px-5 py-2">
                <label className="label">
                    <span className="label-text">Search Type</span>
                </label>
                <div className="input-group ">
                    <select className="select select-bordered w-full">
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

        const setValuesAndLoad = () => {
            props.setGridSize(gridSize)
            props.setSeed(seed)
            props.setTrucks(trucks)
            props.setSearchType(searchType)
            props.fetchData()
        }

        if(props.activeTab == "new"){
            const fields = ["GridSize", "Seed", "Trucks"]
            
            return(
                <div className="rounded-xl shadow-xl py-5 grid justify-center">

                    {/* <TextBox field="Grid Size" setValue={setGridSize}/>
                    <TextBox field="Seed" setValue={setSeed}/>
                    <TextBox field="Trucks" setValue={setTrucks}/> */}
                    {box1}
                    {TextBox({field: "Grid Size", setValue: setGridSize})}
                    {TextBox({field: "Seed", setValue: setSeed})}
                    {TextBox({field: "Trucks", setValue: setTrucks})}

                    <DropDown/>

                    <button onClick={setValuesAndLoad} className="btn btn-primary m-5">Load</button>
                    <button onClick={props.reset} className="btn btn-primary m-5">Reset</button>
                </div>
            )
        } else if(props.activeTab == "old"){
            return(
                <div className="rounded-xl shadow-xl py-5 grid justify-center">
                    {/* <input value={oldID} onChange={(e) => setOldID(e.target.value)} type="text" placeholder="Grid ID" className="input input-bordered input-error w-full max-w-xs" /> */}
                    <div className="form-control px-5 py-2">
                        <label className="label">
                            <span className="label-text">Grid ID</span>
                        </label>
                        <label className="input-group">
                            <input value={props.oldID} onChange={(e) => props.setOldID(e.target.value)} type="text" placeholder={"dqw2z2490pananx"} className="input input-bordered" />
                        </label>
                    </div>
                    <button className="btn btn-primary m-5" onClick={props.loadOld}>Load</button>
                </div>
            )
        }
    }
    return(
        <div className="h-40">
            <div className="tabs tabs-boxed flex justify-center m-10">
                <div onClick={() => props.setActiveTab("new")} className={props.activeTab === "new" ? "tab-active tab" : "tab"}>New</div> 
                <div onClick={() => props.setActiveTab("old")} className={props.activeTab === "old" ? "tab-active tab" : "tab"}>Old</div> 
            </div>

            <h1 className="text-xl bold text-center p-5">Input Fields</h1>

            <TabSwitch />
        </div>
    )
}