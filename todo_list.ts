// Test file for cloe-test-repo — feel free to read, edit, or delete this.
type Priority = "low" | "medium" | "high";

interface Todo {
  id: number;
  title: string;
  completed: boolean;
  priority: Priority;
  createdAt: Date;
}

class TodoList {
  private todos: Todo[] = [];
  private nextId = 1;

  add(title: string, priority: Priority = "medium"): Todo {
    const todo: Todo = {
      id: this.nextId++,
      title,
      completed: false,
      priority,
      createdAt: new Date(),
    };
    this.todos.push(todo);
    return todo;
  }

  complete(id: number): boolean {
    const todo = this.findById(id);
    if (!todo) return false;
    todo.completed = true;
    return true;
  }

  remove(id: number): boolean {
    const index = this.todos.findIndex((t) => t.id === id);
    if (index === -1) return false;
    this.todos.splice(index, 1);
    return true;
  }

  getByPriority(priority: Priority): Todo[] {
    return this.todos.filter((t) => t.priority === priority);
  }

  getPending(): Todo[] {
    return this.todos.filter((t) => !t.completed);
  }

  getCompleted(): Todo[] {
    return this.todos.filter((t) => t.completed);
  }

  private findById(id: number): Todo | undefined {
    return this.todos.find((t) => t.id === id);
  }

  summary(): string {
    const total = this.todos.length;
    const done = this.getCompleted().length;
    return `${done}/${total} tasks completed`;
  }
}

const list = new TodoList();
list.add("Buy groceries", "low");
list.add("Write report", "high");
list.add("Call dentist", "medium");
list.add("Fix CI pipeline", "high");
list.complete(1);
list.complete(3);

console.log(list.summary());
console.log("Pending high priority:", list.getByPriority("high").filter((t) => !t.completed));
