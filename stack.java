// Test file for cloe-test-repo — feel free to read, edit, or delete this.
import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

public class stack {

    static class Stack<T> {
        private final List<T> data = new ArrayList<>();

        public void push(T item) {
            data.add(item);
        }

        public T pop() {
            if (isEmpty()) throw new EmptyStackException();
            return data.remove(data.size() - 1);
        }

        public T peek() {
            if (isEmpty()) throw new EmptyStackException();
            return data.get(data.size() - 1);
        }

        public boolean isEmpty() {
            return data.isEmpty();
        }

        public int size() {
            return data.size();
        }

        @Override
        public String toString() {
            return data.toString();
        }
    }

    static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (c == ')' || c == ']' || c == '}') {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    static String reverseWords(String sentence) {
        Stack<String> stack = new Stack<>();
        for (String word : sentence.split(" ")) {
            stack.push(word);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
            if (!stack.isEmpty()) sb.append(" ");
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Stack<Integer> nums = new Stack<>();
        for (int i = 1; i <= 5; i++) nums.push(i * 10);
        System.out.println("Stack: " + nums);
        System.out.println("Pop: " + nums.pop());
        System.out.println("Peek: " + nums.peek());

        System.out.println(isBalanced("({[]})"));
        System.out.println(isBalanced("({[})"));
        System.out.println(reverseWords("hello world foo bar"));
    }
}
