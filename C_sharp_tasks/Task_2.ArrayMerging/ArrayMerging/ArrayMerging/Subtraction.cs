using System;
using System.Collections.Generic;
using System.Linq;

namespace ArrayMerging
{
    internal static class Subtraction
    {
        private const string Separator = ", ";
        public static void SubtractArrays(string[] firstArray, string[] secondArray)
        {
            var resultArray = new string[firstArray.Length - secondArray.Length];
            var index = 0;
            foreach (var item in firstArray)
            {
                if (!secondArray.Contains(item))
                {
                    resultArray[index] = item;
                    index++;
                }
            }
            PrintResult(firstArray.ToList(), secondArray.ToList(), resultArray.ToList());
        }

        public static void SubtractLists(List<string> firstList, List<string> secondList)
        {
            var resultList = firstList.Except(secondList).ToList();
            PrintResult(firstList, secondList, resultList);
        }

        private static void PrintResult(List<string> minuend, List<string> subtrahend, List<string> difference)
        {
            Console.WriteLine($"Minuend: \n {string.Join(Separator, minuend)} \nSubtrahend: \n {string.Join(Separator, subtrahend)} " +
                              $"\nDifference: \n {string.Join(Separator, difference)}");
        }
    }
}
