import React from 'react'

import { useMovies, useSearch } from '../hooks/hooks'
import { Movies } from './Movies'

export function App () {
  const { movies: mappedMovies } = useMovies()
  const { search, updateSearch, error } = useSearch()

  const handleSubmit = (event) => {
    event.preventDefault()
  }

  const handleChange = (event) => {
    const newQuery = event.target.value
    updateSearch(newQuery)
  }

  return (
    <div className='App'>
      <header>
        <h1>Search movies</h1>
        <form className='form' onSubmit={handleSubmit}>
          <input className='form-search-input' onChange={handleChange} value={search} type='text' id='queryId' name='query' placeholder='Star wars, Avengers, Matrix' />
          <button className='form-search-button' type='submit'>Search</button>
        </form>
        {error && <p className='error-message'>{error}</p>}
      </header>
      <main>
        <Movies movies={mappedMovies} />
      </main>
    </div>
  )
}
