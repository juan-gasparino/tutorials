import React from 'react'

import noFoundMoviesMock from '../mocks/not_found.json'

const ListMovies = ({ movies }) => {
  return (
    <ul className='movies'>
      {
        movies.map(movie => (
          <li className='movie' key={movie.id}>
            <h3>{movie.title}</h3>
            <p>{movie.year}</p>
            <img src={movie.image} alt={movie.title} />
          </li>
        ))
      }
    </ul>
  )
}

const MoviesNotFound = () => {
  return (
    <p>{noFoundMoviesMock.Error}</p>
  )
}

export function Movies ({ movies }) {
  const hasMovies = movies?.length > 0

  return (
    <>{
      hasMovies
        ? <ListMovies movies={movies} />
        : <MoviesNotFound />
    }
    </>
  )
}
