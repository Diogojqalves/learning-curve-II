import React, { useState } from 'react';

import Card from '../card/card.component';

const UseStateExample = () => {
  const [name, setName] = useState('Diogo');
  const [address, setAddress] = useState('Porto');

  return (
    <Card>
      <h1> {name} </h1>
      <h1> {address} </h1>
      <button onClick={() => setName('Andrei')}>Set Name to Andrei</button>
      <button onClick={() => setAddress('Canada')}>Set Address</button>
    </Card>
  );
};

export default UseStateExample;
