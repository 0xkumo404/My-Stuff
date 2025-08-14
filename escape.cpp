#include <iostream>
#include <string>
 
    std::string items;
    std::string done;
	std::string reset;
	std::string does;
    std::string item;
	float code = 0;
    float safecode = 0;
    int t;
    int t1;
    int t2 = 3;
    int x3;
    std::string answer;
    std::string answer2;
    int answer3;


int main() {

//Introduction
std::system("clear");
std::cout << "YOU ARE LOCKED IN A DORM AND DON'T KNOW HOW TO GET OUT...\n\n";
std::cout << "AFTER EVERY ACTION YOU GO BACK TO THE START HOME PAGE\n\n";
std::cout << "ALL INPUTS NEED TO BE LOWERCASE OR NUMERIC WHEN NEEDED (OR ELSE YOU MIGHT BREAK THE GAME[NOT IN A GOOD WAY])\n\n";
std::cout << "YOU WILL NEED TO LOOK UP INFORMATION AT SOME PARTS OF THIS ESCAPE\n\n\n";

 while (code != 2009) {
 //home page
 std::cout << "PRESS ENTER TO CONTINUE";
 std::cin.ignore();
 std::cin.get();
 std::system("clear");
 std::cout << "YOU ARE NOW IN THE CENTER OF THE ROOM\n";
 std::cout << "\nWHERE DO YOU WANT TO GO?\n";
 std::cout << "  W \n";
 std::cout << "A   D\n";
 std::cout << "  S  \n";
 std::cout << "(I)NVENTORY\n";
 std::cout << "(Q)UIT\n";
 std::cout << "(ALL LOWERCASE)\n";
 std::cin >> done;
 std::cout << "\n";


//if w 
  if (done == "w") {
  std::cout << "YOU SEE A DOOR WITH A LOCK ON IT.\n\n";
  std::cout << "THE LOCK HAS A FOUR DIGIT CODE:\n";
  std::cout << "(NUMBERS ONLY)\n\n";
  std::cin >> code;
	if (code == 2009) {
        std::cout << "YOU OPEN THE FIRST DOOR JUST TO FIND A SECOND DOOR WITH ANOTHER LOCK ON IT.";
        std::cout << "\nDO YOU REMEMBER THE CODE ON THE POSTER? IF NOT YOU ONLY HAVE THREE TRYS TO REMEMBER IT.";
        if (t2 == 0) {
            std::cout << "\nYOU LOSE, I AM SORRY YOU NEED TO RESTART. :(";
                return 0;
        } else if (t2 > 0) {
            std::cout << "YOU HAVE " << t2 << "TRIES LEFT";
            std::cin >> answer3;
            if (answer3 == 4218) {
	            std::cout << "\nYOU UNLOCK THE DOOR AND WALK BACK OUT TO THE LOBBY WHERE THE OWNER OF THE ESCAPE ROOM ASKS IF YOU HAD A GOOD TIME.\n\n";
	            return 0;
            }
	    }
    }
	if (code != 2009) {
	std::cout << "\nINNCORRECT CODE.\n\n"; 
	}
  
//if a    
  } else if (done == "a") {
  std::cout << "YOU ENTER A BEDROOM WITH A TABLE, A  BED, AND A POSTER OF A CAT.\n\n";
  std::cout << "WHAT DO YOU WANT TO DO?\n";
  std::cout << "(L)OOK\n(S)EARCH\n(U)SE ITEM\n";
  std::cin >> does;

    //looking in room
  	if (does == "look" || does == "L" || does == "l") {
    std::cout << "\n\nYOU FIND ON THE POSTER AND IN FADED TEXT IN THE CORNER SAYING 'CODE 4218.'\n\n";

    //searching room
    } else if (does == "search" || does == "S" || does == "s") {
        if (t < 1) {
            std::cout << "\nYOU FIND A SMALL KEY UNDER THE BED, AND A PIECE OF PAPER ON THE TABLE. IT SAYS, '..- ... .  *******  --- -.  .-- .. -. -.. --- .--'\n\n";
            std::cout << "YOU CAN'T MAKE OUT THE MIDDLE WORD\n\n";
            items.push_back('K');
            items.push_back('E');
            items.push_back('Y');
            items.push_back('<');
            items.push_back('2');
            items.push_back('7');
            items.push_back('1');
            items.push_back('5');
            items.push_back('>');
            items.push_back('\n');
            t++;
        } else if (t >= 1) {
            std::cout << "\nTHE PIECE OF PAPER SAYS: '..- ... .  *******  --- -.  .-- .. -. -.. --- .--'\n\n";
        }
    
    //using item  
    } else if (does == "use item" || does == "U" || does == "u") {
        std::cout << "WHAT ITEM DO YOU WANT TO USE:";
        std::cin >> item;
        std::cout << "IT DOES NOTHING\n";
    } 

//if s
  } else if (done == "s") {
    std::cout << "YOU SEE A METAL BAR WINDOW.\n\n";
    std::cout << "WHAT DO YOU WANT TO DO?\n";
    std::cout << "LOOK\nSEARCH\nUSE ITEM\n";
    std::cin >> does;
    if (does == "look" || does == "L" || does == "l") {
        std::cout << "\nYOU STILL SEE A WINDOW GUARDED BY METAL BARS, WAIT, IS ONE OF THE BARS LOOSE?\n\n";
    } else if (does == "search" || does == "s" || does == "S") {
        std::cout << "\nYOU FIND A BAR THAT IS A BIT LOOSE, BUT YOU CANNOT REMOVE IT\n";
    } else if (does == "use item" || does == "U" || does == "u") {
        std::cout << "WHAT ITEM DO YOU WANT TO USE:";
        std::cin >> item;
        if (item == "wrench") {
            std::cout << "YOU HIS THE BAR AND IT MOVES IT ENOUGH TO LET A PIECE OF PAPER SLIP OUT.";
            std::cout << "\nIT SAYS, 'THE BIRTHDAY OF THE FIRST STUNT DOUBLE'\n";
            std::cout << "(DD-MM-YYYY)";
            if (answer == "5-22-1922") {
                std::cout << "CORRECT! THAT MUST BE THE CODE TO THE MIRROR";
            } else {
                std::cout << "THAT CAN'T BE RIGHT, I WONDER WHAT IT COULD BE?";
            }
        } else {
            std::cout << "IT DOES NOTHING\n";
        }
    }

//if d
  } else if (done == "d") {
    std::cout << "YOU GO INTO A BATHROOM WITH A SINK, A MIRROR, AND A TOILET.\n\n";
    std::cout << "WHAT DO YOU WANT TO DO?\n";
    std::cout << "LOOK\nSEARCH\nUSE ITEM\n";
    std::cin >> does;
    if (does == "look" || does == "L" || does == "l") {
        std::cout << "YOU SEE THAT THE MIRROR HAS HINGES AND A LOCK WHAT COULD THE CODE BE? (NUMBERS ONLY)\n";
        std::cin >> answer2;
        if (answer2 == "5-22-1922") {
                std::cout << "CORRECT! THE MIRROR OPENS AND YOU FIND A SMALL COMPARTMENT.";
                std::cout << "INSIDE THE COMPARTMENT YOU FIND A SMALL BOX WITH A LOCK ON IT THAT REQUIRES A KEY";
                if (t >= 1) {
                    std::cout << "YOU REMEBER THAT YOU HAVE A KEY!\nYOU PUT IN IN THE LOCK AND THE BOX OPENS\nTHE PIECE OF PAPER HAS FOUR NUMBERS 2009!";
                }
        } else {
            std::cout << "INCORRECT CODE";
        }

    } else if (does == "search" || does == "S" || does == "s") {
        if (t1 < 1) {
        std::cout << "YOU FIND A WRENCH IN THE WATER STORAGE OF THE TOILET\n\n";
        items.push_back('W');
        items.push_back('R');
        items.push_back('E');
        items.push_back('N');
        items.push_back('C');
        items.push_back('H');
        items.push_back('\n');
        t++;
        } else if (t1 >= 1) {
            std::cout << "NOTHING ELSE HERE";
        }
    } else if (does == "use item" || does == "U" || does == "u") {
        std::cout << "WHAT ITEM DO YOU WANT TO USE:";
        std::cin >> item;
        std::cout <<"IT DOES NOTHING\n";
    }

//if quit
  } else if (done == "quit" || done == "q") {
    std::cout << "YOU CHOSE TO QUIT, YOU LOSE :( BYE\n";
    return 0;

//if inventory  
  } else if (done == "i" || done == "inventory") {
      std::cout << items;
      std::cout << "\n";
 
//if else
  } else {
    std::cout << "\nINVALID INPUT PLEASE TRY AGAIN.\n\n";
  }
 }
}
