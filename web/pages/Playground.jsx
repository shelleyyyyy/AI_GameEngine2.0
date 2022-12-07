import React from 'react';
import Tabs from '../components/playground/Tabs';

export default function Playground() {


  const tabs = ["GameEngine", "Stats"]

  return (
    <div>
      <h1 className='text-5xl text-center pb-10'>Playground</h1>
      <Tabs tabs={tabs}/>
    </div>
  )
}