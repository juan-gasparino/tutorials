import { useState } from 'react'

import MoviesList from './MoviesList'

const Search = () => {

  const [moviesString, setMoviesString] = useState("")
  const [moviesArr, setMoviesArr] = useState([])

  const handleChange = (e) => {
    setMoviesString(e.target.value)
  }

  const findMovies = async () => {
    try {
      let arr = []
      let objt = {
        "id": "",
        "name": "",
        "year": 0,
        "type": "",
        "imageUrl": ""
      }
      let moviesArray = moviesString.split(';')
      let url = ""
      moviesArray.map(async (movie) => {
        url = `https://moviesdatabase.p.rapidapi.com/titles/search/akas/${movie}`
        const result = await fetch(url, {
          method: 'GET',
          headers: {
            'X-RapidAPI-Key': '<YOUR-PERSONAL-API-KEY-GOES-HERE>',
            'X-RapidAPI-Host': 'moviesdatabase.p.rapidapi.com'
          }
        })
        const data = await result.json()
        if (data.results.length > 0) {
          objt = {
            "id": data.results[0].id,
            "name": data.results[0].titleText.text,
            "year": data.results[0].releaseYear.year,
            "type": data.results[0].titleType.text,
            "imageUrl": data.results[0].primaryImage !== null ? data.results[0].primaryImage.url : "",
          }
          arr.push(objt)
          if (arr.length === moviesArray.length) {
            setMoviesArr(arr)
          }
        }
      })
    } catch (error) {
      console.error(error)
    }
  }

  return (
    <>
      <input
        placeholder="Movies separete by ;"
        className="Search"
        onChange={handleChange}
      />
      <button onClick={findMovies}>Search</button>
      <MoviesList moviesArray={moviesArr} />
    </>
  )
}

export default Search
