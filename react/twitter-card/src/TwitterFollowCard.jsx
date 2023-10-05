import { useState } from 'react'
import { React } from 'react-dom'

export function TwitterFollowCard ({ children, userName, initialIsFollowing }) {
  const [isFollowing, setIsFollowing] = useState(initialIsFollowing)

  const text = isFollowing ? 'Following' : 'Follow'
  const buttonClassName = isFollowing
    ? 'tw-followCard-follow-btn is-following'
    : 'tw-followCard-follow-btn'

  const handleClick = () => {
    setIsFollowing(!isFollowing)
  }

  return (
    <article className='tw-followCard'>
      <header className='tw-followCard-header'>
        <img
          className='tw-followCard-header-avatar'
          src='https://picsum.photos/200'
          alt='photo user test'
        />
        <div className='tw-followCard-header-userInfo'>
          <strong className='tw-followCard-header-userInfo-name'>{children}</strong>
          <span className='tw-followCard-header-userInfo-nickname'>@{userName}</span>
        </div>
      </header>
      <aside className='tw-followCard-follow'>
        <button className={buttonClassName} onClick={handleClick}>
          {text}
        </button>
      </aside>
    </article>
  )
}
