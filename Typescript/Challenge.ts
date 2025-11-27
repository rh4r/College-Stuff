//Challenge 1 — To-Do List Manager (Console Version)
//Create a script that:
//Starts with an empty array of strings
//Has functions to add a task, remove a task, and display all tasks
//Demonstrates calling those functions in a sequence

//Requirements:
//Use type annotations
//Use a loop to print the list
//Use a function with a return type

let TODO_LIST = [Array<string>];


function AddTask(task_adding: any)
{
  TODO_LIST.push(task_adding);
};

function RemoveTask()
{
  TODO_LIST.pop;
};


function DisplayTask(display_list: any)
{
  for (let index in display_list){
    console.log(display_list[index]);
  }
};

AddTask("My Homework")
AddTask("Study for a test")
RemoveTask();
DisplayTask(TODO_LIST);
