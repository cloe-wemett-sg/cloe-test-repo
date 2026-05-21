import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BankAccount {

    enum TransactionType { DEPOSIT, WITHDRAWAL, TRANSFER }

    record Transaction(TransactionType type, double amount, double balanceAfter, LocalDateTime timestamp) {
        @Override
        public String toString() {
            return String.format("[%s] %s $%.2f  → balance: $%.2f",
                timestamp.toLocalDate(), type, amount, balanceAfter);
        }
    }

    private final String owner;
    private final String accountNumber;
    private double balance;
    private final List<Transaction> history = new ArrayList<>();

    public BankAccount(String owner, String accountNumber, double initialBalance) {
        if (initialBalance < 0) throw new IllegalArgumentException("Initial balance cannot be negative");
        this.owner = owner;
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("Deposit must be positive");
        balance += amount;
        history.add(new Transaction(TransactionType.DEPOSIT, amount, balance, LocalDateTime.now()));
    }

    public void withdraw(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("Withdrawal must be positive");
        if (amount > balance) throw new IllegalStateException("Insufficient funds");
        balance -= amount;
        history.add(new Transaction(TransactionType.WITHDRAWAL, amount, balance, LocalDateTime.now()));
    }

    public void transferTo(BankAccount target, double amount) {
        this.withdraw(amount);
        target.deposit(amount);
        history.add(new Transaction(TransactionType.TRANSFER, amount, balance, LocalDateTime.now()));
    }

    public double getBalance() { return balance; }
    public String getOwner() { return owner; }
    public String getAccountNumber() { return accountNumber; }
    public List<Transaction> getHistory() { return Collections.unmodifiableList(history); }

    public void printStatement() {
        System.out.printf("Account: %s  Owner: %s%n", accountNumber, owner);
        System.out.println("-".repeat(60));
        history.forEach(System.out::println);
        System.out.printf("%-52s $%.2f%n", "Current balance:", balance);
    }

    public static void main(String[] args) {
        BankAccount alice = new BankAccount("Alice", "ACC-001", 1000.00);
        BankAccount bob   = new BankAccount("Bob",   "ACC-002",  250.00);

        alice.deposit(500.00);
        alice.withdraw(200.00);
        alice.transferTo(bob, 300.00);
        bob.deposit(50.00);

        alice.printStatement();
        System.out.println();
        bob.printStatement();
    }
}
