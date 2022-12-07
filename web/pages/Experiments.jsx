import { useEffect, useState } from 'react'

import PocketBase from 'pocketbase'
import Table from "../components/experiments/Table"

export default function Experiments(){

    const PB_HOST = process.env.NEXT_PUBLIC_PB_IP;
    const PB_PORT = process.env.NEXT_PUBLIC_PB_PORT;

    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        setLoading(true)
        const fetchData = async () => {
            const pb = new PocketBase(`http://${PB_HOST}:${PB_PORT}`)
            
            const res = await pb.collection('searchRecords').getFullList(200, {
                sort: '-created',
            });
            
            return res
        }

        fetchData()
            .then((res) => {
                setData(res)
                setLoading(false)
            })
    }, []) 

    if(loading){
        return <div className="mx-96 my-20">Loading...</div>
    }

    return(
        <div className="mx-10">
            <h1 className='text-5xl text-center pb-10'>Experiments</h1>
            <Table d={data}/>
        </div>
    )
}
