import React from 'react'

function Login() {
    return (
        <div>
          <form action="">
            <h1>Log In</h1>
            <div>
              <input type= "text" placeholder="Username" required/>
            </div>
            <div>
              <input type= "password" placeholder="Password" required/>
            </div>
            <div>
              <input type= "password" placeholder="Confirm Password" required/>
            </div>
            <button type="submit">Login</button>
          </form>
        </div>
  )
}

export default Login