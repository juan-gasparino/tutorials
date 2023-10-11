import React, { useRef, useState } from 'react'

import { useMovies, useSearch } from '../hooks/hooks'
import { Movies } from './Movies'

export function App () {
  const [sort, setSort] = useState(false)
  const { search, updateSearch, isFirstTime, error } = useSearch()
  const { movies, getMovies } = useMovies({ search, sort })
  const previousSearch = useRef(search)

  const handleSubmit = (event) => {
    event.preventDefault()
    if (previousSearch.current !== event.target.childNodes[0].value) {
      getMovies(search)
      previousSearch.current = event.target.childNodes[0].value
    }
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
          <button className='form-sort-button' type='checkbox' defaultChecked />
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
