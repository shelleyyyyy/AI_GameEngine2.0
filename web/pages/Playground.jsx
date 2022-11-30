import React from 'react';
import Tabs from '../components/playground/Tabs';

export default function Playground() {


    const tabs = ["GameEngine", "Stats"]

    


  return (
    <div>
      <Tabs tabs={tabs}/>
    </div>
  )
}