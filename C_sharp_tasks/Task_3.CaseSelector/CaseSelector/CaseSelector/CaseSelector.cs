using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace CaseSelector
{
    internal static class CaseSelector
    {
        public static void SelectCases(string filePath, int numberOfRequiredCases = 10)
        {
            var linesInOriginalFile = File.ReadAllLines(filePath, Encoding.UTF8);
            if (linesInOriginalFile.Length - 1 < numberOfRequiredCases)
            {
                Console.WriteLine("The number of required cases is more than number cases in original file.");
                return;
            }
            var selectedCases = new List<string>();
            var random = new Random();
            var indices = new List<int>();
            while (indices.Count < numberOfRequiredCases)
            {
                var index = random.Next(1, linesInOriginalFile.Length);
                if (indices.Count == 0 || !indices.Contains(index))
                {
                    indices.Add(index);
                    selectedCases.Add(linesInOriginalFile[index]);
                }
            }
            var remainedLinesInOriginalFile = linesInOriginalFile.Except(selectedCases).ToArray();
            selectedCases.Insert(0, linesInOriginalFile[0]);
            var extension = Path.GetExtension(filePath);
            var resultFilePath = filePath.Replace(extension, $"_res{extension}");
            File.WriteAllLines(resultFilePath, selectedCases);
            File.WriteAllLines(filePath, remainedLinesInOriginalFile, Encoding.UTF8);
            Console.WriteLine($"File with required number of cases is placed at {resultFilePath}");
        }
    }
}
