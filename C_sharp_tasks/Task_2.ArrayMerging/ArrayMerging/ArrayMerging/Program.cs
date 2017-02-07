using System;
using System.Linq;

namespace ArrayMerging
{
    public static class Program
    {
        private static readonly string[] FirstArray = { "Alex", "Dima", "Kate", "Galina", "Ivan" };
        private static readonly string[] SecondArray = { "Dima", "Ivan", "Kate" };
        private static void Main()
        {
            Subtraction.SubtractArrays(FirstArray, SecondArray);
            Subtraction.SubtractLists(FirstArray.ToList(), SecondArray.ToList());
            Console.ReadLine();
        }
    }
}
