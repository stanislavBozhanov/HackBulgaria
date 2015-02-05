import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;

public class PrimesInAnInterval {
    public static boolean isValidInterval(int start, int end) {
        if (start > 0 && end >= start) {
            return true;
        }
        return false;
    }

    public static boolean isPrime(int number) {
        if (number == 0 || number == 1) {
            return false;
        }
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static List primesInAnInterval(int from, int to) {
        if (!isValidInterval(from, to)) {
            throw new InputMismatchException("invalid input");
        }
        List numbers = new ArrayList();
        for (int i = from; i <= to; i++) {
            if (isPrime(i)) {
                numbers.add(i);
            }
        }
        return numbers;
    }
    public static void main(String[] args) {
        List output = primesInAnInterval(1, 100);
        System.out.println(output);
    }
}
