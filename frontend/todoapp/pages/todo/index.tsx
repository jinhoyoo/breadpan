import { NextPage } from 'next'

import Layout from '../../components/Layout'


const WithInitialProps: NextPage = () => {
  return (
    <Layout title="Users List | Next.js + TypeScript Example">
      <h1>ToDo app</h1>
      {/* <p>
      Example fetching data from inside <code>getInitialProps()</code>.
    </p>
    <p>You are currently on: {pathname}</p>
    <List items={items} />
    <p>
      <Link href="/">
        <a>Go home</a>
      </Link>
    </p> */}
    </Layout>
  )
}

// WithInitialProps.getInitialProps = async ({ pathname }) => {
//   // Example for including initial props in a Next.js function component page.
//   // Don't forget to include the respective types for any props passed into
//   // the component.
//   const items: User[] = await sampleFetchWrapper(
//     'http://localhost:3000/api/users'
//   )

//   return { items, pathname }
// }

export default WithInitialProps