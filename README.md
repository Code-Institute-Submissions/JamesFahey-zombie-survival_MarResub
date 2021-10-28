# Zombie Survival

![Responsive screens](/readme-images/responsive.png)

## Project introduction

Zombie Survival is a text adventure game where the user’s decisions drive the story. The user will be tasked with not only trying to get themselves to safety but also their young family. Each decision made will take them down a different path with multiple endings available. If the user makes the wrong choice, then the game will be over and given the option to try again. 

## Developer's goals

•	Create a text adventure game using Python.

•	Utilise the popularity of Zombies and the time of year by incorporating it as the main theme 

•	Create a game enjoyable to play with incentive to return.

## Target audience

Predominantly aiming towards zombie horror fanbases, but also designed to appeal to those who enjoy choice-based story games with consequences to each decision.

## User stories

### As a developer:

• I want to provide the user with a simple but enjoyable game

• I want to create an immersive story causing the user to feel weight to each choice being made.

• I want to provide the user with clear gameplay instructions.

• I want to be inclusive to everyone and include gender neutral characters

• I want to provide the user with a game that can be played multiple times and still feel different 

• Have the opportunity of either friends/family but also an AI as an opponent. 

### As a new user:

• I want to understand how the game works 

• I want the game to set the scene drawing me into the story

• I want the choices being made to feel like they have consequences

• I want the game to have a compelling story

• I want the game to have multiple outcomes

• I want the game to have some reference to popular zombie culture

• Once the game is completed, I want an option to play again

### As a returning user:

• I want the game to feel new and not repetitive

• I want to have a different outcome

## How to play

The game begins with instructions to the user to simply survive, followed by the question if they want to proceed with the game. Once the user agrees to play an intro to the horrors, which they will face, will begin.

The story will then proceed providing the user with key decisions to make with one wrong move resulting in death to the user and their family. If the user reaches this outcome, they will be provided the option to either play again, starting a new game from the beginning, or to quit.

The user will strive towards four endings with only half being considered as perfect with everyone surviving the ordeal. 


## Data Model

Lucid Charts was used to create a flow chart for the text adventure

![Data Model](/readme-images/data-model.png)

## Features

## Existing features

## Start up

The user will be provided with the goal and theme of the game and provided with the option to play or not. If the user chooses to play the game will begin. 

![Start](/readme-images/start.png)

## Introduction

Once the game has begun the user will be provided with the back story of the game along with some character development. Once this segment has been displayed it will provide the user with their first story driven choice. At this point the game will begin to branch in completely different directions  

![Intro](/readme-images/intro.png)

## Functions

Again, the choice of image was carefully selected to perpetuate the previously mentioned theme of conflict. 

![Functions](/readme-images/functions.png)

## Choices 

Each choice will consist of two options representing two different paths the user can take. The choice made will either continue their journey of survival or cut it short resulting in the user not surviving and getting game over. Once the story comes to an end whether it be successful or not the user will be asked whether they would like to play again. If yes the user will begin the game again

![Choices](/readme-images/choices.png)

## Random Outcome 

A random outcome was added to one of the choices I felt would be least popular. Within the stay function the user will be presented with one of two outcomes. The first is a standard game over message, the second is an easter egg for zombie and gaming fans with a reference to the Resident Evil franchise. 

![Random Outcome](/readme-images/random-outcome.png)

## Endings

The user has 4 possible endings these have been ranked either red, yellow or green. There is only two possible green ending, this being the main objective for the user. Two possible yellow endings and red making up all the rest. 

![Endings](/readme-images/ending.png)

## Invalid input checks

During each choice if the user’s input is invalid, they will be prompted to try again or given the option to quit the game 

![Invalid input checks](/readme-images/valid-check.png)

## Features to be added  

•	The option for the user to save their outcome which can be carried over to later sequels

•	Option to buy the dlc pack. The pack will consist of an expanded storyline with more options and further easter egg surprises


## Technologies used

•	Python

•	Heroku

•	GitHub

•	Gitpod

•	Lucid Charts

## Testing

### Functionality testing

I have manually tested this project by doing the following:

•	Played all possible choices and outcomes to ensure all functions work correctly

•	Given invalid options to ensure the function will check if the user wanted to continue playing or quit the game.

•	Tested in my local terminal and Heroku terminal.

•	Tested by friends and family.

## User stories testing

### As developer:

• I want to provide the user with a simple but enjoyable game

The simple mechanics of the game allow the user to shape the story by typing their answers when prompted 

• I want to create an immersive story causing the user to feel weight to each choice being made.

The story from the beginning adds extra weight for your choices as you are not only making decisions for yourself but also your family. You are put in dangerous and life-threatening situations and you must navigate yourself and family through them 

• I want to provide the user with clear gameplay instructions

The user is prompted when and what to input to progress the story

• I want to provide the user with a game that can be played multiple times and still feel different

With the multiple paths created the user can play several times and not reach the same outcome or path

• I want to be inclusive to everyone and included gender neutral characters

Your partner in the game is called Alex and child Harry so the user’s character could be male or female 

### As a new user:

• I want to understand how the game works 

The user is prompted when and what to input to progress the story

• I want the game to set the scene drawing me into the story

After the user confirms they want to play the intro to the game and story will begin. This will provide the user a background to the events of the game as well as some character development

• I want the game to have a compelling story

The story builds suspense leading up to each choice the user has to make and puts the user in some terrible situations

• I want the choices being made to feel like they have consequences

Every decision you make will affect yourself and those around you, if a wrong choice is made it could lead to death

• I want the game to have multiple outcomes

The game will have four main endings, two endings considered perfect where everyone makes it to the end. One of these endings is considered rare and hard to accomplish. Then two yellow ending where only some of the group survive. To reach one of these endings you will have to avoid several wrong choices which leads to a red ending and all the family’s death 

• I want the game to have some reference to popular zombie culture

The rare perfect ending will include an easter egg and reference to the Resident Evil franchise

• Once the game is completed, I want an option to play again

After the game is completed whether it be successful or not the user will be given the option to play again or exit

### As a returning user:

• I want the game to feel new and not repetitive

With multiple paths and different endings each game will feel completely different

• I want to have a different outcome

To get a different ending you will need to play the game again making different choices along your journey 

## Issues during development

### Game Freezing

While playing, the game sometimes freezes not allowing you to make any further choices. Primarily I thought it was due to functions not being initiated correctly however the freezing is random and all functions have been tested and work correctly.  

### Bugs found on PEP8

•	Unwanted white spaces

•	Incorrect indentation

•	Incorrect line spaces between functions

•	Too many characters on one line

## Validator Testing

•	PEP8 - No errors have been returned from PEP8online.com.

## Deployment

The project was deployed using Code Institutes mock terminal for Heroku

Deployment steps:

•	Fork or clone this repository.

•	Ensure the Profile is in place.

•	requirements.txt can be left empty as this project does not use any external libraries

•	Create a new app in Heroku

•	Select "New" and "Create new app"

•	Name the new app and click "Create new app"

•	In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list)

•	Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files

•	Click on "Deploy" and select your deploy method and repository

•	Click "Connect" on selected repository.

•	Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section

•	Heroku will now deploy the site

## Credits

## Content

•	I used video tutorials from YouTube in order to implement the code needed to create a text adventure
 https://www.youtube.com/watch?v=DEcFCn2ubSg 
 https://www.youtube.com/watch?v=ypNFNr72Xe8&t=2411s


### Design and content inspiration

•	Walking Dead

•	Resident Evil

## Thanks

Special thank you to Adegbenga Adeye for his support and guidance throughout the project