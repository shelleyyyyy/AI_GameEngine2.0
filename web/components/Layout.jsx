import Link from 'next/link'


export default function Layout({ children }) {
    return(
        <>
            {/* <div className="flex justify-center">
                <div className="border-b-2 hover:border-black cursor-pointer transition p-3 text-xl">
                    <Link href="/Playground">Playgorund</Link>
                </div>
                <div className="border-b-2 hover:border-black cursor-pointer transition p-3 text-xl">
                    <Link href="/Experiments">Experiments</Link>
                </div>
            </div>            */}

            <div className="navbar bg-base-100">
                <div className="flex-1">
                    <Link href="/" className="btn btn-ghost normal-case text-xl">Trucks</Link>
                </div>
                <div className="flex-none">
                    <ul className="menu menu-horizontal p-0">
                        <li><Link href="/Playground">Playground</Link></li>
                        <li><Link href="/Experiments">Experiments</Link></li>
                    </ul>
                </div>
            </div>
            
            {children}
        </> 
    )
}
