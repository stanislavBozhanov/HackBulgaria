public class PrimesInAnInterval {
    public static boolean isPrime(int Number) {
        if (Number == 0 || Number == 1) {
            return false;
        }
        for (int i = 2; i < Number / 2; i++) {
            if (Number % i == 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
    }
}
