import java.util.ArrayList;
import java.util.List;

public class UserManager {
    public static void main(String[] args) {
        List<String> activeUsers = new ArrayList<>();
        activeUsers.add("Alice");
        activeUsers.add("Bob");

        String searchUser = new String("Alice");

        // Bug: Using the wrong comparison tool
        for (String user : activeUsers) {
            if (user == searchUser) { 
                System.out.println("Found user: " + user);
            }
        }
    }
}
