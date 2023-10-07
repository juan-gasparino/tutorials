import { useEffect, useState, useRef } from 'react'
import moviesMock from '../mocks/movies.json'

export function useMovies () {
  const movies = moviesMock.Search

  const mappedMovies = movies?.map((movie) => ({
    id: movie.imdbID,
    title: movie.Title,
    image: movie.Poster,
    year: movie.Year
  }))

  return { movies: mappedMovies }
}

export function useSearch () {
  const [search, updateSearch] = useState('')
  const [error, setError] = useState(null)
  const isFirstTime = useRef(true)

  useEffect(() => {
    if (isFirstTime.current === true) {
      isFirstTime.current = search === ''
      return
    }

    if (search === '') {
      setError('No se puede buscar una película vacía')
      return
    }

    if (search.match(/^\d+$/)) {
      setError('No se puede buscar una película con un número')
      return
    }

    if (search.length < 3) {
      setError('La búsqueda debe tener al menos 3 caracteres')
      return
    }

    setError(null)
  }, [search])

  return { search, updateSearch, error }
}
