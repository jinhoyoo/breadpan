import * as React from "react";
import { Todo } from "../interfaces";

type Props = {
  items: Todo[];
};

const TodoList: React.FunctionComponent<Props> = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={item.key}>
        <p>{item.task}</p>
      </li>
    ))}
  </ul>
);

export default TodoList;
