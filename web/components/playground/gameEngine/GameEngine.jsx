import Grid from "./Grid"
import InputFields from "./InputFields"

export default function GameEngine(){
    return(
        <div className="flex justify-center gap-10">
            <InputFields/>
            <Grid/>
        </div>
    )
}