import React from 'react'

const MoviesList = React.memo(props => {

  const paginate = (array, page_size, page_number) => {
    return array.slice(page_number * page_size, (page_number + 1) * page_size)
  }

  console.log(props.moviesArray)
  console.log(paginate(props.moviesArray, 5, 0))

  return (
    <>
    </>
  )
})

export default MoviesList
