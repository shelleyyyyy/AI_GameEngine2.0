import Link from 'next/link'


export default function Layout({ children }) {
    return(
        <>
            <div className="flex justify-center">
                <div className="border-b-2 hover:border-black cursor-pointer transition p-3 text-xl">
                    <Link href="/Playground">Playgorund</Link>
                </div>
                <div className="border-b-2 hover:border-black cursor-pointer transition p-3 text-xl">
                    <Link href="/Experiments">Experiments</Link>
                </div>
            </div>           
            
            {children}
        </> 
    )
}

