import java.util.*;
public class Chatbot
{
  public static void main(String[] args) 
   {
	 Scanner scanner = new Scanner(System.in);
     String user1;
	 System.out.println("Chatbot: Hello! I am a simple chatbot. How can I help you today?");
	   do
	   {
	     System.out.println("YOU: ");
	      user1 = scanner.nextLine();
	       if (user1.equalsIgnoreCase("hello")||user1.equalsIgnoreCase("hi"))
	        {
	          System.out.println("Chatbot Resposne: Hi there!");
	        } 
	       else if (user1.equalsIgnoreCase("how are you")||user1.equalsIgnoreCase("how are you feeling"))
	       {
	         System.out.println("Chatbot Resposne: I'm just a program, but thanks for asking!");
	       } 
	       else if (user1.equalsIgnoreCase("any special news today?")||user1.equalsIgnoreCase("any news today?")||user1.equalsIgnoreCase("anything special today?")) 
	       {
	         System.out.println("Chatbot Resposne: Nothing");
	       } 
	        else if (user1.equalsIgnoreCase("bye")) 
	       {
	        System.out.println("Chatbot Resposne: Goodbye! Have a great day!Hope to see you again!");
	         break; 
	       } 
	       else 
	       {
	        System.out.println("Chatbot Resposne: I'm sorry, I didn't understand that. Can you please clarify?");
	         break;
	        }
	}while(user1!="bye"||user1 !="BYE");

  scanner.close();
	}

}