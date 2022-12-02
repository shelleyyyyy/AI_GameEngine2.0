

import { BsTruck } from 'react-icons/bs';
import { AiOutlineArrowRight } from 'react-icons/ai';
import { IoMdArrowDropright } from 'react-icons/io';
import { IconContext } from "react-icons";
import { BsFillEmojiHeartEyesFill } from 'react-icons/bs';

export default function Grid({ grid }){

    // console.log(grid.length)

    const itemSize = 40 / grid.length 
    const s = itemSize + "rem"

    const Item = ({item}) => {
        if(item == "a-u"){
            return(
                <div style={{width: s, height: s}} className={"gap bg-red-400 shadow-xl text-black rounded-xl p-3 flex justify-center place-items-center"} >
                     <BsTruck className="h-full w-full" style={{transform: 'rotate(270deg)' }}/>
                </div>
            )
        } else if(item == "a-r"){
            return(
                <div style={{width: s, height: s}} className={"gap bg-red-400 shadow-xl text-black rounded-xl p-3 flex justify-center "} >
                    <BsTruck className="h-full w-full"/>
                </div>
            )
        }
        else if(item == "a-d"){
            return(
                <div style={{width: s, height: s}} className={"gap bg-red-400 shadow-xl text-black rounded-xl p-3 flex justify-center p-3"} >
                    <BsTruck className="h-full w-full" style={{transform: 'rotate(90deg)' }}/>
                </div>
            )
        } else if(item == "a-l"){
            return(
                <div style={{width: s, height: s}} className={"gap bg-red-400 shadow-xl text-black rounded-xl p-3 flex justify-center"} >
                    <BsTruck className="h-full w-full" style={{transform: 'rotate(180deg)' }}/>
                </div>
            )
        } else if(item == "c"){
            return(
                <div style={{width: s, height: s}} className="gap bg-black shadow-xl text-black rounded-xl p-3">
                    <BsTruck className="h-full w-full" style={{transform: 'rotate(90deg)' }}/>
                </div>
            )
        } else if(item == "p-u"){
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl text-black rounded-xl p-3">
                    <IoMdArrowDropright className="h-full w-full" style={{transform: 'rotate(90deg)' }}/>
                </div>
            )
        }
        else if(item == "p-r"){
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl text-black rounded-xl p-3">
                    <IoMdArrowDropright className="h-full w-full"/>
                </div>
            )
        }
        else if(item == "p-d"){
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl text-black rounded-xl p-3">
                    <IoMdArrowDropright className="h-full w-full" style={{transform: 'rotate(90deg)' }}/>
                </div>
            )
        }
        else if(item == "p-l"){
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl text-black rounded-xl p-3">
                    <IoMdArrowDropright className="h-full w-full" style={{transform: 'rotate(90deg)' }}/>
                </div>
            )
        } else if(item == "g"){
            return(
                <div style={{width: s, height: s}} className="gap bg-pink-500 shadow-xl text-black rounded-xl p-3">
                    <BsFillEmojiHeartEyesFill className="h-full w-full "/>
                </div>
            )
        } else {
            return(
                <div style={{width: s, height: s}} className="gap bg-white shadow-xl text-black rounded-xl p-3">
                
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
