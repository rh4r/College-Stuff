/*
Challenge 2 — Number Analyzer

Ask the user (or hard-code values if not using input) for a list of numbers and write functions to:
Find the largest number
Find the smallest number
Calculate the average

Requirements:
Use a typed array (number[])
Use a for loop or for..of
Use at least 3 functions
 */
const NUMBERLIST = [
  50,
  5,
  10,
  2,
];

function ReturnLargestNumber(list_o_numbers: Array<any>)
{
  var CurrentLargestNumber = 0;
  for (let numb in list_o_numbers)
  {
    let RealNumb = parseInt(list_o_numbers[numb]);
    if (RealNumb > CurrentLargestNumber)
    {
      CurrentLargestNumber = RealNumb;
    }
  }
  return CurrentLargestNumber;
}

function ReturnSmallestNumber(list_o_numbers: Array<any>)
{
  var CurrentLargestNumber = 0;
  for (let numb in list_o_numbers)
  {
    let RealNumb = parseInt(list_o_numbers[numb]);
    if (RealNumb < CurrentLargestNumber)
    {
      CurrentLargestNumber = RealNumb;
    }
  }
  return CurrentLargestNumber;
}

function ReturnAverageNumber(list_o_numbers: Array<any>)
{
  var Average = 0;
  var TrueNumbers = []

  for (let numb in list_o_numbers)
  {
    let RealNumb = parseInt(list_o_numbers[numb]);
    TrueNumbers.push(RealNumb);
  }

  for (let n in TrueNumbers)
  {
    Average += TrueNumbers[n];
  }
  return Math.floor(Average / 3);
}

let LargestNumber = ReturnLargestNumber(NUMBERLIST);
let SmallestNumber = ReturnSmallestNumber(NUMBERLIST);
let AverageNumber = ReturnAverageNumber(NUMBERLIST);

console.log(
  `Largest number is ${LargestNumber}`,
  `Smallest number is ${SmallestNumber}`,
  `Average number is ${AverageNumber}`,
)
