import { useCatFact, useCatRandomImage } from './hooks/hooks.js'
import './App.css'
import { useState } from 'react'

export function App () {
  const [buttonClicked, useButtonClicked] = useState(false)
  const { fact, callRandomCat } = useCatFact()
  const { imageUrl } = useCatRandomImage({ fact })

  const test = () => {
    useButtonClicked(true)
    callRandomCat()
  }

  return (
    <main>
      <h1>App test</h1>

      <button onClick={test}>Get new fact</button>
      {buttonClicked !== true ? null : <p data-testid='click-ok'>button clicked</p>}
      {fact && <p>{fact}</p>}
      {imageUrl && <img src={imageUrl} alt='random cat image from API' />}

    </main>
  )
}
