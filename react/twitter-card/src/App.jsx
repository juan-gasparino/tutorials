import { React } from 'react-dom'

import { TwitterFollowCard } from './TwitterFollowCard'

export function App () {
  return (
    <section className='App'>
      <TwitterFollowCard userName='jodosmi' initialIsFollowing={false}>
        John Doe Smith
      </TwitterFollowCard>
    </section>
  )
}
