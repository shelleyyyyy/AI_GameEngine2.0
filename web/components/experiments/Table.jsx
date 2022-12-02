
import useCopyToClipboard from "../../hooks/useCopyToClipboard"

import { FiCopy } from "react-icons/fi"

export default function Table({ d }){

    // console.log(d[0].search)

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
                    <div className="stat-title">Path</div>
                    <div className="stat-value">{two}</div>
                </div>
                
                <div className="stat">
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