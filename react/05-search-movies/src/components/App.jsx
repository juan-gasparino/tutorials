import React, { useRef } from 'react'

import { useMovies, useSearch } from '../hooks/hooks'
import { Movies } from './Movies'

export function App() {
  const { search, updateSearch, isFirstTime, error } = useSearch()
  const { movies, getMovies } = useMovies({ search })
  const previousSearch = useRef(search)

  const handleSubmit = (event) => {
    event.preventDefault()
    getMovies(search)
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
          <input
            className='form-search-input'
            onChange={handleChange}
            value={search}
            type='text'
            id='queryId'
            name='query'
            placeholder='Star wars, Avengers, Matrix'
          />
          <button className='form-search-button' type='submit'>Search</button>
        </form>
        {error && <p className='error-message'>{error}</p>}
      </header>
      <main>
        {!isFirstTime.current && <Movies movies={movies} />}
      </main>
    </div>
  )
}
