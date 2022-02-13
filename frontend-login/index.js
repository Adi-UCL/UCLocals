import Head from "next/head";
import Register from "./register";
import LoginAuth from "./UCLLoginAuth";

export default function Home() {
  return (
    <div className="container">
      <Head>
        <title>UCLOCALS</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <h1 className="title">UCLocals</h1>
        <div className="grid">
          <LoginAuth />
          <Register />
        </div>
      </main>
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
        `}
      </style>
    </div>
  );
}
