'use client'
import {useEffect,useState} from 'react'

export default function Dashboard(){
 const [data,setData]=useState([])
 useEffect(()=>{
   fetch('/api/scan')
     .then(r=>r.json())
     .then(setData)
 },[])

 return (
  <main style={{background:'#020617',color:'white',minHeight:'100vh',padding:'20px'}}>
   <h2>Screener IDX</h2>
   <table border={1}>
    <thead>
     <tr>
      <th>Kode</th><th>Trend</th><th>RSI</th>
      <th>TP1</th><th>TP2</th><th>SL</th><th>Score</th>
     </tr>
    </thead>
    <tbody>
     {data.map((x:any,i:number)=>(
      <tr key={i}>
       <td>{x.ticker}</td>
       <td>{x.trend}</td>
       <td>{x.rsi}</td>
       <td>{x.tp1}</td>
       <td>{x.tp2}</td>
       <td>{x.sl}</td>
       <td>{x.score}</td>
      </tr>
     ))}
    </tbody>
   </table>
  </main>
 )
}
