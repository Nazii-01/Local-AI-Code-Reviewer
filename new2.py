public class TextCheck {
    public static void main(String[] args) {
        String input1 = "hello";
        String input2 = new String("hello");
        
        if (input1 == input2) {
            System.out.println("The words match!");
        } else {
            System.out.println("The words do not match!");
        }
    }
}
