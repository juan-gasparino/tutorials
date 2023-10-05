import { React } from 'react-dom'

import { TwitterFollowCard } from './TwitterFollowCard'

const users = [
  {
    name: 'Jane Clare Johnsson',
    userName: 'janecj',
    isFollowing: true
  },
  {
    name: 'John Doe Smith',
    userName: 'jodosmi',
    isFollowing: false
  },
  {
    name: 'Paco Alvarez',
    userName: 'pacalva',
    isFollowing: true
  }
]

export function App () {
  return (
    <section className='App'>
      {
        users.map(({ userName, name, isFollowing }) => (
          <TwitterFollowCard
            /* do not use math random of new date to force new keys etc etc */
            key={userName}
            userName={userName}
            initialIsFollowing={isFollowing}
          >
            {name}
          </TwitterFollowCard>
        ))
      }
    </section>
  )
}
