import { useEffect, useState, useRef } from 'react'

export function useMovies ({ search }) {
  const [responseMovies, setResponseMovies] = useState([])

  const getMovies = () => {
    if (search) {
      fetch(`https://omdbapi.com/?apikey=4287ad07&s=${search}`)
        .then(response => response.json())
        .then(data => {
          const movies = data.Search?.map(data => ({
            id: data.imdbID,
            title: data.Title,
            image: data.Poster,
            year: data.Year
          }))
          setResponseMovies(movies)
        })
    }
  }

  return { movies: responseMovies, getMovies }
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

  return { search, updateSearch, isFirstTime, error }
}
