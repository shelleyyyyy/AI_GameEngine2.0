

import PocketBase from 'pocketbase'
import { useEffect, useState } from 'react'

export default function Stats({ data }){
    
    const BlockGeneral = ({ one, two, three }) => {
        return(
            <div className="stats shadow">
                <div className="stat">
                    <div className="stat-title">Size</div>
                    <div className="stat-value">{one}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-title">Longest Path</div>
                    <div className="stat-value">{two}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-title">Shortest Path</div>
                    <div className="stat-value">{three}</div>
                </div>
            </div>
        )
    }

    const Block = ({ one, two, three }) => {
        return(
            <div className="stats shadow">
                <div className="stat">
                    <div className="stat-title">ID</div>
                    <div className="stat-value">{one}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-title">Path Length</div>
                    <div className="stat-value">{two}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-title">Time To Solve</div>
                    <div className="stat-value">{three}</div>
                </div>
            </div>
        )
    }

    const save = () => {

        console.log(data)

        const createData = {
            "search": data,
        }

        // console.log(createData)

        const fetchData = async () => {
            const pb = new PocketBase('http://localhost:8090')
            const authData = await pb.admins.authWithPassword('shelleywr23@mail.vmi.edu', 'rootrootroot');
            const record = await pb.collection('searchRecords').create(createData);
        }
        fetchData()
    }

    return(
        <div className="grid justify-center">
            <div className="flex justify-center ">
                <div className="">
                    <h1 className="text-center text-4xl p-10">Overview</h1>
                </div>
                <div className=" flex items-center justify-center">
                    <button className="btn" onClick={save}>Save</button>
                </div>
            </div>
            <BlockGeneral one={data.stats.size} two={data.stats.longestPath} three={data.stats.shortestPath}/>

            <h1 className="text-center text-4xl p-10">Agents</h1>
            <div className="grid grid-cols-1 gap-5">
                {data.agents.map((agent, index) => {
                    return(
                        <Block key={index} one={agent.stats.id} two={agent.stats.path} three={agent.stats.time}/>
                    )
                })}
            </div>
        </div>
    )
}