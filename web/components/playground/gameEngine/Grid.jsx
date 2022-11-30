
export default function Grid(){

    const grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,'a',0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,'c',0,0,0,0,0,0,0]
    ]

    console.log(grid.length)

    const itemSize = grid.length * 1
    const height = "h-[" + itemSize + "em]"
    const width = " w-[" + itemSize + "em]"
    const s = itemSize + "rem"
    console.log(s)


    const Item = ({item}) => {
        if(item == "a"){
            return(
                <div style={{width: s, height: s}} className={"gap bg-red-400 shadow-xl text-black rounded-xl"} >

                </div>
            )
        } else if(item == "c"){
            return(
                <div style={{width: s, height: s}} className="gap bg-black shadow-xl w-20 h-20 text-black rounded-xl">

                </div>
            )
        } else if(item == "p"){
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl w-20 h-20 text-black rounded-xl">

                </div>
            )
        } else {
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl w-20 h-20 text-black rounded-xl">
                    
                </div>
            )
        }
    }

    const Row = ({ row }) => {
        return(
            <div className="flex gap-5">
                {row.map((item, k) => (
                    <Item item={item} key={k}/>
                ))}

            </div>
        )
    }

    return(
        <div className="gap-5 grid justify-center">

            {grid.map((row, k) => (
                <Row row={row} key={k}/>
            ))}
        </div>

    )
}
