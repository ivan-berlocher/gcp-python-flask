import Head from 'next/head';
import DevStudio from '../components/DevStudio';

export default function Home() {
  return (
    <>
      <Head>
        <title>DevStudio</title>
      </Head>
      <DevStudio />
    </>
  );
}
