using System;
using System.IO;

namespace CaseSelector
{
    internal static class FileUtil
    {
        private static string _filePath = string.Empty;
        private static int _numberOfCases;

        public static string GetFile()
        {
            do
            {
                Console.WriteLine("Enter file path or print exit to escape: ");
                var inputFilePath = Console.ReadLine().Trim();
                if (inputFilePath.ToLower() == "exit")
                {
                    Environment.Exit(0);
                }
                if (File.Exists(inputFilePath))
                {
                    _filePath = inputFilePath;
                }
                else
                {
                    Console.WriteLine($"'{inputFilePath}' file doesn't exist.");
                }
            }
            while (_filePath == string.Empty);
            return _filePath;
        }

        public static int GetNumberOfCases()
        {
            Console.WriteLine("Enter required number of cases (default = 10): ");
            var converted = int.TryParse(Console.ReadLine(), out _numberOfCases);
            if (!converted || _numberOfCases< 1)
            {
                _numberOfCases = 10;
            }
            return _numberOfCases;
        }
    }
}
