
import useCopyToClipboard from "../../hooks/useCopyToClipboard"

import { FiCopy } from "react-icons/fi"

export default function Table({ d }){

    // console.log(d[0].search)

    const data = [
        {
            "id": 1,
            "search": "Breadth First Search",
            "time": 5,
            "shortestPath": 5,
            "trucks": 2,
            "longestPath": 9,
            "trucks_info": [
                {
                    "id": 1,
                    "time": 5,
                    "path": 5
                },
                {
                    "id": 1,
                    "time": 5,
                    "path": 5
                },
                {
                    "id": 1,
                    "time": 5,
                    "path": 5
                },
                {
                    "id": 1,
                    "time": 5,
                    "path": 5
                }
            ]
        },
        {
            id: 2,
            search: "Breadth First Search",
            time: 5,
            shortestPath: 5,
            trucks: 2,
            longestPath: 9,
            trucks_info: [
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
            ]
        },
        {
            id: 3,
            search: "Breadth First Search",
            time: 5,
            shortestPath: 5,
            trucks: 2,
            longestPath: 9,
            trucks_info: [
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
                {
                    id: 1,
                    time: 5,
                    path: 5,
                },
            ]
        },
    ]

    const BlockGeneral = ({ one, two, three }) => {
        return(
            <div className="stats shadow">
                <div className="stat">
                    <div className="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-8 h-8 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <div className="stat-title">Size</div>
                    <div className="stat-value">{one}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-8 h-8 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                    </div>
                    <div className="stat-title">Longest Path</div>
                    <div className="stat-value">{two}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-8 h-8 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path></svg>
                    </div>
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
                    <div className="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-8 h-8 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <div className="stat-title">ID</div>
                    <div className="stat-value">{one}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-8 h-8 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                    </div>
                    <div className="stat-title">Path</div>
                    <div className="stat-value">{two}</div>
                </div>
                
                <div className="stat">
                    <div className="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-8 h-8 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path></svg>
                    </div>
                    <div className="stat-title">Time</div>
                    <div className="stat-value">{three}</div>
                </div>
            </div>
        )
    }

    const Modal = ({ data }) => {

        return(
            <>
                <label htmlFor="my-modal-4" className="btn btn-ghost btn-xs">Details</label>

                <input type="checkbox" id="my-modal-4" className="modal-toggle" />
                <label htmlFor="my-modal-4" className="modal cursor-pointer">
                    <div className="bg-gray-500 grid gap-5 p-5 rounded-xl">
                        <h3 className="text-3xl font-bold text-center">Info</h3>
                        <BlockGeneral one={data.search.stats.size} two={data.search.stats.shortestPath} three={data.search.stats.longestPath} />
                        <h3 className="text-3xl font-bold text-center">Trucks</h3>
                        {data.search.agents.map((truck, index) => {
                            return(
                                <Block key={index} one={truck.stats.id} two={truck.stats.path} three={truck.stats.time} />
                            )
                        })}
                    </div>  
                </label>
            </>
        )
    }

    const [value, copy] = useCopyToClipboard()

    function handleCopy(id) {
        copy(id)
    }

    return(
        <div className="m-0 p-0 w-full">
            <table className="table w-full m-0 p-0">
                <thead>
                    <tr>
                        <th>

                        </th>
                        <th>ID</th>
                        <th>Search</th>
                        <th>Longest Time</th>
                        <th>Shortest Time</th>
                        <th>Longest Path</th>
                        <th>Shortest Path</th>
                        <th>Trucks</th>
                        <th>Size</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {d.map((item, k) => (
                        <tr key={k}>
                            <td>
                                <label>
                                    <input type="checkbox" className="checkbox" />
                                </label>
                            </td>
                            <td>
                                <div className="flex gap-2">
                                    <div className="tooltip" data-tip="copy to clipboard">
                                        <FiCopy onClick={() => handleCopy(item.id)} className="h-full w-full cursor-pointer hover:text-gray-200 transition text-xl"/>
                                    </div>
                                    <div>
                                        {item.id}
                                    </div>
                                </div>
                            </td>
                            <td>{item.search.stats.search}</td>
                            
                            {/* time */}
                            <td>{item.search.stats.longestTime}</td>
                            <td>{item.search.stats.shortestTime}</td>

                            {/* path */}
                            <td>{item.search.stats.longestPath}</td>
                            <td>{item.search.stats.shortestPath}</td>

                            {/* trucks */}
                            <td>{item.search.stats.trucks}</td>

                            {/* size */}
                            <td>{item.search.stats.size}</td>

                            <td>
                                <Modal data={item}/>
                            </td>
                        </tr>
                    ))} 
                </tbody>
            </table>
        </div>
    )
}