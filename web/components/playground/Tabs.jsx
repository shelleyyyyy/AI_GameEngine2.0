import {React, useState} from "react"
import GameEngine from "./gameEngine/GameEngine"
import Stats from "./stats/Stats"
import PocketBase from 'pocketbase'
import axios from 'axios'

export default function Tabs({ tabs }){

    const original = {
        grid: [
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],

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
    const [loading, setLoading] = useState(false)
    const [oldID, setOldID] = useState("")

    const [grid, setGrid] = useState(data.grid)
    const [agents, setAgents] = useState(data.agents)

    const [activeSubTab, setActiveSubTab] = useState("new")

    const loadOld = () => {
        setLoading(true)
        const fetchData = async () => {
            const pb = new PocketBase('http://localhost:8090')

            const authData = await pb.admins.authWithPassword('shelleywr23@mail.vmi.edu', 'rootrootroot');
            console.log("OLD ID", oldID)
            const record = await pb.collection('searchRecords').getOne(oldID);
            
            setData(record.search)
            setLoading(false)
            console.log(record.search)
        }
        
        fetchData()
            .then((res) => console.log(res))
    }   

    const reset = () => {
        console.log("Reset")
        setGrid(original.grid)
        setData(original)
    }
    
    const [activeTab, setActiveTab] = useState(tabs[0])

    const TabSwitch = () => {
        // define swithc function
        if(activeTab == "GameEngine"){
            return(
                <div>
                    <GameEngine activeTab={activeSubTab} setActiveTab={setActiveSubTab} oldID={oldID} setOldID={setOldID} setData={setData} reset={reset} loadOld={loadOld} data={data}/>
                </div>
            )
        } else if(activeTab == "Stats"){
            return(
                <div>
                    <Stats data={data}/>
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