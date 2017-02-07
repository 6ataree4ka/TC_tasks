using System;

namespace CaseSelector
{
    public static class Program
    {
        private static void Main()
        {
            var filePath = FileUtil.GetFile();
            var numberOfCases = FileUtil.GetNumberOfCases();
            CaseSelector.SelectCases(filePath, numberOfCases);
            Console.ReadLine();
        }
    }
}
