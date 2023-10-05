const CAT_ENDPOINT_RANDOM_FACT = 'https://catfact.ninja/fact'
const CAT_ENDPOINT_CATAAS = 'https://cataas.com'
const CAT_ENDPOINT_RANDOM_IMAGE_TEXT = CAT_ENDPOINT_CATAAS + '/cat/says/:text?size=50&color=red&json=true'

export const callRandomCatService = async () => {
  const res = await fetch(CAT_ENDPOINT_RANDOM_FACT)
  const response = await res.json()
  const { fact } = response
  return fact
}

export const callRandomImageService = async (fact) => {
  const threeFirstWords = fact.split(' ').slice(0, 3).join(' ')

  return fetch(CAT_ENDPOINT_RANDOM_IMAGE_TEXT.replace(':text', threeFirstWords))
    .then(res => res.json())
    .then(response => {
      const { url } = response
      return (CAT_ENDPOINT_CATAAS + url)
    })
}
