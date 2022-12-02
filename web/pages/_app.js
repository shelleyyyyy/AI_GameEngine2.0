import '../styles/globals.css'
import Layout from '../components/Layout'

function MyApp({ Component, pageProps }) {
  return (
    <div data-theme="cupcake" class=" pb-96">
      <Layout>
      <Component {...pageProps} />
    </Layout> 
    </div>
  )
}

export default MyApp
