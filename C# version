using System;
// PICK A PSEUDO RANDOM NUMBER //
// MAKE A TIMER TO SEE HOW FAST A QUESTION WAS AWNSERED
// MAKE A LOOP FOR THE QUESTION//
// MAKE THE LOOP, LOOP FOR THE AMOUNT THE USER WANTS IT TOO//
// MAKE MIXED ?!!??!?!?!?!?!?!?!??!?!?!?!




public class Program {

  public static void Main(string[] args) {
  Menu();


  }
 public static void divison(){
    Console.WriteLine("How Many Questions Would You Like?");
    int q = int.Parse(Console.ReadLine());
    int a = 0;
    int correct = 0;
    int incorrect = 0;
    while (a != q){
    Random rnd = new Random();
    int num1 = rnd.Next(1,100);
    int num2 = rnd.Next(1,100);
    // generate random number
    var ans = num1/num2;
    Console.WriteLine($"{num1} / {num2} = ?");
    int usrans =  int.Parse(Console.ReadLine());
    // add 2 random numbers together and asks user the question
    if (usrans == ans){
      Console.WriteLine("This is correct");
      Console.WriteLine($"{num1} / {num2} = {ans}");
      correct++;
      }
    else{
      Console.WriteLine("Incorrect The Correct Awnser Is");
      Console.WriteLine($"{num1} / {num2} = {ans}");
      incorrect++;

      }
    // checks if the user's awnser is correct or incorrect 
      a++;
    // adds one to the loop
    }
    Console.WriteLine($"You Got {correct} Correct");
    Console.WriteLine($"You Got {incorrect} Incorrect");
    System.Threading.Thread.Sleep(1000);
    Console.Clear();
  }



  public static void subtraction(){
    Console.WriteLine("How Many Questions Would You Like?");
    int q = int.Parse(Console.ReadLine());
    int a = 0;
    int correct = 0;
    int incorrect = 0;
    while (a != q){
    Random rnd = new Random();
    int num1 = rnd.Next(1,100);
    int num2 = rnd.Next(1,100);
    // generate random number
    var ans = num1-num2;
    Console.WriteLine($"{num1} - {num2} = ?");
    int usrans =  int.Parse(Console.ReadLine());
    // add 2 random numbers together and asks user the question
    if (usrans == ans){
      Console.WriteLine("This is correct");
      Console.WriteLine($"{num1} - {num2} = {ans}");
      correct++;
      }
    else{
      Console.WriteLine("Incorrect The Correct Awnser Is");
      Console.WriteLine($"{num1} - {num2} = {ans}");
      incorrect++;

      }
    // checks if the user's awnser is correct or incorrect 
      a++;
    // adds one to the loop
    }
    Console.WriteLine($"You Got {correct} Correct");
    Console.WriteLine($"You Got {incorrect} Incorrect");
    System.Threading.Thread.Sleep(10000);
    Console.Clear();
  
  }



  public static void addition(){
    Console.WriteLine("How Many Questions Would You Like?");
    int q = int.Parse(Console.ReadLine());
    int a = 0;
    int correct = 0;
    int incorrect = 0;
    while (a != q){
    Random rnd = new Random();
    int num1 = rnd.Next(1,100);
    int num2 = rnd.Next(1,100);
    // generate random number
    var ans = num1+num2;
    Console.WriteLine($"{num1} + {num2} = ?");
    int usrans =  int.Parse(Console.ReadLine());
    // add 2 random numbers together and asks user the question
    if (usrans == ans){
      Console.WriteLine("This is correct");
      Console.WriteLine($"{num1} + {num2} = {ans}");
      correct++;
      }
    else{
      Console.WriteLine("Incorrect The Correct Awnser Is");
      Console.WriteLine($"{num1} + {num2} = {ans}");
      incorrect++;

      }
    // checks if the user's awnser is correct or incorrect 
      a++;
    // adds one to the loop
    }
    Console.WriteLine($"You Got {correct} Correct");
    Console.WriteLine($"You Got {incorrect} Incorrect");
    System.Threading.Thread.Sleep(10000);
    Console.Clear();
  
  }

  public static void mulitplication(){
    Console.WriteLine("How Many Questions Would You Like?");
    int q = int.Parse(Console.ReadLine());
    int a = 0;
    int correct = 0;
    int incorrect = 0;
    while (a != q){
    Random rnd = new Random();
    int num1 = rnd.Next(1,12);
    int num2 = rnd.Next(1,12);
    // generate random number
    var ans = num1*num2;
    Console.WriteLine($"{num1} * {num2} = ?");
    int usrans =  int.Parse(Console.ReadLine());
    // add 2 random numbers together and asks user the question
    if (usrans == ans){
      Console.WriteLine("This is correct");
      Console.WriteLine($"{num1} * {num2} = {ans}");
      correct++;
      }
    else{
      Console.WriteLine("Incorrect The Correct Awnser Is");
      Console.WriteLine($"{num1} * {num2} = {ans}");
      incorrect++;

      }
    // checks if the user's awnser is correct or incorrect 
      a++;
    // adds one to the loop
    }
    Console.WriteLine($"You Got {correct} Correct");
    Console.WriteLine($"You Got {incorrect} Incorrect");
    System.Threading.Thread.Sleep(10000);
    Console.Clear();
  
  }
  public static void Mixed(){
    Random rnd = new Random();
    int num1 = rnd.Next(1,100);
    int num2 = rnd.Next(1,100);

    
  }
  
  public static void Menu(){
    Console.WriteLine("Welcome to the math quiz please enter what subject you'd like to do.");
    Console.WriteLine("1. Addition 2.Subtraction 3.Multiplication 4.Divison 5.Mixed");
    int choice = int.Parse(Console.ReadLine());
    System.Threading.Thread.Sleep(100);
    Console.Clear();
    switch (choice){
      case 1:
      addition();
      Menu();
      break;
      case 2:
      subtraction();
      Menu();
      break;
      case 3:
      divison();
      Menu();
      break;
      case 4:
      mulitplication();
      Menu();
      break;
      default:
      Menu();
      break;
    }
  }

}
