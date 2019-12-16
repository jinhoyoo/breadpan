import { NextPage } from "next";
import Layout from "../../components/Layout";
import ToDoList from "../../components/ToDoList";
import Link from "next/link";
import { sampleFetchWrapper } from "../../utils/sample-api";
import { Todo } from "../../interfaces";

type Props = {
  items: Todo[];
  pathname: string;
};

const WithInitialProps: NextPage<Props> = ({ items, pathname }) => {
  return (
    <Layout title="Users List | Next.js + TypeScript Example">
      <h1>ToDo app</h1>

      <p>You are currently on: {pathname} </p>
      <ToDoList items={items} />
      <p>
        <Link href="/">
          <a>Go home</a>
        </Link>
      </p>
    </Layout>
  );
};

WithInitialProps.getInitialProps = async ({ pathname }) => {
  // Example for including initial props in a Next.js function component page.
  // Don't forget to include the respective types for any props passed into
  // the component.
  const items: Todo[] = await sampleFetchWrapper("http://localhost:5000/todos");

  return { items, pathname };
};

export default WithInitialProps;
