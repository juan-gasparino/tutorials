import React from 'react'

import { useMovies } from '../hooks/hooks'
import { Movies } from './Movies'

export function App () {
  const { movies: mappedMovies } = useMovies()

  const handleSubmit = (event) => {
    event.preventDefault()
    const fields = Object.fromEntries(
      new window.FormData(event.target)
    )
    console.log(fields)
  }

  return (
    <div className='App'>
      <header>
        <h1>Search movies</h1>
        <form className='form' onSubmit={handleSubmit}>
          <input className='form-search-input' type='text' id='queryId' name='query' placeholder='Star wars, Avengers, Matrix' />
          <button className='form-search-button' type='submit'>Search</button>
        </form>
      </header>
      <main>
        <Movies movies={mappedMovies} />
      </main>
    </div>
  )
}
