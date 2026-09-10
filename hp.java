public class ProfileCheck {
    public static void main(String[] args) {
        String username = null; 

        // Bug: Calling a method on a null reference
        if (username.equals("admin")) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied.");
        }
    }
}
