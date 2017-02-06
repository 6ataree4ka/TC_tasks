using System;
using System.Collections.Generic;
using System.Linq;

namespace ArrayMerging
{
    class ArrayMerging
    {
        static void Main(string[] args)
        {
            string[] first = new string[] { "Alex", "Dima", "Kate", "Galina", "Ivan" };
            string[] second = new string[] { "Dima", "Ivan", "Kate" };
            string[] result = first.Except(second).ToArray();
            Console.WriteLine("First array is: {0}", string.Join(", ", first));
            Console.WriteLine("Second array is: {0}", string.Join(", ", second));
            Console.WriteLine("Subtract of arrays is: {0}", string.Join(", ", result));

            Console.WriteLine();

            List<string> firstList = new List<string>() { "Alex", "Dima", "Kate", "Galina", "Ivan" };
            List<string> secondList = new List<string>() { "Dima", "Ivan", "Kate" };
            List<string> resultList = firstList.Except(secondList).ToList<string>();
            Console.WriteLine("First list is: {0}", string.Join(", ", firstList));
            Console.WriteLine("Second list is: {0}", string.Join(", ", secondList));
            Console.WriteLine("Subtract of lists is: {0}", string.Join(", ", resultList));

            Console.ReadLine();
        }
    }
}
