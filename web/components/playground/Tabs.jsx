import {React, useState} from "react"
import GameEngine from "./gameEngine/GameEngine"
import Stats from "./stats/Stats"
export default function Tabs({ tabs }){

    
    const data = {
        grid: [
            ["c", "c", "c", "c", "c"],
            ["a-d", "a-d", "a-d", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "g", "c"],
            ["c", "c", "c", "c", "c"]
        ],
        stats: {
            size: 5,
            longestPath: 7,
            shortestPath: 5,
        },
        agents: [
            {
                position: {
                    x: 0,
                    y: 1,
                },
                status: "a-d",
                sequence: ['l', 'r  ', 'm', 'm', 'l', 'm', 'm'],
                stats: {
                    id: 1,
                    time: 5,
                    path: 5,
                }
            },
            {
                position: {
                    x: 0,
                    y: 1,
                },
                status: "a-d",
                sequence: ['l', 'r  ', 'm', 'm', 'l', 'm', 'm'],
                stats: {
                    id: 1,
                    time: 5,
                    path: 5,
                }
            },
            
        ], 
        searchTypes: [
            "Breadth First Search",
            "Depth First Search",
            "Depth Limit Search",
            "Uniform Cost Search",
            "Iterative Depth Limited Search"
        ]
    }
    
    
    
    const [activeTab, setActiveTab] = useState(tabs[0])



    const TabSwitch = () => {
        // define swithc function
        if(activeTab == "GameEngine"){
            return(
                <div>
                    <GameEngine data={data}/>
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