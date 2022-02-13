const Register = () => {
  const RegisterForm = (
    <div class="container">
      <div class="card">
        <h2 class="card-heading">Let us create your account</h2>
        <form name="register-form" method="POST" action="contact/?success=true">
          <label htmlFor="name">Name</label>
          <input id="name" name="name" required type="text" />
          <label htmlFor="email">Email</label>
          <input id="email" type="text" name="email"></input>
          <label htmlFor="societies">Societies</label>
          <input id="societies" type="text" name="societies"></input>
          <label htmlFor="year">Year</label>
          <input id="year" type="text" name="year"></input>
          <label htmlFor="degree">Degree</label>
          <input id="degree" type="text" name="degree"></input>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );

  return (
    <div>
      <h1>Contact Us</h1>
      {RegisterForm}
      <style jsx global>
        {`
          html,
          body {
            font-size: 18px;
            background-color: #dbd8f4;
            color: #27004e;
            padding: 1em;
            margin: 1em;
            font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
              Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue,
              sans-serif;
          }
          * {
            box-sizing: border-box;
          }
          h1 {
            text-transform: uppercase;
          }
          .container {
            display: flex;
            flex-direction: column;
            width: 80%;
            grid-row-gap: 0.5em;
          }
          @media (max-width: 769px) {
            .container {
              width: 100%;
            }
          }
          label {
            font-size: 1.2em;
          }
          input[type="text"] {
            width: 100%;
            border: 2px solid #aaa;
            border-radius: 4px;
            margin: 8px 0;
            outline: none;
            padding: 8px;
            box-sizing: border-box;
            transition: 0.3s;
          }

          input[type="text"]:focus {
            border-color: dodgerBlue;
            box-shadow: 0 0 8px 0 dodgerBlue;
          }
          button {
            max-width: 400px;
            margin: 0 auto;
            color: #f3f0ee;
            background-color: #022f94de;
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            text-transform: uppercase;
            border-radius: 10px;
          }
          button:hover {
            background-color: #051f58de;
          }
          #UCLSignIn {
            margin-top: 20px;
          }
        `}
      </style>
    </div>
  );
};

export default Register;
