import {React, useState} from "react"
import GameEngine from "./gameEngine/GameEngine"
import Stats from "./stats/Stats"
import axios from 'axios'

export default function Tabs({ tabs }){

    const original = {
        grid: [
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
        ],
        stats: {
            size: 5,
            longestPath: 9,
            shortestPath: 5,
            trucks: 2,
            longestTime: 5,
            shortestTime: 2,
            search: "Breadth First Search"
        },
        agents: [
            {
                position: {
                    x: 0,
                    y: 1,
                },
                status: "a-d",
                sequence: ['l', 'r', 'm', 'm', 'l', 'm', 'm'],
                stats: {
                    id: 1,
                    time: 5,
                    path: 5,
                }
            },
            {
                position: {
                    x: 0,
                    y: 0,
                },
                status: "a-d",
                sequence: ['l', 'r', 'm', 'm', 'm', 'l', 'm', 'm'],
                stats: {
                    id: 1,
                    time: 5,
                    path: 5,
                }
            },
        ]
    }

    const [data, setData] = useState(original)
    const [oldID, setOldID] = useState("")
    const [savedData, setSavedData] = useState(original)

    const [activeSubTab, setActiveSubTab] = useState("new")

    const reset = () => {
        setData({...original})
    }
    
    const [activeTab, setActiveTab] = useState(tabs[0])

    const TabSwitch = () => {
        // define swithc function
        if(activeTab == "GameEngine"){
            return(
                <div>
                    <GameEngine setSavedData={setSavedData} activeTab={activeSubTab} setActiveTab={setActiveSubTab} oldID={oldID} setOldID={setOldID} setData={setData} reset={reset} data={data}/>
                </div>
            )
        } else if(activeTab == "Stats"){
            return(
                <div>
                    <Stats data={savedData}/>
                </div>
            )
        }
    }

    return(
        <>
            <div className="tabs tabs-boxed flex justify-center m-10">
                {tabs.map((tab, k) => (
                    <div onClick={() => setActiveTab(tab)} key={k} className={activeTab === tab ? "tab-active tab" : "tab"}>{tab}</div> 
                ))}
            </div>

            <TabSwitch />
        </>


    )
}