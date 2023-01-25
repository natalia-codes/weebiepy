import React, {useState, useEffect} from 'react'

function App() {

  const [data, setData] = useState([{}])
  console.log(data)

  useEffect(() => {
    fetch('/test').then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div>
      {(typeof data.itemsTest === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.itemsTest.map((items, i) => (
          <p key={i}>{items}</p>
        ))
      )}
    </div>
  )
}

export default App