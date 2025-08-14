import { useEffect, useState } from "react";

function App() {
    const [count , setCount] = useState(0)

    const fetachCounter = async () =>{
        const res = await fetch("https")
        const data = res.json()
        setCount(data.value)

    }

    const updateCounter = async (action) =>{

        const res = await fetch("post url",{
            method: "POST",
            headers: {
                "content-type" : "application/json"
            }
            ,
            body : JSON.stringify({action})
    })
    const data = await res.json()
    setCount(data.value)

    };

    useEffect (()=> {
        fetachCounter()
    },[])

    return (
        <div> 
            <h1> Counter :{count}</h1>
            <button onClick={() => updateCounter("increment")}> increment</button>
        </div>
    )
}