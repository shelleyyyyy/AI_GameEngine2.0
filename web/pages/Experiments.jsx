import { useEffect, useState } from 'react'

import PocketBase from 'pocketbase'
import Table from "../components/experiments/Table"

export default function Experiments(){

    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        setLoading(true)
        const fetchData = async () => {
            const pb = new PocketBase('http://localhost:8090')

            const authData = await pb.admins.authWithPassword('shelleywr23@mail.vmi.edu', 'rootrootroot');
            
            const res = await pb.collection('searchRecords').getFullList(200, {
                sort: '-created',
            });
            
            return res

            setData(res)
            setLoading(false)
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
