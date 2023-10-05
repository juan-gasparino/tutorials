import { callRandomCatService, callRandomImageService } from '../services/endpoints.js'
import { useEffect, useState } from 'react'

export function useCatFact () {
  const [fact, setFact] = useState()

  const callRandomCat = async () => {
    const newFact = await callRandomCatService()
    setFact(newFact)
  }

  useEffect(() => {
    callRandomCat()
  }, [])

  return { fact, callRandomCat }
}

export function useCatRandomImage ({ fact }) {
  const [imageUrl, setImageUrl] = useState()

  const callRandomImage = async () => {
    const newImageUrl = await callRandomImageService(fact)
    setImageUrl(newImageUrl)
  }

  useEffect(() => {
    if (!fact) return
    callRandomImage()
  }, [fact])

  return { imageUrl }
}
