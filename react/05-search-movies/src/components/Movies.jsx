import React from 'react'

const ListMovies = ({ movies }) => {
  return (
    <ul className='movies'>
      {
        movies.map(movie => (
          <li className='movie' key={movie.id}>
            <h3 className='movie-title'>{movie.title}</h3>
            <p className='movie-year'>{movie.year}</p>
            <img className='movie-poster' src={movie.image} alt={movie.title} />
          </li>
        ))
      }
    </ul>
  )
}

const MoviesNotFound = () => {
  return (
    <p>Movie not found!</p>
  )
}

export function Movies ({ movies }) {
  const hasMovies = movies?.length > 0

  return (
    <>
      {
      hasMovies
        ? <ListMovies movies={movies} />
        : <MoviesNotFound />
      }
    </>
  )
}
