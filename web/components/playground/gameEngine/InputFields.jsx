import {React, useState} from "react"

export default function InputFields({ reset, loadOld, test }){

    const TextBox = ({ field }) => {
        return(
            <div className="form-control px-5 py-2">
                <label className="label">
                    <span className="label-text">{field}</span>
                </label>
                <label className="input-group">
                    <input type="text" placeholder={field} className="input input-bordered" />
                </label>
            </div>
        )
    }

    const DropDown = () => {

        const options = ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm", "A* Search"]

        return(
            <div className="form-control px-5 py-2">
                <label className="label">
                    <span className="label-text">Search Type</span>
                </label>
                <div className="input-group ">
                    <select className="select select-bordered w-full">
                        {options.map((option, k) => (
                            <option>{option}</option>
                        ))}
                    </select>
                </div>
            </div>
        )
    }

    const [activeTab, setActiveTab] = useState("new")

    const TabSwitch = () => {
        // define swithc function
        if(activeTab == "new"){
            const fields = ["Grid Size", "Seed", "Trucks"]

            return(
                <div className="rounded-xl shadow-xl py-5 grid justify-center">
                    
                    {fields.map((field, k) => (
                        <TextBox field={field}/>
                    ))}

                    <DropDown/>

                    <button onClick={test} className="btn btn-primary m-5">Load</button>
                    <button onClick={reset} className="btn btn-primary m-5">Reset</button>
                </div>
            )
        } else if(activeTab == "old"){
            const fields = ["Grid ID"]

            return(
                <div className="rounded-xl shadow-xl py-5 grid justify-center">
                    
                    {fields.map((field, k) => (
                        <TextBox field={field}/>
                    ))}

                    <button className="btn btn-primary m-5" onClick={loadOld}>Load</button>

                </div>
            )
        }
    }
    return(

        
        <div>
            <div className="tabs tabs-boxed flex justify-center m-10">
                <div onClick={() => setActiveTab("new")} className={activeTab === "new" ? "tab-active tab" : "tab"}>New</div> 
                <div onClick={() => setActiveTab("old")} className={activeTab === "old" ? "tab-active tab" : "tab"}>Old</div> 
            </div>

            <h1 className="text-xl bold text-center p-5">Input Fields</h1>

            <TabSwitch />
        </div>



    )
}